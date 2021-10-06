def foo():
    return 'bar'

def hello(name):
    return f'Helo {name}'

#dekorator przyjmuje funkcje
def uppercase(func):
    #funkcja która będzie zwrócona, wydmuszka
    # *args i **kwargs są po to aby przekazywać argumenty do fonkcji
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper

print(uppercase(foo)())
print(uppercase(hello)('Pawel'))

