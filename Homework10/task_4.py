# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


class TestClass:

    def test_one(self, func_timer):
        assert str(5) == '5'

    def test_two(self, func_timer):
        assert 5 + 2 == 7

    def test_three(self, func_timer):
        assert 'H' in 'Hello'

    def test_four(self, func_timer):
        arr = [1, 2, 3, 4]
        assert len(arr) == 4

    def test_five(self, func_timer):
        assert 5 * 2 == 10

    def test_six(self, func_timer):
        assert 14 - 6 == 8

    def test_seven(self, func_timer):
        assert 6 / 2 == 3

    def test_eight(self, func_timer):
        assert 7 % 2 == 1

    def test_nine(self, func_timer):
        assert 2 ** 3 == 8

    def test_ten(self, func_timer):
        assert 'world'.startswith('wor')

    def test_eleven(self, func_timer):
        assert 'cat' in ['dog', 'cat', 'mouse']

    def test_twelve(self, func_timer):
        assert None is None

    def test_thirteen(self, func_timer):
        assert 5 > 3

    def test_fourteen(self, func_timer):
        assert 'hello'.capitalize() == 'Hello'


# Фикстура class_timer применяется ко всему классу TestClass
@pytest.mark.usefixtures("class_timer")
class TestClass:
    def test_one(self, func_timer):
        assert str(5) == '5'

    def test_two(self, func_timer):
        assert 5 + 2 == 7

    def test_three(self, func_timer):
        assert 'H' in 'Hello'

    def test_four(self, func_timer):
        arr = [1, 2, 3, 4]
        assert len(arr) == 4

    def test_five(self, func_timer):
        assert 5 * 2 == 10

    def test_six(self, func_timer):
        assert 14 - 6 == 8

    def test_seven(self, func_timer):
        assert 6 / 2 == 3

    def test_eight(self, func_timer):
        assert 7 % 2 == 1

    def test_nine(self, func_timer):
        assert 2 ** 3 == 8

    def test_ten(self, func_timer):
        assert 'world'.startswith('wor')

    def test_eleven(self, func_timer):
        assert 'cat' in ['dog', 'cat', 'mouse']

    def test_twelve(self, func_timer):
        assert None is None

    def test_thirteen(self, func_timer):
        assert 5 > 3

    def test_fourteen(self, func_timer):
        assert 'hello'.capitalize() == 'Hello'
