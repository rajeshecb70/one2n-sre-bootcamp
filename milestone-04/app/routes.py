from flask import Blueprint, request
from .models import Student
from .schemas import StudentSchema
from . import db

bp = Blueprint('students', __name__, url_prefix='/api/v1/students')


@bp.route('', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_student)
    db.session.commit()
    return StudentSchema().jsonify(new_student), 201


@bp.route('', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return StudentSchema(many=True).jsonify(students)


@bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return StudentSchema().jsonify(student)


@bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json
    student.name = data['name']
    student.age = data['age']
    student.gender = data['gender']
    db.session.commit()
    return StudentSchema().jsonify(student)


@bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204


def init_app(app):
    app.register_blueprint(bp)
