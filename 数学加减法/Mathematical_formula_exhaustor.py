# coding=utf-8
#!/usr/bin/env python


class Mathematical_formula_exhaustor():
    def __init__(self) -> None:
        pass

    def plus_under_10(self, start_number):
        "10以内的两位数加法"
        res = {"name": "plus_under_10",
               "datalist": []}
        number_limit = 10
        for n1 in range(start_number, number_limit + 1):
            for n2 in range(start_number, number_limit + 1 - n1):
                if n1 == 0 or n2 == 0:
                    is_0 = 'Y'
                else:
                    is_0 = 'N'
                question = "{} ＋ {} = (  )".format(n1, n2)
                answer = n1 + n2
                res["datalist"].append(
                    {"is_0": is_0, "question": question, "answer": answer})
        return res


if __name__ == '__main__':
    pass
    gen = Mathematical_formula_exhaustor()
    a = gen.plus_under_10(0)
    print(a)
