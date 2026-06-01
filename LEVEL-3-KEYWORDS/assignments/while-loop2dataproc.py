# import os
# print(os.getcwd())

# Example: Reading a file line-by-line using a while loop.
# The loop continues until the end of file (EOF) is reached.
# readline() returns an empty string ("") when no more lines are available.

# Open the file in read mode ("r")
# 'with' ensures the file is automatically closed after use.
with open("sample_data.txt", "r") as input_file:

    # Read the first line from the file
    line = input_file.readline()

    # Continue looping as long as 'line' contains data
    # When EOF is reached, readline() returns an empty string,
    # which evaluates to False and stops the loop.
    while line:

        # strip() removes leading/trailing whitespace and newline characters
        print(line.strip())

        # Read the next line in each iteration
        line = input_file.readline()

# End of file processing

