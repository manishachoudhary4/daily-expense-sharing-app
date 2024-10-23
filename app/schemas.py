from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    email: str
    name: str
    mobile: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    mobile: str
    
    class Config:
        orm_mode = True

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    split_method: str
    participants: List[int]
