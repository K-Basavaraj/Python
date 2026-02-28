#====================================================================================================
                                    # Annotating variblesby type: #
#====================================================================================================
"""
Type annotation allows you to clearly cummunicate the argument type and return type of function 
in the code. 
its helpful for developers, where hints like what kind of data the varibale is supposed to hold.

Think of annoting a varible as if you were to put a label on a cobtainer and anything in that container
should hold what the label is describing. 

The name is declared using colon(:)which is annoted with the type of str. indicated that name varible 
should hold a str value. 

If a function expects a list of integer you should annotelike  List[int]
"""

import typing
name: str = "Rajesh"
print(name) #Rajesh

age: int = 25
print(age) #25 #age is a varible int is a type of annotation 

salary: float = 30000.00
print(salary)

List_Of_Numbers: typing.List[int] = [1,2,3] 
print(List_Of_Numbers) #[1, 2, 3]

Tuple_Of_Numbers: typing.Tuple[int] = (4,5,6)
print(Tuple_Of_Numbers) #(4, 5, 6)

Dictonary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
print(Dictonary) #{'key1': 1, 'key2': 2}

Set_Of_Numbers: typing.Set[int] = {7,8,9}
print(Set_Of_Numbers) #{8, 9, 7}