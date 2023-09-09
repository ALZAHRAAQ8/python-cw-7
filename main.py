class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"my name is {self.name}, and iam {self.age} years old"
    
    def is_adult(person):
        if first_person.age > 18:
            print("You have too much responsibilities")

        elif first_person.age < 18:
            print("lucky you")


first_person = Person("alzahraa", 17)
print(first_person.name , first_person.age)

print(first_person)