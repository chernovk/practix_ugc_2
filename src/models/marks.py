from pydantic import BaseModel, validator
import uuid
from typing import Optional
from datetime import datetime


class BaseMark(BaseModel):
    film_id: uuid.UUID


class MarkAction(BaseMark):
    mark: int

    @validator('mark', pre=True, always=True)
    def check_mark(cls, v):
        if 0 > v >= 10:
            raise ValueError('Invalid value for mark field')
        return v

class Mark(BaseModel):
    film_id: Optional[uuid.UUID]
    mark: int
    datetime: Optional[datetime]
    user_login: Optional[str]

    @validator('datetime', pre=True, always=True)
    def set_datetime_now(cls, v):
        if not v:
            return datetime.now()
        return v


class AverageFilmRatingResponseModel(BaseModel):
    film_id: uuid.UUID
    average_rating: float


class FilmMarksCountResponseModel(BaseModel):
    film_id: uuid.UUID
    marks_count: int