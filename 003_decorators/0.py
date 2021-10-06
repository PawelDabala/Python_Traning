#dekorator przyjmuje funkcje
def uppercase(func):
    #funkcja która będzie zwrócona, wydmuszka
    # *args i **kwargs są po to aby przekazywać argumenty do fonkcji
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper

@uppercase   
def foo():
    return 'bar'

@uppercase
def hello(name):
    return f'Helo {name}'


print(foo())
print(hello("Pawel"))
   


