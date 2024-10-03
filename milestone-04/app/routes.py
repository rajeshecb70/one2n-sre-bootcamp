from flask import Blueprint, request, jsonify
from .models import Student
from . import db

bp = Blueprint("students", __name__, url_prefix="/api/v1/students")


@bp.route("", methods=["POST"])
def add_student():
    data = request.json
    new_student = Student(**data)  # Unpacking the dictionary into Student model
    db.session.add(new_student)
    db.session.commit()
    return jsonify(
        {
            "id": new_student.id,
            "name": new_student.name,
            "age": new_student.age,
            "gender": new_student.gender,
        }
    ), 201


@bp.route("", methods=["GET"])
def get_all_students():
    students = Student.query.all()
    return jsonify(
        [
            {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "gender": student.gender,
            }
            for student in students
        ]
    )


@bp.route("/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(
        {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
        }
    )


@bp.route("/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json
    student.name = data["name"]
    student.age = data["age"]
    student.gender = data["gender"]
    db.session.commit()
    return jsonify(
        {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
        }
    )


@bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return "", 204


def init_app(app):
    app.register_blueprint(bp)
