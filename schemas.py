from pydantic import BaseModel, EmailStr


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "Medium"
    status: str = "Pending"


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: str | None = None
    status: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    priority: str
    status: str

    class Config:
        from_attributes = True
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True        