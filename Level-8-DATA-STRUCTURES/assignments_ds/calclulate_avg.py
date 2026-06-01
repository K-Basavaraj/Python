cpu_loads = [45, 92, 30, 75, 88]
#calculate the average cpu load
average_load = sum(cpu_loads) / len(cpu_loads)
print(f"Average CPU Load: {average_load}") #output: Average CPU Load: 66.0 here we have calculated the average CPU load by using the sum() function to get the total of all the CPU loads and then dividing that total by the number of CPU loads, which we get using the len() function. The result is the average CPU load, which is 66.0 in this case.

#sum() type error only works with numbers not with strings

