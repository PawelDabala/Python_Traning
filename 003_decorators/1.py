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


answer_one = True
answer_two = False

pineaplles = 5
zebra = 2

zebra < pineaplles
pineaplles > zebra
pineaplles == zebra



ola_age = 10
ola_height = 1.5
(ola_age > 8) and (ola_height > 1.4)

is_dark = input('Is it dark outside? y/n)')
if is_dark == 'y':
    print('Goodnight! Zzzzzzzzzzzzzzz....')
else:
    print('Goodmoring')


weather = input ('What is the forecast for today? (rain/snow/sun)')
if weather == 'rain':
    print('Remember your umbrella!')
elif weather == 'snow':
    print('Remember your woolly gloves!')
else:
    print('Remember your sunglasses!')

for licznik in range(1, 11):
    print('Emma\'s Room - Keep Out!!!')

for licznik in range(10):
    print('Emma\'s Room - Keep Out!!!')


while True:
    print('This is an infinite loop!')


while True:
    answer = input('Are you bored yet? (y/n)')
    if answer == 'y':
        print('How rude!')
        break

for hooray_counter in range(1, 4):
    for hip_counter in range(1, 3):
        print('Hip')
    print('Hooray!')

cars = ['opel', 'volvo', 'vw', 'audi']
for car in cars:
    print(car)