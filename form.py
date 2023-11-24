from flask import Blueprint, request
from datetime import datetime
from markupsafe import escape

form = Blueprint('form', __name__)


@form.route("/name/<path:name>")
def hello(name):
    return f"Hello, {name}!"


@form.route("/name2/<path:name>")
def hello2(name):
    return f"Hello, {escape(name)}!"


@form.route('/get_time')
def get_time():
    dt = datetime.now()
    return {"dt": dt}


@form.route('/fetch')
def fetch():
    return '''
    <style>
        button {
            font-size: 40px;
        }
        body {
            font-size: 40px;
            text-align: center;
        }
    </style>
    <script>
        function start() {
            fetch('/get_time')
                .then(resp => {
                    return resp.json();
                })
                .then(data => {
                    document.querySelector('div').innerHTML = data.dt;
                })
        }
    </script>

    <button onclick="start()">Получить время сервера с помощью fetch()</button>
    <div></div>
    '''


@form.route("/form/")
def form_menu():
    return '''
        <ol>
            <li><a href="/form/get">GET</a></li>
            <li><a href="/form/post/urlencoded">POST: application/x-www-form-urlencoded</a></li>
            <li><a href="/form/post/form-data">POST: multipart/form-data</a></li>
        </ol>
'''


@form.route('/f')
def f():
    return 'success'


@form.route("/form/get")
def form_get():
    if not request.args.get('request'):
        return '''
            <title>form/get</title>
            <body style="font-size: 20px">
            <div style="font-family: monospace">
                &lt;form method="get"&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="hidden" value="yes" name="request"&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="text" value="alex" name="user"&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="text" value="13" name="age"&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="text" value="green" name="color"&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;button type="submit"&gt;submit&lt;/button&gt;<br>
                &lt;/form&gt;
            </div>

            <form method=get>
                <input type=hidden value=yes name=request><br>
                <input type=text value=alex name=user><br>
                <input type=text value=13 name=age><br>
                <input type=text value=green name=color><br>
                <button type=submit>submit</button>
            </form>
            <div style="margin-top: 30px;">
                <a href="/form" style="color: gray; font-size: 20px;">menu</a>
            </div>
            </body>
            '''
    rqst = request.args.get('request')
    user = request.args.get('user')
    age = request.args.get('age')
    color = request.args.get('color')
    return '''
            <title>form/get</title>
            <body style="font-size: 20px">
            <h1>Получены данные:</h1>
            <div>
                request: "{}"<br>
                name: "{}"<br>
                age: "{}"<br>
                color: "{}"<br>
            </div>
            <div>
                <a href="javascript:history.back()">Назад</button>
            </div>
            <div style="margin-top: 30px;">
                <a href="/form" style="color: gray; font-size: 20px;">menu</a>
            </div>
            </body>
        '''.format(rqst, user, age, color)


@form.route("/form/post/<type>", methods=['post', 'get'])
def form_post(type):
    enctype = 'application/x-www-form-urlencoded' if type == 'urlencoded' else 'multipart/form-data'

    if request.method == 'GET':
        return '''
            <title>form/post: {enctype}</title>
            <body style="font-size: 20px">
                <div style="font-family: monospace">
                    &lt;form method="post" enctype="{enctype}"&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="hidden" value="yes" name="request"&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="text" value="alex" name="user"&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="text" value="13" name="age"&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type="text" value="green" name="color"&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&lt;button type="submit"&gt;submit&lt;/button&gt;<br>
                    &lt;/form&gt;
                </div>
                <br><br>
                <form method=post enctype="{enctype}">
                    <input type=text value=alex name=user><br>
                    <input type=text value=13 name=age><br>
                    <input type=text value=green name=color><br>
                    <input type=file name=image><br>
                    <button type=submit>submit</button>
                </form>
                <div style="margin-top: 30px;">
                    <a href="/form" style="color: gray; font-size: 20px;">menu</a>
                </div>
            </body>
        '''.format(enctype=enctype)

    user = request.form.get('user')
    age = request.form.get('age')
    color = request.form.get('color')
    image = request.files.get('image') and '"{}"'.format(request.files.get('image').filename) or '<i>файл не выбран</i>'
    return '''
            <title>form/post</title>
            <body style="font-size: 20px">
            <h1>Получены данные:</h1>
            <div>
                name: "{}"<br>
                age: "{}"<br>
                color: "{}"<br>
                image: {}
            </div>
            <div>
                <a href="javascript:history.back()">Назад</button>
            </div>
            <div style="margin-top: 30px;">
                <a href="/form" style="color: gray; font-size: 20px;">menu</a>
            </div>
            </body>
        '''.format(user, age, color, image)
