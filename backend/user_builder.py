from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional
from user import User, Gender

class UserBuilder:
   def __init__(self):
       self._email = None
       self._name = None
       self._gender = None
       self._birth_date = None
       self._password = None
       self._current_streak = 0
       self._last_mood_entry = None
       
   def email(self, email: str) -> 'UserBuilder':
       self._email = email
       return self

   def name(self, name: str) -> 'UserBuilder':
       self._name = name
       return self

   def gender(self, gender: Gender) -> 'UserBuilder':
       self._gender = gender
       return self

   def birth_date(self, birth_date: date) -> 'UserBuilder':
       self._birth_date = birth_date
       return self

   def password(self, password: str) -> 'UserBuilder':
       self._password = password
       return self

   def build(self) -> User:
       if not all([self._email, self._name, self._gender, self._birth_date, self._password]):
           raise ValueError("All required fields must be set")
       return User(
            id=None,
            email=self._email,
            name=self._name,
            gender=self._gender,
            birth_date=self._birth_date,
            password=self._password,
            current_streak=self._current_streak,
            last_mood_entry=self._last_mood_entry
        )
   
   