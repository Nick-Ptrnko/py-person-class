class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Додаємо екземпляр до атрибута класу people
        Person.people[self.name] = self
        #people[self.name] = self

def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person, person.age))

people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
person_list = create_person_list(people)