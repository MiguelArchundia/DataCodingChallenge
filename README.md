Data Coding Challenge
Miguel Archundia's Data Coding Challenge - September 2023


Ensure you have Python 3.10.6 installed as it's required for this script to function correctly. No additional libraries are necessary since heapq, os, and datetime are included with this version of Python.

Files:
heap_implementation.py: This is the main file.
generate_file.py: If no file is provided, use this script to generate a file with a specified number of rows.
tests_heap_implementation.py: Utilize this file to test the methods used in heap_implementation.py.
Execution Instructions:
Run heap_implementation.py. It will prompt you to enter a full path to the input file. If no valid path is provided, the script will fall back to a default path defined within the script. You might need to modify this default path to match your local setup.
Upon execution, you will be prompted to enter a value for X, which represents the number of top values to be popped from the heap, demonstrating the solution to the data coding challenge.
This implementation utilizes a heap which significantly accelerates the process, making it orders of magnitude quicker than using the typical sorted method in Python.

Context:
This challenge simulates a scenario similar to handling a priority queue, which requires a swift determination of process prioritization.
