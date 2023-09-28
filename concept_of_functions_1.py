#define a function
"""
Syntax for defining a function 

def function_name():
    <statements>

def function_name(args):
    <statements>
"""
def doSomething():
    print("I am a function")#statement- calling the print function

def doAnotherThing(name:str):
    print("I am  "+ name) #calling the print function

def doTheThirdThing(name:str, height:float):
    #print("I am  "+ name) #calling the print function
    doAnotherThing(name)#calling the doAnotherThing function
    print("I am "+ str(height) + "meters")#calling the print function

#calling a function
"""
Syntax for calling a function 

function_name()
"""
doSomething()#no argument calling the doSomething function
doAnotherThing("Joseph")# 1 argument calling the doAnotherThing function
doTheThirdThing("Okon", 1.74)# 2 argument calling the doTheThirdThing function


def doTheFourthThing():
    doAnotherThing("Amanam")#calling the print doAnotherThing function

doTheFourthThing()