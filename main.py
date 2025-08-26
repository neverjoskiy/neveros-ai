import logging
import os
import time
import tkinter as tk
from tkinter import font as tkfont
import pyttsx3
import sounddevice as sd
from scipy.io import wavfile
import numpy as np
import threading
import queue
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from pynput import keyboard, mouse
from flask import Flask, render_template_string, request

# === НАСТРОЙКИ ===
TOKEN = "HybaBuBa49248Jdellas78jfdsHFH"
ADMIN_ID = 1234567
TEMP_AUDIO = "nevoros_temp.wav"
QUEUE = queue.Queue()
STEP = 20

# === ЛОГИРОВАНИЕ ===
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# === УПРАВЛЕНИЕ МЫШЬЮ ===
mouse_controller = mouse.Controller()

def on_press(key):
    try:
        if key == keyboard.Key.up:
            mouse_controller.move(0, -STEP)
        elif key == keyboard.Key.down:
            mouse_controller.move(0, STEP)
        elif key == keyboard.Key.left:
            mouse_controller.move(-STEP, 0)
        elif key == keyboard.Key.right:
            mouse_controller.move(STEP, 0)
        elif key == keyboard.Key.esc:
            print("🛑 Esc — выход")
            os._exit(0)
    except:
        pass

def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return listener

# === TTS ===
def text_to_speech_to_file(text, filename):
    if os.path.exists(filename):
        os.remove(filename)
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'Irina' in voice.name or 'irina' in voice.name or 'russian' in str(voice.languages).lower():
            engine.setProperty('voice', voice.id)
            break
    engine.save_to_file(text, filename)
    engine.runAndWait()
    engine.stop()

# === ВОСПРОИЗВЕДЕНИЕ В МИКРОФОН ===
def play_audio_as_microphone(filename):
    try:
        sr, audio = wavfile.read(filename)
        
        if len(audio.shape) > 1:
            audio = audio.mean(axis=1)  # в моно
        audio = audio.astype(np.float32)
        audio /= np.max(np.abs(audio)) + 1e-6
        audio *= 3.0
        audio = np.clip(audio, -1.0, 1.0)

        devices = sd.query_devices()
        target_device = None
        for i, d in enumerate(devices):
            if d['max_output_channels'] >= 1 and 'CABLE Input' in d['name']:
                target_device = i
                print(f"🎯 Используем: {d['name']} (ID: {i})")
                break

        if target_device is None:
            print("❌ Не найдено устройство 'CABLE Input'")
            return

        # ✅ Правильно: без channels!
        sd.play(audio, samplerate=sr, device=target_device)
        sd.wait()
        print("✅ Аудио отправлено в виртуальный микрофон")

    except Exception as e:
        print(f"❌ Ошибка: {type(e).__name__}: {e}")
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# === GUI: ОКНО NEVOROS ===
class NevorosWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nevoros AI")
        self.root.geometry("600x200")
        self.root.configure(bg='#1e1e1e')
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.95)
        self.root.eval('tk::PlaceWindow . center')

        title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        text_font = tkfont.Font(family="Consolas", size=14)

        tk.Label(self.root, text="🤖 NEVOROS", font=title_font, bg='#1e1e1e', fg='#00ffcc').pack(pady=10)
        self.text_label = tk.Label(self.root, text="Готов к работе...", font=text_font, bg='#1e1e1e', fg='white', wraplength=550, justify='center')
        self.text_label.pack(pady=10)
        tk.Label(self.root, text="● Активен", font=("Arial", 10), bg='#1e1e1e', fg='green').pack()
        tk.Button(self.root, text="✖", command=self.root.quit, bg='red', fg='white', bd=0, width=2, height=1, font=("Arial", 8)).place(x=570, y=10)

        self.current_text = ""
        self.target_text = ""
        self.is_typing = False

    def update_text(self, text):
        self.target_text = f"«{text}»"
        self.current_text = ""
        self.is_typing = True
        self.type_char()

    def type_char(self):
        if not self.is_typing:
            return
        if len(self.current_text) < len(self.target_text):
            self.current_text += self.target_text[len(self.current_text)]
            self.text_label.config(text=self.current_text)
            self.root.after(50, self.type_char)
        else:
            self.is_typing = False

    def run(self):
        self.root.mainloop()

# === TELEGRAM БОТ ===
async def start(update, context):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text("🔐 Добро пожаловать.\nЯ — **NEVOROS**.")

async def handle_message(update, context):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if user_id != ADMIN_ID:
        return

    if len(text) > 300:
        text = text[:297] + "..."

    QUEUE.put(text)
    await update.message.reply_text("✅ NEVOROS говорит...")

def run_bot():
    while True:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            app = Application.builder().token(TOKEN).build()
            app.add_handler(CommandHandler("start", start))
            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
            print("✅ Бот запущен")
            loop.run_until_complete(app.run_polling())
        except Exception as e:
            print(f"🔴 Ошибка: {e}")
            time.sleep(3)

# === ВЕБ-СЕРВЕР (Flask) ===
app = Flask(__name__)
messages = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Nevoros Web</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #121212; color: #eee; }
        h1 { color: #00ffcc; }
        input, button { padding: 10px; margin: 10px 0; }
        button { background: #00ffcc; color: black; border: none; cursor: pointer; }
        button:hover { background: #00cccc; }
        .msg { margin: 5px 0; padding: 8px; background: #1e1e1e; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>🤖 Nevoros Web Control</h1>
    <form method="POST">
        <input type="text" name="text" placeholder="Введите текст для озвучки" required style="width: 300px;">
        <button type="submit">Сказать</button>
    </form>
    <div><small>Текст будет озвучен через виртуальный микрофон</small></div>
    <h3>История:</h3>
    {% for msg in messages %}
        <div class="msg">{{ msg }}</div>
    {% endfor %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def web_control():
    if request.method == "POST":
        text = request.form["text"][:300]
        QUEUE.put(text)
        messages.append(f"🗣️ {text}")
        if len(messages) > 50:
            messages.pop(0)
    return render_template_string(HTML_TEMPLATE, messages=messages)

def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

# === ОСНОВНОЙ ЗАПУСК ===
def main():
    print("🚀 Запуск NEVOROS...")

    window = NevorosWindow()
    kb_listener = start_keyboard_listener()
    print("✅ Управление мышью включено")

    # Запуск Telegram-бота
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    print("✅ Бот запущен")

    # Запуск веб-сервера
    web_thread = threading.Thread(target=run_flask, daemon=True)
    web_thread.start()
    print("✅ Веб-сервер запущен: http://localhost:5000")

    # Проверка очереди
    def check_queue():
        try:
            text = QUEUE.get_nowait()
            window.update_text(text)
            threading.Thread(
                target=lambda: (text_to_speech_to_file(text, TEMP_AUDIO), play_audio_as_microphone(TEMP_AUDIO)),
                daemon=True
            ).start()
        except queue.Empty:
            pass
        finally:
            window.root.after(100, check_queue)

    window.root.after(100, check_queue)
    print("🟢 GUI запущен")
    window.run()

if __name__ == "__main__":
    main()
