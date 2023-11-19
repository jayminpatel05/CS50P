# Learning goals
# class methods -> do NOt need class instantiation
class Student:
    def __init__(self, name, house, patronous='None'):
        if not name:
            raise ValueError("Missing name. Please enter name")

        self.name = name
        self.house = house
        self.patronous = patronous

    def __str__(self):
        return f"Student name: {self.name}, house: {self.house}, patronous: {self.patronous}"

## introduce class method for get student.
# get_student should be abstracted as a part of the class and not a separate function
    @classmethod
    def get(cls):
        name = input("Enter student name: ")
        house = input("Enter student house: ")
        response = input("Does the student have patronous(Y/N) ? ")
        if response == 'N' or response == 'n':
            patro = ""
        else:
            patro = input("Enter Patronous: ")
        # return cls and not the classs name
        return cls(name, house, patro)


def main():
    student = Student.get()
    print(f"Please see below details for {student.name}")
    print(student)

if __name__ == "__main__":
    main()