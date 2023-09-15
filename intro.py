#syntax 
#<variable> = value
#Single Line Comment
"""
Multiple Line Comment
"""
name = "Joseph"#create a location call name and store value Joseph in that location.
print(name) #print (go to the location and get the value)
#<variable> = value
what_type_is_this = type(name)
print("The type is: "+ str(what_type_is_this))

#def functionName():
def doSomething():
    print("I am a method")

def getWaterForMe():
    print("I am going to get water")

def buyBiscuitsForMe(money):
    print("I have been given "+ "$"+str(money)+ " to buy biscuits")

# doSomething()
# getWaterForMe()
# buyBiscuitsForMe(20)

def fullName(firstName, surname):#method definition
    print("Your full name is : " +str(firstName)+ " "  +str(surname))

fullName("Dominic", "Thompson") #method call -> calling the method(function)
fullName("Joseph", "Okon")
fullName("Benjamin", "Jackson")