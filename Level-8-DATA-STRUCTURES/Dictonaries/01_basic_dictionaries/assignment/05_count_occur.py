#EXAMPLE: COUNT OCCURING USING `in`

words = ["oneplus", "apple", "realme", "redmi", "oppo", "nokia", "samsung", "oneplus"]

counts = {}
for word in words: 
    if word in counts: 
        counts[word] += 1
    else: 
        counts[word] = 1
print(counts)

#o/p: {'oneplus': 2, 'apple': 1, 'realme': 1, 'redmi': 1, 'oppo': 1, 'nokia': 1, 'samsung': 1}