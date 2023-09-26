from datetime import datetime
startTime = datetime.now()

while True:  # This will keep asking until a valid integer is entered
    user_input = input("Enter an integer value for X: ")
    try:
        X = int(user_input)  # Try to convert the input to an integer
        break  # If the conversion succeeds, break out of the loop
    except ValueError:  # If the conversion fails, a ValueError will be raised
        print("That's not a valid integer. Please try again.")

# Now you can use X as an integer in your code

fileToSort = "/Users/marchundia/DataCodingChallenge/output.txt"
# Step 1: Open the file
with open(fileToSort, 'r') as file:
    # Step 2: Read the file line by line
    data = [list(map(int, line.split())) for line in file]  # Steps 3, 4, and 5

# Now, 'data' is a 2-dimensional array containing the data from the file


# Using sorted to sort the array based on the 2nd element of each sub-array
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

#Time to complete:
time_to_complete = (datetime.now() - startTime)
print("Time to complete based on " + str(X) + " Rows to sort:")
print(time_to_complete)

# Iterate through the first X elements of the sorted array
for row in sorted_data[:X]:
    print(row)

print("Time to complete based on " + str(X) + " Rows to sort:")
print(time_to_complete)




