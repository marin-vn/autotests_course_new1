# Фикстура, считающая время начала и окончания выполнения всего класса тестов

import pytest
import time


@pytest.fixture(scope="class")
def class_timer(request):
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nTime taken to execute {request.cls.__name__}: {end_time - start_time} seconds")


# Фикстура, считающая время выполнения отдельного теста
@pytest.fixture()
def func_timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nTime taken to execute test: {end_time - start_time} seconds")
