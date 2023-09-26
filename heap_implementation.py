import heapq
import os
from datetime import datetime


#Optional Method for asking the user to provide the full filepath to the output file
def process_file(file_path=None):
    default_file = "/Users/marchundia/DataCodingChallenge/output.txt"

    if file_path is None:
        file_path = input("Please provide the full path to the file: ")

    if os.path.exists(file_path):
        # File exists
        print(f"Processing file: {file_path}")
        return file_path
    else:
        print("Error: The file + " + file_path +  " does not exist.")
        file_path = default_file
        print("Using default file: " + file_path)
        return file_path

# method for getting user input for X, aka number of times to pop from top of heap
def getUserInput():
    while True:  
        user_input = input("Enter an integer value for X: ")
        try:
            X = int(user_input)  
            break  
        except ValueError:  
            print("That's not a valid integer. Please try again.")

#Method for reading the file
def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read().split()
    return [(int(data[i]), int(data[i+1])) for i in range(0, len(data), 2)]

#To create a max heap using heapq invert the array 
def heapify_2d(arr):
    max_heap = [(-t[1], t) for t in arr]
    heapq.heapify(max_heap)
    return max_heap

#Method for building the heap 
# Method for building the heap 
# time complexity of heappush is O(log n), where n is the number of elements in the heap.
# or this case the number of lines in the file
def heappush(heap, item):
    heapq.heappush(heap, (-item[1], item))

#Method for poping the head form the heap    
def heappop(heap):
    priority, item = heapq.heappop(heap)
    return item

def getUserInput():
    while True:  # This will keep asking until a valid integer is entered
        user_input = input("Enter an integer value for X: ")
        try:
            X = int(user_input)  # Try to convert the input to an integer
            return X
            break  # If the conversion succeeds, break out of the loop
        except ValueError:  # If the conversion fails, a ValueError will be raised
            print("That's not a valid integer. Please try again.")

   

if __name__ == "__main__":

    try:
        file_path = process_file()  # User provides the file path or default is chosen
        times_to_pop = getUserInput() # User chooses int to determine times to pop from top of heap
        list_data = read_file(file_path) # Heap is taken from the file 

        startTime = datetime.now() # Start time in order to determine length of time for heap building
        max_heap = heapify_2d(list_data) # Building the heap
        time_to_complete = (datetime.now() - startTime) # time it took to create the heap

        for _ in range(min(times_to_pop, len(max_heap))):  # Ensure X is not greater than the number of items in the heap
            item = heappop(max_heap)
            print(item[0])  # Print tuples in descending order based on the second column

        print("Completion time: " + str(time_to_complete)) # print time to complete operation

    except KeyboardInterrupt:
        print("\nUser interrupted the process.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
