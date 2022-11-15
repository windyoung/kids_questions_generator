# coding=utf-8
#!/usr/bin/env python
from email import header
import random
import labels
import os
from reportlab.graphics import shapes
# import prettytable
from prettytable import PrettyTable, MSWORD_FRIENDLY, ALL
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont


class MathematicalFormulaGenerator():
    def __init__(self) -> None:
        self.Mathematical_operation_symbol = ['＋', '－', '×', '÷']
        pass

    def math_generator(self, number_limit, operation_symbol):
        "生成算式,需要带 参数1：数字限制；参数2：可用的运算符"
        pass

    def math_plus(self, number_limit):
        plus1 = random.randint(0, number_limit-1)
        plus2 = random.randint(0, number_limit-1)
        res = plus1 + plus2
        while(res <= number_limit):
            return [plus1, plus2]
        else:
            self.math_plus(number_limit)


if __name__ == '__main__':
    formula_generator = MathematicalFormulaGenerator()
    a = formula_generator.math_plus(10)
    print(a)


