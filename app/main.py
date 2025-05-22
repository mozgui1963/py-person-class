class Person:
    people = {}


    def __init___(self, name: str, age: int):
        self.name = __name__
        self.age = age
        self.wife = None
        self.husband =  None
        Person.people[name] = self

def create_person_list(people_data: list) -> list:

    people_instances = [Person(person["name"], person["age"]) for person in people_data]

    for person in people_data:
        instance = Person.people[person["name"]]
        spouse_key = "wife" if "wife" in person else "husband"

        if person[spouse_key]:
            spouse_instance = Person.people[person[spouse_key]]
            setattr(instance, spouse_key, spouse_instance)

    return people_instances
