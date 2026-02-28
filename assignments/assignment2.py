"""
1) we have Dirctory with 5 files. Each file has Different size: 2048, 4357, 97658, 125 and 8.
Calculate the average file size. Set the files varible to the number of files.
finally, output a message saying "The average size is: " 
hint: use the str() fyunmction to conver the number into string.
"""
# f1 = 2048;  f2 = 4357;  f3 = 97658; f4 = 125; f5 = 8  #Each file has Different size: 2048, 4357, 97658, 125 and 8.
f1, f2, f3, f4, f5 = 2048, 4357, 97658, 125, 8
Total_File_Size = f1+f2+f3+f4+f5 
Files = 5 #number of files.
Avg_File_size = Total_File_Size/Files
print("The average size is:" + str(Avg_File_size)) #The average size is:20839.2

"""
2) two friends are eating dinner at resturent, The bill comes in the amount of 47.28$
The friends decided to split the bill evenly between them. 
after adding 15% tip for the service. 
calculate the tip, The total amount to pay and eachs share friends. 
The output saying " Each person needs to pay: " 
"""
Actual_Bill = 47.28 
Tip = Actual_Bill * 0.15 
Total_Bill_with_tip = Actual_Bill + Tip
Bill_share_each = Total_Bill_with_tip / 2
print("Each person needs to pay: " + str(Bill_share_each)) #Each person needs to pay: 27.186


#dividedbyzerofix error 
numerator = 10 
denominator = 0 

if not denominator: 
    denominator = 10 
result = numerator/denominator
print(result)