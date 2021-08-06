# DICOM Test Sender

Кросплатформенное десктопное приложение для работы с DICOM-файлами (чтение, просмотр тегов, просмотр изображений), отправкой и получением их по локальной сети.

## Возможности
- чтение dicom файлов с исследованиями из каталога
- просмотр тегов и проверка файлов на валидность
- просмотр изображений/снимков хранящихся в dicom-формате
- отправка файлов на удаленный PACS-сервер (реализация функцию SCU)
- получение файлов по сети (реализация функцию SCP) c последующим сохранением в папку

## Запуск
1. Установить и активировать вирт.окружение Python
```
python -m venv pyside-dicom-sender
pyside-dicom-sender\Scripts\activate
```

2. Установка зависимостей
```
pip install -r requirements.txt
```

3. Запуск приложения
```
python main.py
```

**Установка на Mac с чипом не М1:**
1. Скачать проект с помощью Download
2. Распаковать zip архив
3. Открыть терминал по адресу папки
4. Выполнитьь команды:
```
pip3 install -r requirements.txt
python3 main.py
```
В дальнейшем запуск программы производить в терминале, открытом по адресу папки, в которой установлен проект.

## Работа

1. Редактирование UI
```
pyside-dicom-sender\Scripts\pyside6-designer.exe form.ui
```

2. Компиляция UI
```
pyside-dicom-sender\Scripts\pyside6-uic.exe form.ui > ui_main.py
```

3. Редактирование файла main.py

## Сборка

1. Windows
```
pyside-dicom-sender\Scripts\pyinstaller --windowed --onefile dicom-sender.spec
```
2. MacOS
```
pyinstaller --windowed --onefile --name="dicom-sender-mac" main.py
```
3. Linux

## Дистрибутивы

- Windows - [скачать](https://files.sbermed.ai/s/tESi4tmCERfpmcQ)
- MacOS - 
- Linux - 

## Демонстрация

- [Видео](https://files.sbermed.ai/s/tTH2LQXNt4gCK8p)
- [Видео2 (MacOS)](https://files.sbermed.ai/s/kBAc6WsjwpR75GG)

[![Watch the video](images/screenshot1.png)](https://files.sbermed.ai/s/tTH2LQXNt4gCK8p)

