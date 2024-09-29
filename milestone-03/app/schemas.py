from . import ma
from .models import Student

class StudentSchema(ma.SQLAlchemyAutoSchema):
    """Schema for the Student model."""

    class Meta:
        model = Student
        load_instance = True
