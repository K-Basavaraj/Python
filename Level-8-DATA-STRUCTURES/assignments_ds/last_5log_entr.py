logs = ["log1", "log2", "log3", "log4", "log5", "log6", "log7"]
recent_newest_first = logs[-5:][::-1]
print(recent_newest_first) #output: ['log7', 'log6', 'log5', 'log4', 'log3'] here we have sliced the logs list to get the last 5 items using logs[-5:], which gives us ['log3', 'log4', 'log5', 'log6', 'log7']. Then we reverse that slice using [::-1] to get the most recent logs first, resulting in ['log7', 'log6', 'log5', 'log4', 'log3'].
#reversed logs = logs[-5:] #this will give us the last 5 logs in the original order, which is ['log3', 'log4', 'log5', 'log6', 'log7']

#example2: 
items = ["a", "b", "c", "d", "e", "f", "g"]
items[::3] 
#start at index 0 (a), stop at the end of the list, step by 3
#output: ['a', 'd', 'g'] here we have sliced the items list starting from index 0 (which is "a"), stopping at the end of the list, and stepping by 3 (which means we take every third item). So we get the items at index 0 ("a"), index 3 ("d"), and index 6 ("g") in the resulting list.

items [::-1]
#start at the end of the list, stop at the beginning of the list, step by -1 (backwards)
#output: ['g', 'f', 'e', 'd', 'c', 'b', 'a'] here we have sliced the items list starting from the end of the list, stopping at the beginning of the list, and stepping by -1 (which means we take every item in reverse order). So we get all the items in the list but in reverse order, resulting in ['g', 'f', 'e', 'd', 'c', 'b', 'a'].

items [1:6:2]
#start at index 1 (b), stop before index 6 (f), step by 2
#output: ['b', 'd', 'f'] here we have sliced the items list
#starting from index 1 (which is "b"), stopping before index 6 (which is "f"), and stepping by 2 (which means we take every second item). So we get the items at index 1 ("b"), index 3 ("d"), and index 5 ("f") in the resulting list, which gives us ['b', 'd', 'f'].

items[::-2]
#start at the end of the list, stop at the beginning of the list, step by -2 (backwards, every 2nd item)
#output: ['g', 'e', 'c', 'a'] here we have sliced the items list starting from the end of the list, stopping at the beginning of the list, and stepping by -2 (which means we take every second item in reverse order). So we get the items at index 6 ("g"), index 4 ("e"), index 2 ("c"), and index 0 ("a") in the resulting list, which gives us ['g', 'e', 'c', 'a'].
