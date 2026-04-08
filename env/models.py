from pydantic import BaseModel
from typing import List

class Email(BaseModel):
    id: int
    subject: str
    body: str

class Observation(BaseModel):
    emails: List[Email]
    message: str

class Action(BaseModel):
    email_id: int
    label: str

class Reward(BaseModel):
    score: float