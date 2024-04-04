import random
import re
from typing import List, Tuple

from ..persistent import db
from ..models.student import Student
from ..models.subject import Subject
from ..views import student_view as studentv


class StudentController:
    EMAIL_PATTERN = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
    PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

    def __init__(self) -> None:
        self.view, self.db = (
            studentv.StudentView(),
            db.Database(),
        )

    def login(self) -> Tuple[Student | None, str]:
        (username, password) = self.view.login()

        if not self.__is_valid_login_session(username, password):
            return (None, "Invalid Username or Password, please try again")

        selected_student = [
            student
            for student in self.db.context
            if student.email.lower() == username.lower()
            and student.password.lower() == password.lower()
        ]

        if not selected_student:
            return (None, "Invalid Username or Password, please try again")

        return (selected_student[0], "")

    def register(self):
        (username, password) = self.view.register()

        if self.__is_exited_user(username):
            return (False, "user already exist")
        elif self.__is_valid_login_session(username, password):
            return (True, "")
        else:
            return (False, "Invalid Username or Password, please try again")

    def change_password(self, ctx: Student):
        pass

    def enrol_subject(self, ctx: Student):

        new_subject: Subject = Subject.create_subject(
            1, "Subject 1", random.randint(45, 100)
        )
        students = [st for st in self.db.context if st.id == ctx.id]

        if not students:
            raise Exception()

        entity: Student = students[0]
        entity.enrol_subject(new_subject)

        self.db.save()

    def view_enrolment(self, ctx: Student):
        pass

    def get_subject_info(self, ctx: Student):
        pass

    def remove_subject(self, ctx: Student):
        pass

    def __is_valid_login_session(self, email, password):
        return self.__validate_email(email) and self.__validate_password(password)

    def __validate_password(self, password: str):
        return re.match(self.PASSWORD_PATTERN, password)

    def __validate_email(self, email: str):
        return re.match(self.EMAIL_PATTERN, email)

    def __is_exited_user(self, username: str) -> bool:
        students: List[Student] = self.db.read()

        return [
            student for student in students if student.email.lower() == username.lower()
        ][0] is not None

    def __is_registed_user(self, username: str, password: str) -> List[Student]:
        students: List[Student] = self.db.read()

        return [
            student
            for student in students
            if student.email.lower() == username.lower()
            and student.password.lower() == password.lower()
        ]
