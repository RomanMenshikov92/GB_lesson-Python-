import pytest
from controls import DecToDouble
from controls import list_mixing
from controls import numberDayWeek

# test for hw__3.4 form homework-3


@pytest.mark.parametrize('decimal_number, expected_result', [(45, '101101'), (3, '11'), (2, '10')])
def test_DecToDouble(decimal_number, expected_result):
    assert DecToDouble(decimal_number) == expected_result


# test for hw__2.5 form homework-2
@pytest.mark.parametrize('list_input', [([1, 2, 3, 4, 5]),
                                        (['b', 'a', 99, 9])])
def test_mix_list_good(list_input):
    first = list_input
    second = list_mixing(list_input)
    assert first != second


# test for hw__1.1 form homework-1
@pytest.mark.parametrize('x, expected_result', [(1, 'Нет.Это Понедельник'), (2, 'Нет.Это Вторник'), (3, 'Нет.Это Среда'), (4, 'Нет.Это Четверг'), (5, 'Нет.Это Пятница'), (6, 'Да.Это Суббота'), (7, 'Да.Это Воскресенье')])
def test_numberDayWeek(x, expected_result):
    assert numberDayWeek(x) == expected_result
