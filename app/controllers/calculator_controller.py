"""imports"""
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for

"""calculator controller class"""
class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Enter a value for value 1 and or value 2'
        else:
            flash('CORRECT!!!')

            # get values
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # create tuple
            my_tuple = (value1, value2)
            # retrieve the operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator2.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator2.html')






