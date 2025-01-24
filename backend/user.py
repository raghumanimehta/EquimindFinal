from datetime import datetime, date
from enum import Enum
from typing import Optional

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"
    TRANSGENDER = "TRANSGENDER"
    GENDERQUEER = "GENDERQUEER"
    GENDER_FLUID = "GENDER_FLUID"
    AGENDER = "AGENDER"
    OTHER = "OTHER"
    PREFER_NOT_TO_SAY = "PREFER_NOT_TO_SAY"

class User:
    def __init__(
        self,
        id: int,
        email: str,
        name: str,
        gender: Gender,
        birth_date: date,
        password: str,
        current_streak: int = 0,
        last_mood_entry: Optional[datetime] = None
    ):
        self._id = id
        self._email = email
        self._name = name
        self._gender = gender
        self._birth_date = birth_date
        self._password = password
        self._current_streak = current_streak
        self._last_mood_entry = last_mood_entry

    @property
    def id(self) -> int:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, value: Gender):
        self._gender = value

    @property
    def birth_date(self) -> date:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        self._birth_date = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value

    @property
    def current_streak(self) -> int:
        return self._current_streak

    @current_streak.setter
    def current_streak(self, value: int):
        self._current_streak = value

    @property
    def last_mood_entry(self) -> Optional[datetime]:
        return self._last_mood_entry

    @last_mood_entry.setter
    def last_mood_entry(self, value: Optional[datetime]):
        self._last_mood_entry = value
