from flask import Blueprint, render_template, request, abort

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html', courses = courses)


courses = [
    {"name": "c++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "c#", "videos": 8}    # если цена не указана, то курс бесплатный
]


@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return courses


@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if 0 <= course_num < len(courses):
        print(f'return courses[{course_num}] = {courses[course_num]}')
        return courses[course_num]

    print('not found - 404')
    abort(404)


@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    courses.append(course)
    return len(courses)-1


@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    course = request.get_json()
    if 0 <= course_num < len(courses):
        print(f'put courses[{course_num}] = {course}')
        courses[course_num] = course
        return courses[course_num]

    print('not found - 404')
    abort(404)


@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if 0 <= course_num < len(courses):
        print(f'delete courses[{course_num}] = {courses[course_num]}')
        del courses[course_num]
        return '', 204

    print('not found - 404')
    abort(404)
