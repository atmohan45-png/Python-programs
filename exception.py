class calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def additon(self,opr):
        try:
            if opr=="+":
                return self.num1+self.num2
            elif opr=="-":
                return self.num1-self.num2
            elif opr=="*":
                return self.num1*self.num2
            elif opr=="/":
                return self.num1/self.num2
            else:
                return "invalid operator"
        except ZeroDivisionError:
            return "division by zero is not allowed"    
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
operator=input("enter operator (+,-,*,/):")
calculator=calc(num1,num2)
