"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division calculation object"""
    def get_result(self):
        """get the Division results"""
        quotient = 1.0
        for value in self.values:
            quotient = value/quotient
        return quotient
