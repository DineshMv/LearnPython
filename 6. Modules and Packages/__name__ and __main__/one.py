# One.py
# When a script file is called, all the code at indentation level 0 gets executed
# __name__ is a built-in variable in python
# when a py script is called (python one.py), python automatically assign __name__ = "__main__"

def my_func():
    print("func in one.py")


print("Top Level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly!")
else:
    print("one.py has been imported")
