"""
Zadanie 0

Przygotuj funkcję sprawdzającą czy osoba o podanym wieku jest
osobą pełnoletnią

"""

def is_adult(age: int) -> bool:
    return age >= 18


def test_is_adult():
    # given
    age = 18

    # when
    result = is_adult(age)

    # then
    assert result

def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(3)

