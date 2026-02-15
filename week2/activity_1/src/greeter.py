'''Considering reuse (modularisation)
when creating python programs'''
# create a calculator class and re-use this by instantiating it in the main.py

# So as not to contaminate your global namespace, it is good practice to use a main function.

# so that we can reuse our code as both a module and
# we can use an if statement to ensure that some code is only executed when name is __main__

# module name when imported


def greet(name):
    print(f"Hello, {name}")

def main():
    greet('John')

if __name__ == '__main__':
    main()