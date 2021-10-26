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


first_name = 'Jan'
second_name = "Kowalski "
print(first_name)
print(second_name)

print(first_name + second_name)

>>> len("Hellow")
6

rocket_player1 = "Tom"
rocket_player2 = "Anna"
rocket_player3 = "Waldek"

rocket_players = ["Tom", "Anna", "Waldek"]

rocket_players[0]
rocket_players.append("Jola")
rocket_players[0] = "Waldek"

#usunięcie gracza o indexie 2
del rocket_players[2]
# usunięcie cąłej listy
del rocket_players
# usunięcie elementu po wartości
rocket_players.remove("Anna")
# usunięcie elementu i zwrócenie
rocket_players.pop()
rocket_players.pop(2)

#użytkownik od 1 do 2
rocket_players[1:3]
#użytkownik od 1 do końca
rocket_players[1:]
#użytkownik do drugiego włącznie
rocket_players[:3]
