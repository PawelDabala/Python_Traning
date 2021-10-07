#dekorator przyjmuje funkcje
def uppercase(func):
    #funkcja która będzie zwrócona, wydmuszka
    # *args i **kwargs są po to aby przekazywać argumenty do fonkcji
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper

def repeat(times):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            response = []
            for _ in range(times):
                response.append(func(*args, **kwargs))

            return response
        return inner_wrapper

    return wrapper

@repeat(3)
def hello(name):
    return f'Helo {name}'
print(hello('Jaga'))

# print(repeat(4)(hello)("Pawel"))
   


