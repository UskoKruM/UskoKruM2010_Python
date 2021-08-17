import json

"""
json_str = '{"nombre":"Oscar","edad":28,"pais":"Perú"}'
print(json_str)
print(type(json_str))

python_dict = json.loads(json_str)
print(python_dict)
print(type(python_dict))
print(python_dict['edad'])
print(python_dict['pais'])
"""

"""
data = {
    "youtuber": "UskoKruM2010",
    "nombre": "Oscar",
    "edad": 28,
    "cursos": ["PHP", "Python", "JavaScript", "C#", "Node.js"]
}
json_data = json.dumps(data)
print(json_data)
print(type(json_data))
"""

"""
Python	|   JSON
dict	=>  Object
list	=>  Array
tuple	=>  Array
str	    =>  String
int	    =>  Number
float	=>  Number
True	=>  true
False	=>  false
None	=>  null
"""

"""
data = {
    "youtuber": "UskoKruM2010",
    "nombre": "Oscar",
    "edad": 28,
    "cursos": ["PHP", "Python", "JavaScript", "C#", "Node.js"]
}

# json_data = json.dumps(data, indent=4, separators=(", ", " : "))
json_data = json.dumps(data, indent=4, separators=(", ", " : "), sort_keys=True)
print(json_data)
"""

"""
json_data = json.JSONEncoder().encode({"lenguajes": ["Python", "JavaScript"]})
print(json_data)
print(type(json_data))

python_dict = json.JSONDecoder().decode(json_data)
print(python_dict)
print(type(python_dict))
"""


class Curso():

    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos


curso_1 = Curso("9841", "Lenguaje", 4)
print(curso_1)
json_object_data = json.dumps(curso_1.__dict__)
print(json_object_data)
print(type(json_object_data))
python_dict = json.loads(json_object_data)
print(python_dict)
print(type(python_dict))
