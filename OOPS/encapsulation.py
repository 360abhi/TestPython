class Temperature:

    def __init__(self,celsius):
        self.__celsius = celsius

    @property
    def celsius(self):           # Getter
        return self.__celsius
    
    def set_celsius(self, value):   # Setter
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self.__celsius = value

t = Temperature(34)
print(t.celsius)