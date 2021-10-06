def foo():
    return 'bar'

#dekorator przyjmuje funkcje
def uppercase(func):
    #funkcja która będzie zwrócona
    def wrapper():
        return func().upper()

    return wrapper

print(uppercase(foo)())