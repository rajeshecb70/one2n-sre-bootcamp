from flask import Blueprint, request
from .models import Student
from .schemas import StudentSchema
from . import db

bp = Blueprint('students', __name__, url_prefix='/api/v1/students')


@bp.route('', methods=['POST'])
def add_student():
    """Add a new student to the database."""
    data = request.json
    new_student = Student(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_student)
    db.session.commit()
    return StudentSchema().jsonify(new_student), 201


@bp.route('', methods=['GET'])
def get_all_students():
    """Retrieve all students from the database."""
    students = Student.query.all()
    return StudentSchema(many=True).jsonify(students)


@bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student by ID."""
    student = Student.query.get_or_404(student_id)
    return StudentSchema().jsonify(student)


@bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update a student's information."""
    student = Student.query.get_or_404(student_id)
    data = request.json
    student.name = data['name']
    student.age = data['age']
    student.gender = data['gender']
    db.session.commit()
    return StudentSchema().jsonify(student)


@bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student by ID."""
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return '', 204


def init_app(app):
    """Initialize the routes for the application."""
    app.register_blueprint(bp)
