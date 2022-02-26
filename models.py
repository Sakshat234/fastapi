from typing import Optional, List #typing means what the code accepts as a request. eg in roles it only accepts requests in List
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional
from uuid import UUID,uuid4
from enum import Enum

class Role(str,Enum):
    admin="admin"
    user="user"
    student="student"
class Gender(str,Enum):
    male="male"
    female="female"

class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str
    middle_name:Optional[str]
    roles:List[Role]
    gender:Gender
class UserUpdateRequest(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    middle_name:Optional[str]
    roles:Optional[List[Role]]
    gender:Optional[Gender]