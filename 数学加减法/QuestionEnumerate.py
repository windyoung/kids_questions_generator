# coding=utf-8
#!/usr/bin/env python3

import math


class math_enumerate():
    def __init__(self) -> None:
        self.start_number = 1
        pass

    def plus_questions(self, number_limit: int, is_startfrom_0: bool = False, Number_of_operations: int = 2):
        questions = []
        if is_startfrom_0:
            start_number = 0
        else:
            start_number = 1
        match Number_of_operations:
            case 2:
                for n1 in range(start_number, number_limit + 1):
                    for n2 in range(start_number, number_limit + 1 - n1):
                        question = "{} ＋ {} =[   ]".format(n1, n2)
                        questions.append(question)

            case 3:
                for n1 in range(start_number, number_limit + 1):
                    for n2 in range(start_number, number_limit + 1 - n1):
                        for n3 in range(start_number, number_limit + 1 - n1 - n2):
                            question = "{} ＋ {} ＋ {} =[   ]".format(n1, n2, n3)
                            questions.append(question)
            case 4:
                for n1 in range(start_number, number_limit + 1):
                    for n2 in range(start_number, number_limit + 1 - n1):
                        for n3 in range(start_number, number_limit + 1 - n1 - n2):
                            for n4 in range(start_number, number_limit + 1 - n1 - n2 - n3):
                                question = "{} ＋ {} ＋ {} ＋ {} =[   ]".format(
                                    n1, n2, n3, n4)
                                questions.append(question)
        return questions

    def minus_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2):
        questions = []
        if is_startfrom_0:
            start_number = 0
        else:
            start_number = 1
        match Number_of_operations:
            case 2:
                for n1 in range(number_limit, start_number - 1, -1):
                    for n2 in range(start_number, n1 + 1):
                        question = "{} － {} =[   ]".format(n1, n2)
                        questions.append(question)

            case 3:
                for n1 in range(number_limit, start_number - 1, -1):
                    for n2 in range(n1 - 1, start_number - 1, -1):
                        for n3 in range(n2, start_number - 1, -1):
                            if (n1 - n2 - n3 >= 0):
                                question = "{} － {} － {} =[   ]".format(
                                    n1, n2, n3)
                                questions.append(question)
            case 4:
                for n1 in range(number_limit, start_number - 1, -1):
                    for n2 in range(n1 - 1, start_number - 1, -1):
                        for n3 in range(n2, start_number - 1, -1):
                            for n4 in range(n3, start_number - 1, -1):
                                if (n1 - n2 - n3 - n4 >= 0):
                                    question = "{} － {} － {} － {} =[   ]".format(
                                        n1, n2, n3, n4)
                                    questions.append(question)
        return questions

    def mutiply_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2, is_squared: bool = True):
        questions = []
        if is_squared:
            root = math.ceil(math.sqrt(number_limit))
        if is_startfrom_0:
            start_number = 0
        else:
            start_number = 1
        match Number_of_operations:
            case 2:
                for n1 in range(start_number, root + 1):
                    for n2 in range(start_number, root + 1):
                        if (n1 * n2 <= number_limit):
                            question = "{} × {} =[   ]".format(n1, n2)
                            questions.append(question)

            case 3:
                for n1 in range(start_number, root + 1):
                    for n2 in range(start_number, root + 1):
                        for n3 in range(start_number, root + 1):
                            if (n1 * n2 * n3 <= number_limit):
                                question = "{} × {} × {} =[   ]".format(
                                    n1, n2, n3)
                                questions.append(question)
            case 4:
                for n1 in range(start_number, root + 1):
                    for n2 in range(start_number, root + 1):
                        for n3 in range(start_number, root + 1):
                            for n4 in range(start_number, root + 1):
                                if (n1 * n2 * n3 * n4 <= number_limit):
                                    question = "{} × {} × {} × {} =[   ]".format(
                                        n1, n2, n3, n4)
                                    questions.append(question)
        return questions

    def divid_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2):
        pass

    def hybrid_operation_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2, operators: list = ['＋', '－', '×', '÷']):
        pass


if __name__ == '__main__':
    me = math_enumerate()
    number_limit = 90
    is_startfrom_0 = False
    Number_of_operations = 4
    is_squared = True
    a = me.mutiply_questions(number_limit, is_startfrom_0,
                             Number_of_operations, is_squared)
    print(a, len(a))
