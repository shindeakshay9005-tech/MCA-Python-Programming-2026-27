# Package initializer: exposes selected functions from the package modules.
from .details import get_student_details
from .results import calculate_grade

__all__ = ["get_student_details", "calculate_grade"]
