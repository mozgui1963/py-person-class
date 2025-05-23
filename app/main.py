class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people_data: list) -> list:

    people_instances = []

    for person in people_data:
        instance = Person(person["name"], person["age"])
        people_instances.append(instance)

    for person in people_data:
        instance = Person.people[person["name"]]
        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person.get(spouse_key)

        if spouse_name:
            setattr(instance, spouse_key, Person.people.get(spouse_name))

    return people_instances

