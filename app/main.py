class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Додаємо екземпляр до атрибута класу people
        Person.people[self.name] = self


def create_person_list(people_dicts: list) -> list:
    # ЕТАП 1: Створення всіх об'єктів та наповнення Person.people
    person_list = []
    for person_dict in people_dicts:
        person_list.append(
            Person(person_dict["name"], person_dict["age"])
        )

    # ЕТАП 2: Встановлення зв'язків
    for person_dict in people_dicts:

        # Отримуємо об'єкт (екземпляр Person) для модифікації
        current_person_object = Person.people[person_dict["name"]]

        # Перевіряємо, чи є партнер
        if person_dict.get("wife") is not None:
            wife_name = person_dict["wife"]
            # Встановлюємо атрибут 'wife', посилаючись на об'єкт із реєстру
            current_person_object.wife = Person.people[wife_name]

        elif person_dict.get("husband") is not None:
            husband_name = person_dict["husband"]
            # Встановлюємо атрибут 'husband', посилаючись на об'єкт із реєстру
            current_person_object.husband = Person.people[husband_name]

    return person_list
