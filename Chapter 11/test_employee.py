import pytest

from employee import Employee


@pytest.fixture
def employee():
    """Create an employee instance for use in multiple tests."""
    employee = Employee("Colby", "ONeal", 50000)
    return employee


def test_give_default_raise(employee):
    """Test that the default raise adds 5000 to the salary."""
    employee.give_raise()

    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """Test that a custom raise amount is added to the salary."""
    employee.give_raise(10000)

    assert employee.annual_salary == 60000