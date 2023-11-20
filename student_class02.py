# Learning goals
# >> use python decorators in classes to prevent mutation
# >> getter setter property within classes.


class Student:
    def __init__(self, name, house, patronous='None'):
        if not name:
            raise ValueError("Missing name. Please enter name")

        self.name = name
        self.house = house
        self.patronous = patronous

    def __str__(self):
        return f"Student name: {self.name}, house: {self.house}, patronous: {self.patronous}"

    def charm(self):
        if self.patronous == "Stag":
            return "Horse"
        elif self.patronous == "Otter":
            return "Seal"
        elif self.patronous == "Terrier":
            return "Dog"
        else:
            return "Charm not assigned"
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print()
    print(f"Please see below details for {student.name}")
    print(student)
    print("Charm assigned to your student: " + student.charm())


def get_student():
   name = input("Enter student name: ")
   house = input("Enter student house: ")
   response = input("Does the student have patronous(Y/N) ? ")
   if response == 'N' or response == 'n':
       patro = ""
   else:
       patro = input("Enter Patronous: ")
   return Student(name,house,patro)

if __name__ == "__main__":
    main()