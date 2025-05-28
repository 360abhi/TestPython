def myfunc(*args,**kwargs):
    print(list(arg for arg in args))
    print(dict({v:k for k,v in kwargs.items()}))


myfunc("Abhishek","Kalyan",mvar="Hello")

