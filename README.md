# lyceum

**Запуск проекта**

Первый шаг одинаковый, дальше разные для OC Windows/Linux <br><br>
1 Клонируем себе репозиторий: <br>
```git clone https://github.com/mge410/lyceum.git ```<br>
и переходим в папку с проектом <br>
```cd lyceum ```<br>
В репозитории с проектом создаём файл .env и в нём прописываем SECRET_KEY=ВАШ_СЕКРЕТНЫЙ_КЛЮЧ <br>

Windows: <br>
2 Заводим виртуальное окружение и активируем его: <br>
```python -m venv venv ```<br>
```.\venv\Scripts\activate ```<br>

3 Обновляем pip и качаем туда все что есть в requirements.txt: <br>
```python -m pip install --upgrade pip``` <br>
```pip install -r requirements.txt ```<br>

4 Запускаем проект: <br>
``` python .\lyceum\manage.py runserver ```<br>

Linux: <br>

2 Заводим виртуальное окружение и активируем его: <br>
```python3 -m venv venv ```<br>
```source venv/bin/activate ```<br>

3 Обновляем pip и качаем туда все что есть в requirements.txt: <br>
```pip install -U pip или python3 -m pip install --upgrade pip```<br>
```pip install -r requirements.txt``` <br>

4 Запускаем проект: <br> 
```python3 lyceum/manage.py runserver```<br>


**Настройка проекта**
Проект изначально запускается в DEBUG режиме, после это можно изменить в настройка __/lyceum/.env__
В репозитории уже есть пример файла с настройками проекта __example_config.env__
И мы можем скопировать это файл с названием .env внутри проекта в папку lyceum <br>
__Для Windows__ <br>
```cp example_config.env .\lyceum\.env``` <br>
__Для linux__ <br>
```cp -r example_config.env /lyceum/.env``` <br>
После чего его можно настроить под себя <br>
Например прописать DEBAG=False

***Разработка проекта***

Тут зависимости которые использовались для локальной разработки проекта, для запуска проекта они не требуются <br>
Устанавливаем зависимости для разработки проекта: <br>
``` pip install -r requirements_dev.txt```

***Тестирование***

Тут зависимости которые использовались для тестирования проета CI/CD <br>
Устанавливаем зависимости для тестирования проекта: <br>
``` pip install -r requirements_test.txt```