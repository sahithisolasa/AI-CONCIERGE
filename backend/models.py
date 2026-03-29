from pydantic import BaseModel

class UserProfile(BaseModel):
    age: int
    income: int
    expense: int
    goal: str
    risk: str