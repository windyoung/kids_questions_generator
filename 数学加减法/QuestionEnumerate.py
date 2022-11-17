# coding=utf-8
#!/usr/bin/env python3

class math_enumerate():
    def __init__(self) -> None:
        self.start_number=1
        pass

    def plus_questions(self, number_limit: int, is_startfrom_0: bool=False, Number_of_operations: int = 2):
        questions=[]
        if is_startfrom_0:
            start_number=0
        else:
            start_number=1
        match Number_of_operations:
            case 2:
                for n1 in range(start_number,number_limit+1):
                    for n2 in range(start_number,number_limit+1-n1):
                        question="{} ＋ {} =[   ]".format(n1,n2)
                        questions.append(question)
                        
            case 3:
                for n1 in range(start_number,number_limit+1):
                    for n2 in range(start_number,number_limit+1-n1):
                        for n3 in range(start_number,number_limit+1-n1-n2):
                            question="{} ＋ {} ＋ {} =[   ]".format(n1,n2,n3)
                            questions.append(question)

        return questions

    def minus_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2):
        pass

    def mutiply_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2):
        pass

    def divid_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2):
        pass

    def hybrid_operation_questions(self, number_limit: int, is_startfrom_0: bool, Number_of_operations: int = 2, operators: list = ['＋', '－', '×', '÷']):
        pass


if __name__ == '__main__':
    me = math_enumerate()
    a=me.plus_questions(100,False,2)
    print(a,len(a))
