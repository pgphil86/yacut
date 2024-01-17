# 'Yacut' created by Pavel.
```
https://github.com/pgphil86
```
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
### Languages:
### I. [Русский язык.](https://github.com/pgphil86/yacut?tab=readme-ov-file#i-проект-yacut)
### II. [English language.](https://github.com/pgphil86/yacut?tab=readme-ov-file#-i-the-yakut-project)
## I. Проект 'Yacut'.

### Описание проекта.
'Yacut' - это сервис, который укорачивает ссылки. 
### Работа с проектом.
Для начала необходимо клонировать репозиторий и зайти в рабочую директорию проекта.
```
git@github.com:pgphil86/yacut.git
```
```
cd yacut
```
Далее создаем и активируем виртуальное окружение.
```
python3 -m venv venv
```
```
source venv/bin/activate
```
После устанавливаем зависимости из requirements.txt.
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
В корневой директории проекта создаем файл .env с переменными:
```
FLASK_APP=yacut
```
Для режима отладки:
```
FLASK_ENV=development
```
Для режима готового продукта:
```
FLASK_ENV=production
```
```
DATABASE_URI=sqlite:///db.sqlite3
```
```
SECRET_KEY=<Секретный ключ>
```
Далее создаём миграции:
```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```
Проект можно запускать:
```
flask run
```
[Вверх.](https://github.com/pgphil86/yacut?tab=readme-ov-file#yacut-created-by-pavel)

## ## I. The Yacut project.

### Description of the project.
Yacut is a service that shortens links. 
### Working with the project.
First, you need to clone the repository and go to the working directory of the project.
```
git@github.com:pgphil86/yacut.git
```
```
cd yacut
```
Next, we create and activate a virtual environment.
```
python 3 -m ven ven
```
```
source venv/bin/activate
```
After that, we install the dependencies from requirements.txt .
```
python3 -m pip install --upgrade php
```
```
pip install -r requirements.txt
```
Create a file in the root directory of the project.env with variables:
```
FLASK_APP=yacut
```
For debugging mode:
```
FLASK_ENV=development
```
For the finished product mode:
```
FLASK_ENV=production
```
```
DATABASE_URI=sqlite:///db.sqlite3
```
```
SECRET_KEY=<Secret key>
```
Next, we create migrations:
```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```
The project can be launched:
```
flask run
```
[Up.](https://github.com/pgphil86/yacut?tab=readme-ov-file#yacut-created-by-pavel)
