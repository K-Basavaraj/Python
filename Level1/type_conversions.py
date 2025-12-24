#print (7 + "8") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(type("a")) #<class 'str'>
print(type(2)) #<class 'int'>
print(type(2.5)) #<class 'float'>
name = "Rajesh"
#print(name)   #output: Rajesh
print(type(name)) #<class 'str'>
#====================================================================================================
                                        #Implict conversion 
#====================================================================================================
#The interpreter automatically conver one data type to another type is called type casting.
print(7+8.5) #15.5 int + float 15.5 here the interpreter will automatcially convert int 7 into float 7 and                       the result will also be float 

print("a" + "b" + "c") #abc

print("This " + "is " + "pretty " + "good!") #This is pretty good!

#====================================================================================================
                                        #Explist conversion(Manually convert)
#====================================================================================================
# for converting str type to int is possible? yes! with explist converstion we call a function with                            the name of the type we are converting to. 
#Area of Triangle formula=(Area=1/2​×base×height)

Base = 30
Height = 25
area = (Base*Height)/2 
#print("The are of Triangle is: " + area) ##TypeError: can only concatenate str (not "float") to str
print("The are of Triangle is: " + str(area)) #The are of Triangle is: 375.0 its converting num to string 
