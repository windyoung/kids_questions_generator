# coding=utf-8
#!/usr/bin/env python
from email import header
import random
import labels
import os
import math
from reportlab.graphics import shapes
# import prettytable
from prettytable import PrettyTable, MSWORD_FRIENDLY, ALL
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont


class MathematicalFormulaGenerator():
    def __init__(self) -> None:
        self.Mathematical_operation_symbol = ['＋', '－', '×', '÷']
        self.Questions_list = []
        pass

    def math_generator(self, number_limit, operation_symbols, question_number, is_squared):
        "生成算式,需要带 参数1：数字限制；参数2：可用的运算符"
        question_number = math.ceil(question_number*1.5)
        question_Queue = []
        for i in range(question_number):
            question_Queue.append(random.choice(operation_symbols))
        for i in question_Queue:
            try:
                match i:
                    case '＋':
                        res = self.math_plus(number_limit).__next__()
                    case '－':
                        res = self.math_minus(number_limit)
                    case '×':
                        res = self.math_mutiply(
                            number_limit, is_squared).__next__()
                    case '÷':
                        res = self.math_Divid(number_limit, is_squared)
                self.Questions_list.append(res)
            except StopIteration:
                continue

        if len(self.Questions_list) < question_number:
            # print("1", len(self.Questions_list), "<", question_number)
            self.math_generator(number_limit, operation_symbols,
                                question_number-len(self.Questions_list), is_squared)

    def math_generator_starter(self, number_limit, operation_symbols, question_number, is_squared=True):
        self.math_generator(
            number_limit, operation_symbols, question_number, is_squared)
        Questions = self.Questions_list[0:question_number]
        # print("2 , question_number", question_number, "Questions_list",
        #       len(self.Questions_list), "Questions", len(Questions))
        q_text = []
        for i in Questions:
            # print(i,type(i))
            key = list(i.keys())[0]
            # print(i, key)
            q_text.append("{} {} {} = [   ] ".format(
                i[key][0], key, i[key][1]))
        return q_text

    def math_plus(self, number_limit):
        plus1 = random.randint(0, number_limit-1)
        plus2 = random.randint(0, number_limit-1)
        res = plus1 + plus2
        while True:
            if (res <= number_limit):
                yield {"＋": [plus1, plus2]}

            else:
                self.math_plus(number_limit)
            break  # StopIteration

    def math_minus(self, number_limit):
        minus1 = random.randint(1, number_limit)
        minus2 = random.randint(0, number_limit-minus1)
        res = minus1 - minus2
        if (res >= 0):
            return {"－": [minus1, minus2]}
        else:
            return {"－": [minus2, minus1]}

    def math_mutiply(self, number_limit, is_squared):
        if is_squared:
            root = math.ceil(math.sqrt(number_limit))
            mutiply1 = random.randint(1, root)
            mutiply2 = random.randint(1, root)
        else:
            mutiply1 = random.randint(1, number_limit//2)
            mutiply2 = random.randint(1, number_limit//mutiply1)
        res = mutiply1*mutiply2
        while True:
            if (res <= number_limit):
                yield {"×": [mutiply1, mutiply2]}
            else:
                self.math_mutiply(number_limit, is_squared)
            break  # StopIteration

    def math_Divid(self, number_limit, is_squared):
        res = self.math_mutiply(number_limit, is_squared).__next__()
        # print(res)
        divid1 = res["×"][0]*res["×"][1]
        divid2 = res["×"][1]
        return {'÷': [divid1, divid2]}  # StopIteration


if __name__ == '__main__':
    formula_generator = MathematicalFormulaGenerator()
    # a = formula_generator.math_plus(10)
    # print(a.__next__())
    # b = formula_generator.math_minus(10)
    # print(b)
    # c = formula_generator.math_mutiply(100, False)
    # print("c", c.__next__())
    # c1 = formula_generator.math_mutiply(100)
    # print("c1", c1.__next__())
    # d = formula_generator.math_Divid(100,True)
    # print("d True",d)
    # d1 = formula_generator.math_Divid(100,False)
    # print("d1 False",d1)
    # ['＋', '－', '×', '÷']
    K = formula_generator.math_generator_starter(10, ['＋', '－'], 20, True)
    print(len(K), K)
