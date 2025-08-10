from Typing import TypedDict

class person(TypedDict):
    name:str
    age:int
    
new_Id=person({'name':'Alice', 'age':30 })

print(new_Id)