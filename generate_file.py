import random

def generate_file(num_lines):
    # Ensure unique numbers by keeping track of generated numbers
    generated_numbers = set()

    # File name is output file + number of lines
    file_name = f'output_{num_lines}.txt'


    # Open file for writing
    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            # Generate unique 10-digit number
            while True:
                unique_number = str(random.randint(100_000_0000, 999_999_9999))
                if unique_number not in generated_numbers:
                    generated_numbers.add(unique_number)
                    break
            
            # Generate random number between 1 and 100,000,000
            random_number = random.randint(1, 100_000_000)
            
            # Write to file
            file.write(f'{unique_number} {random_number}\n')

# Get user input for the number of lines to generate
num_lines = int(input('Enter the number of lines to generate: '))
generate_file(num_lines)
