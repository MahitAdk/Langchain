from pydantic import BaseModel,EmailStr,Field

class Student(BaseModel):
    name:str
    #name:str='Mahit' Giving default value to the system
    age:int
    email:EmailStr#Checks for valid email format
    CGPA:float=Field(gt=0,lt=10)#Checks for valid GPA between 0 and 10
    
new_student={'name':'Mahi','age':20}

student=Student(**new_studen)