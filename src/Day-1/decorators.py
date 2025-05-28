
def mydeco(func):
    def wrapper(*args):
        print("Before function")
        func(*args)
        print("After Function")
    return wrapper

@mydeco
def hello(var):
    print(f"Hello {var} !!!")

@mydeco
def twohello(var,var2):
    print(f"Hello {var} and {var2} !!!")

hello("Abhishek")
twohello("Abhishek","Chhawari")