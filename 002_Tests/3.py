"""
Przygotuj funkcję, która będzie sortowała otrzymywaną listę imion:
- w kolejności alfabetycznej pierwszej litery,
- w kolejności alfabetycznej ostatniej litery,
- według długości imienia

"""
import pytest

def sort_by(names, first_letter= False, last_letter=False, lenght=False):
    if first_letter:
        names.sort()

    if last_letter:
        #odwrucenie sortowania
        names.sort(key= lambda name: name[::-1])

    if lenght:
        names.sort(key=len)

    return names


class TestSort:
    # uzycie fixture pozwala w jednym miejscu zadeklarować 
    # dane których można uzywać w innych funkcjach
    # wymagany import biboteki pytest    
    @pytest.fixture
    def names(self):
        return ['Alina', 'Ewa', 'Paulina', 'Maciej']

    def test_sort(self, names):
        
        # when
        sorted_names = sort_by(names, first_letter=True)

        # then
        assert sorted_names == ['Alina', 'Ewa', 'Maciej', 'Paulina']

    def test_reverse_sort(self, names):
        # when
        sorted_names = sort_by(names, last_letter=True)

        # given
        assert sorted_names == ['Alina', 'Paulina', 'Ewa', 'Maciej']

    def test_by_lenght(self, names):
        # when
        sorted_names = sort_by(names, lenght=True)

        # given
        assert sorted_names == ['Ewa', 'Alina','Maciej', 'Paulina']





    