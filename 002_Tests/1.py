"""
Przygotuj funkcję, która na podstawie
wysogości oraz dugości podstawy
Wyświeti (print) pole trójkąta

"""

def get_triangle_field(base: int, height: int) -> float:
    print(0.5 * base * height)

# capsys - pobranie iwentów systemowych, 
# pobiera to co wyświetla program lub błędy
def test_triangle_area(capsys):
    #try
    base = 10
    height = 8

    #when
    get_triangle_field(base, height)
    #zwraca tuple z wynikiem i ewentualnym błędem
    out, err = capsys.readouterr()

    #then
    assert out == '40.0\n'
