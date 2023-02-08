# lyceum

![Bitbucket Pipelines:](https://img.shields.io/bitbucket/pipelines/mge410/lyceum/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


***Запуск проекта***

Первый шаг одинаковый, дальше резные для OC Windows/Linux </br></br>
1 Клонируем себе репозиторий: </br>
Вводим: git clone https://github.com/mge410/lyceum.git и переходим в папку с проектом </br>
Вводим: cd lyceum </br>
В репозитории с проектом создаём файл .env и в нём прописываем SECRET_KEY=ВАШ_СЕКРЕТНЫЙ_КЛЮЧ </br>

Windows: </br>
2 Заводим виртуальное окружение и активируем его: </br>
Вводим: python -m venv venv </br>
Затем: .\venv\Scripts\activate </br>

3 Обновляем pip и качаем туда все что есть в requirements.txt: </br>
Вводим: python -m pip install --upgrade pip </br>
Затем: pip install -r requirements.txt </br>

4 Запускаем проект: </br>
Вводим: python .\lyceum\manage.py runserver </br>

Linux: </br>

2 Заводим виртуальное окружение и активируем его: </br>
Вводим: python3 -m venv venv </br>
Затем: source venv/bin/activate </br>

3 Обновляем pip и качаем туда все что есть в requirements.txt: </br>
Вводим: pip install -U pip или python3 -m pip install --upgrade pip </br>
Затем: pip install -r requirements.txt </br>

4 Запускаем проект: </br> 
Вводим: python3 lyceum/manage.py runserver </br>

***Разработка проекта***

Устанавливаем зависимости для разработки проекта
Вводим: pip install -r requirements_dev.txt

***Тестирование проекта***

Устанавливаем зависимости для разработки проекта
Вводим: pip install -r requirements_test.txt