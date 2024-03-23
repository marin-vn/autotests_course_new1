# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ((10,), 10),
                             ((10, 5), 2),
                             pytest.param((10, 5, 2), 1, marks=pytest.mark.skip('bad test')),
                             pytest.param((10, 5, 2, 2), 0.5, marks=pytest.mark.smoke),
                             ((10, 5, 2, 2, 0), ZeroDivisionError)
                         ]
                         )
def test_parametrize(numbers, expected_result):
    if expected_result == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            all_division(*numbers)
    else:
        assert all_division(*numbers) == expected_result
