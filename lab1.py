from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <ol>
            <li>
                <a href="/lab1">Лабораторная работа 1</a>
            </li>
            <li>
                <a href="/lab2">/lab2</a>
            </li>
        </ol>

        <footer>
            &copy; Иван Иванов, ФБИ-00, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1/")
def lab():
    return """
<!doctype html>
<html>
    <head>
        <title>Иванов Иван Иванович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <div>
            Flask — фреймворк для создания веб-приложений на языке программирования
            Python, использующий набор инструментов Werkzeug, а также шаблонизатор
            Jinja2. Относится к категории так называемых микрофреймворков —
            минималистичных каркасов веб-приложений, сознательно предоставляющих лишьсамые базовые возможности.
        </div>

        <a href="/menu">меню</a>

        <h2>Реализованные роуты</h2>

        <ul>
            <li><a href="/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="/lab1/student">/lab1/student - студент</a></li>
            <li><a href="/lab1/python">/lab1/python - python</a></li>
        </ul>

        <footer>
            &copy; Иван Иванов, ФБИ-00, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@lab1.route("/lab1/student")
def student():
    return "Иванов Иван"


@lab1.route("/lab1/python")
def python():
    return "python"


@lab1.route("/lab1/abc")
def abc():
    return "abc"
