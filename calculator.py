from tkinter import *

class Calculator:

    def __init__(self):
        self.root=Tk()
        self.root.title('Basic Calculator!')

        self.root.minsize(250,350)
        self.root.maxsize(250,350)

        self.result=Label(self.root,text='',bg='white',width='24',height=4)
        self.result.grid(row=0,column=0,columnspan=4)

        self.btn1 = Button(self.root, text='1', bg='pink', width=6, height=4,command=lambda: self.get_num("1")).grid(row=1,column=0)
        self.btn2 = Button(self.root, text='2', bg='pink', width=6, height=4,command=lambda: self.get_num("2")).grid(row=1, column=1)
        self.btn3 = Button(self.root, text='3', bg='pink', width=6, height=4,command=lambda: self.get_num("3")).grid(row=1, column=2)
        self.btnAdd = Button(self.root, text='+', bg='pink', width=6, height=4,command=lambda: self.get_operator("+")).grid(row=1, column=3)

        self.btn4 = Button(self.root, text='4', bg='pink', width=6, height=4,command=lambda: self.get_num("4")).grid(row=2, column=0)
        self.btn5 = Button(self.root, text='5', bg='pink', width=6, height=4,command=lambda: self.get_num("5")).grid(row=2, column=1)
        self.btn6 = Button(self.root, text='6', bg='pink', width=6, height=4,command=lambda: self.get_num("6")).grid(row=2, column=2)
        self.btnSub = Button(self.root, text='-', bg='pink', width=6, height=4,command=lambda: self.get_operator("-")).grid(row=2, column=3)

        self.btn7 = Button(self.root, text='7', bg='pink', width=6, height=4,command=lambda: self.get_num("7")).grid(row=3, column=0)
        self.btn8 = Button(self.root, text='8', bg='pink', width=6, height=4,command=lambda: self.get_num("8")).grid(row=3, column=1)
        self.btn9 = Button(self.root, text='9', bg='pink', width=6, height=4,command=lambda: self.get_num("9")).grid(row=3, column=2)
        self.btnDiv = Button(self.root, text='/', bg='pink', width=6, height=4,command=lambda: self.get_operator("/")).grid(row=3, column=3)

        self.btn0 = Button(self.root, text='0', bg='pink', width=6, height=4,command=lambda: self.get_num("0")).grid(row=4, column=0)
        self.btnMul = Button(self.root, text='*', bg='pink', width=6, height=4,command=lambda: self.get_operator("*")).grid(row=4, column=1)
        self.btnC = Button(self.root, text='C', bg='pink', width=6, height=4,command=lambda: self.clear()).grid(row=4, column=2)
        self.btnEql = Button(self.root, text='=', bg='pink', width=6, height=4,command=lambda: self.calculate()).grid(row=4, column=3)

        self.root.mainloop()

    def get_num(self,number):

        new_text=self.result['text']+number
        self.result.configure(text=new_text)

    def clear(self):
        self.result.configure(text="")

    def get_operator(self,operator):
        self.first_number=int(self.result['text'])
        self.result.configure(text="")
        self.operator=operator

    def calculate(self):
        self.second_number=int(self.result['text'])

        if self.operator=='+':
            answer=self.first_number+self.second_number
            self.result.configure(text=str(answer))
        elif self.operator=='-':
            answer=self.first_number-self.second_number
            self.result.configure(text=str(answer))
        elif self.operator=='*':
            answer=self.first_number*self.second_number
            self.result.configure(text=str(answer))
        elif self.operator=='/':
            if self.second_number==0:
                self.result.configure(text='Gadha naki?')
            else:
                answer = self.first_number/self.second_number
                self.result.configure(text=str(answer))



obj1=Calculator()