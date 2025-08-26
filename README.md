# neveros-ai
NEVOROS is a multi-functional desktop application built with Python that combines mouse control, text-to-speech (TTS), and integration with a Telegram bot and a web interface. Created to boost productivity and convenience, NEVOROS lets you control your computer with voice commands sent through Telegram or a web panel.

# ✨ KEY FEATURES
🗣️ TEXT-TO-SPEECH (TTS): Converts any text into speech and plays it through a virtual audio cable, allowing you to use it as a voice assistant in streaming apps or games.

▶️ KEYBOARD MOUSE CONTROL: Move your mouse cursor using the arrow keys. Perfect for precise adjustments or when a mouse is not available.

💬 TELEGRAM BOT INTEGRATION: Send text commands to your Telegram bot, and NEVOROS will instantly speak them aloud.

🌐 BUILT-IN WEB SERVER: Control the application through a user-friendly local web interface, accessible at http://localhost:5000.

🖼️ ELEGANT GUI: A minimalist and stylish graphical interface with a "typing text" animation and a status indicator.

# 🚀 INSTALLATION
To run NEVOROS, you'll need Python 3.8+ and a few libraries.

CLONE THE REPOSITORY:

Bash

git clone https://github.com/yourusername/nevoros.git
cd nevoros
INSTALL LIBRARIES:

Bash

pip install -r requirements.txt
# ⚙️ SETUP:
Create a Telegram bot with BotFather to get your TOKEN.

Find your Telegram ADMIN_ID.

Replace TOKEN and ADMIN_ID in the main.py file.

Install a program like VB-CABLE Virtual Audio Device to play audio through a virtual microphone.

# 🕹️ USAGE
LAUNCH
Run the application from the command line:

Bash

python main.py
MODES OF OPERATION

GUI: A small window will appear, showing the status and the text being spoken.

TELEGRAM: Send messages to your bot. Any text will be spoken.

WEB PANEL: Open http://localhost:5000 in your browser to enter text for TTS.

MOUSE CONTROL: Use the arrow keys ↑, ↓, ←, → to move the mouse cursor.

SHUTDOWN
Press the Esc key at any time to exit the application.

# 🛠️ TECHNOLOGIES
Python

tkinter — Graphical User Interface

pyttsx3 — Text-to-Speech

sounddevice & scipy — Audio Playback

pynput — Mouse and Keyboard Control

python-telegram-bot — Telegram API Integration

Flask — Local Web Server

# 🙏 ACKNOWLEDGMENTS
Thanks for using NEVOROS! I welcome your suggestions and contributions to the project.

# NEVOROS — это многофункциональное десктопное приложение на Python, которое объединяет управление мышью, преобразование текста в речь (TTS) и интеграцию с Telegram-ботом и веб-интерфейсом. Созданный для повышения производительности и удобства, NEVOROS позволяет вам управлять своим компьютером с помощью голосовых команд, вводимых через Telegram или веб-панель.

# ✨ КЛЮЧЕВЫЕ ОСОБЕННОСТИ
🗣️ ТЕКСТ-В-РЕЧЬ (TTS): Превращает любой текст в речь и воспроизводит его через виртуальный аудиокабель, что позволяет использовать его в качестве голосового ассистента в стриминговых приложениях или играх.

▶️ УПРАВЛЕНИЕ МЫШЬЮ С КЛАВИАТУРЫ: Перемещайте курсор мыши с помощью клавиш-стрелок. Идеально подходит для точных настроек или в случаях, когда мышь недоступна.

💬 ИНТЕГРАЦИЯ С TELEGRAM-БОТОМ: Отправляйте текстовые команды в свой Telegram-бот, и NEVOROS мгновенно озвучит их.

🌐 ВСТРОЕННЫЙ ВЕБ-СЕРВЕР: Управляйте приложением через удобный локальный веб-интерфейс, доступный по адресу http://localhost:5000.

🖼️ ЭЛЕГАНТНЫЙ GUI: Минималистичный и стильный графический интерфейс с анимацией "печатающегося текста" и индикатором статуса.

# 🚀 УСТАНОВКА
Чтобы запустить NEVOROS, вам понадобится Python 3.8+ и несколько библиотек.

КЛОНИРУЙТЕ РЕПОЗИТОРИЙ:

Bash

git clone https://github.com/yourusername/nevoros.git
cd nevoros
УСТАНОВИТЕ БИБЛИОТЕКИ:

Bash

pip install -r requirements.txt

# НАСТРОЙКА:

Создайте Telegram-бота через BotFather и получите TOKEN.

Найдите свой Telegram ADMIN_ID.

Замените TOKEN и ADMIN_ID в файле main.py.

Установите программу VB-CABLE Virtual Audio Device или аналог, чтобы воспроизводить звук в виртуальный микрофон.

# 🕹️ ИСПОЛЬЗОВАНИЕ
ЗАПУСК
Запустите приложение из командной строки:

Bash

python main.py
РЕЖИМЫ РАБОТЫ
GUI: Запустится небольшое окно, которое отображает статус и текст озвучки.

TELEGRAM: Отправляйте сообщения своему боту. Любой текст будет озвучен.

ВЕБ-ПАНЕЛЬ: Откройте http://localhost:5000 в браузере, чтобы ввести текст для озвучки.

УПРАВЛЕНИЕ МЫШЬЮ: Используйте клавиши-стрелки ↑, ↓, ←, → для перемещения курсора мыши.

ОСТАНОВКА
Нажмите клавишу Esc в любое время, чтобы завершить работу приложения.

# 🛠️ ТЕХНОЛОГИИ
Python

tkinter — Графический интерфейс

pyttsx3 — Преобразование текста в речь

sounddevice & scipy — Воспроизведение аудио

pynput — Управление мышью и клавиатурой

python-telegram-bot — Интеграция с Telegram API

Flask — Локальный веб-сервер

🙏 БЛАГОДАРНОСТЬ
Спасибо, что используете NEVOROS! Буду рад вашим предложениям и вкладу в развитие проекта.
