from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


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
