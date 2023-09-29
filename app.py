from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
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
                <a href="/lab2/example">/lab2/example</a>
            </li>
        </ol>

        <footer>
            &copy; Иван Иванов, ФБИ-00, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
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

@app.route('/lab1/oak')
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

@app.route("/lab1/student")
def student():
    return "Иванов Иван"

@app.route("/lab1/python")
def student():
    return "python"

@app.route("/lab1/abc")
def student():
    return "abc"

@app.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Иван Иванов', 2, 'ФБИ-00', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html',
                            name=name, lab_num=lab_num, group=group,
                            course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')



# @app.route('/base')
# def base():
#     name = 'Иван Иванов'
#     lab_num = 2
#     fruits = [
#         {'name': "яблоки", 'price': 100},
#         {'name': "груши", 'price': 120},
#         {'name': "апельсины", 'price': 80},
#         {'name': "мандарины", 'price': 95},
#         {'name': "манго", 'price': 321}
#     ]
#     return render_template('base.html', name = name, lab_num = lab_num, fruits=fruits)
