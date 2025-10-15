import pytest
from source.school import Classroom, TooManyStudents

@pytest.fixture
def setup_classroom():
    teacher = Classroom.Teacher("Mr. Smith")
    students = [Classroom.Student(f"Student{i}") for i in range(3)]
    classroom = Classroom(teacher, students, "Mathematics")
    return classroom


def test_add_student(setup_classroom):
    classroom = setup_classroom
    new_student = Classroom.Student("New Student")
    classroom.add_student(new_student)
    assert new_student in classroom.student  #bhakhar add gareko new_student chai student ko list ma xa ki xaina bhanera herne
    assert len(classroom.student) == 4


def test_add_student_too_many(setup_classroom):
    classroom = setup_classroom
    # fill up to 11 students to trigger exception
    for i in range(8):  # already 3 students
        classroom.add_student(Classroom.Student(f"Extra{i}"))

    with pytest.raises(TooManyStudents):
        classroom.add_student(Classroom.Student("Overflow"))


def test_remove_student(setup_classroom):
    classroom = setup_classroom
    name_to_remove = "Student1"
    classroom.remove_student(name_to_remove)
    remaining_names = [s.name for s in classroom.student]
    assert name_to_remove not in remaining_names


def test_change_teacher(setup_classroom):
    classroom = setup_classroom
    new_teacher = Classroom.Teacher("Mrs. Johnson")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Mrs. Johnson"
