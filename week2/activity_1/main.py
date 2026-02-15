from src.greeter import greet
from src.student import Student

def main():
    greet('John')
    student1 = Student("Sera", '1234567', ["IPOS", "Ethics", "Mobile Dev"], "1 Street st, somewhere")
    
    greet(student1.name)


if __name__ == '__main__':
    main()


# print(greet)
# use an alias - consider why might we do this?
    
    # def mergeUnits(self ,newUnits, oldUnits):

# sometimes we only want to import what we need

# create a calculator class in the module

# use the new class to return a score to a user


