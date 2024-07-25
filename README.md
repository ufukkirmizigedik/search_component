# Поиск продуктов и инструментов

Этот проект представляет собой программу для поиска продуктов и инструментов по названиям из Excel-файла. Он использует графический интерфейс на базе Tkinter для загрузки файла и выполняет поиск по трем каталогам: Weller, DMC и Harwin.

## Функции

- Загрузка Excel-файла через графический интерфейс.
- Поиск продуктов в каталогах Weller, DMC и Harwin.
- Обновление Excel-файла с добавлением ссылок на продукты.
- Сохранение обновленного файла и автоматическое его открытие.

## Установка

Следуйте этим шагам для установки и запуска проекта на вашем локальном компьютере:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/username/repository-name.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd repository-name
    ```

3. Создайте виртуальную среду и активируйте её:
    ```bash
    python -m venv env
    source env/bin/activate  # Для Windows: env\Scripts\activate
    ```


4. Установите необходимые зависимости:
    ```bash
    pip install pandas openpyxl
    ```

## Использование

1. Запустите приложение:
    ```bash
    python parser.py
    ```

2. Нажмите кнопку "Attach" и выберите ваш Excel-файл для загрузки.

3. Нажмите кнопку "Start" для начала обработки файла. Программа скопирует выбранный файл в целевую папку, выполнит поиск продуктов и обновит ссылки в файле.

4. Обновленный файл будет сохранен под именем `guncellenmis_veri.xlsx` и автоматически откроется.

## Пример структуры проекта


project/
│
├── parser.py # Основной код парсера
├── weller.py # Модуль для поиска продуктов Weller
├── dmc.py # Модуль для поиска продуктов DMC
├── harvin.py # Модуль для поиска продуктов Harwin
└── requirements.txt # Зависимости проекта

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по электронной почте: ufukkirmizigedik1984@gmail.com

