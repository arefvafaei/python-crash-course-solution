from Employee import Employee
#
#
# def test_give_default_salary():
#     employee = Employee("aref", "vafaei",10000)
#     assert Employee.give_raise(employee) == 15000
#
#
# def test_give_custom_salary():
#     employee = Employee("aref", "vafaei",10000)
#     assert Employee.give_raise(employee,10000) == 20000
#
import pytest


@pytest.fixture
def employee():
    return Employee("aref", "vafaei", 10000)


def test_give_default_salary(employee):
    employee.give_raise()
    assert employee.salary == 15000


def test_give_custom_salary(employee):
    employee.give_raise(10000)
    assert employee.salary == 20000
