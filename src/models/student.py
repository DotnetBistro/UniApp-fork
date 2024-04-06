from __future__ import annotations
from typing import List

from models.subject import Subject


class Student:
    id: str
    name: str
    email: str
    password: str
    enrolment: List[Subject]

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name, self.email, self.password = name, email, password
        self.enrolment = []

    def __str__(self) -> str:
        return f"Id: {self.id} - Name {self.name} - Email {self.email} - Fully Enrol: {self.is_fully_enrol()}"

    @staticmethod
    def create_student(name: str, email: str, password: str) -> Student:
        return Student(name, email, password)

    def is_fully_enrol(self) -> bool:
        return self.__is_exceeded_enrolment()

    def enrol_subject(self, subject: Subject):
        if self.__is_exceeded_enrolment():
            self.enrolment.append(subject)

    def delete_subject(self, subjectId: int):
        self.enrolment

    def __is_exceeded_enrolment(self) -> bool:
        return len(self.enrolment) >= 4
