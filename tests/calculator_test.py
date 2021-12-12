"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    Calculations.clear_history()
def test_calculator_add_static(clear_history_fixture):
    """testing the add"""
    my_tuple = (1.0,2.0,5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8.0
def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    my_tuple = (1.0,2.0,3.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == -6.0
def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    my_tuple = (1.0,2.0,3.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 6.0
def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide  method of the calc"""
    my_tuple = (1.0,2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 0.5