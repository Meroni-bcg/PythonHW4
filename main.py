# 1. Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

# 2. Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [2, 3, 4, 5]
result = mult_list(numbers)
print(result)  # Output: 120

#the mult_list() function is defined correctly with the appropriate indentation. The numbers list is passed as an argument to the function when calling mult_list(numbers). The function calculates the product of all the numbers in the numbers list correctly, and the returned result is stored in the result variable. Finally, the result is printed, which should output 120, the product of the numbers [2, 3, 4, 5]


# 3. Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

string = "Meroni, Cervantes!"
result = rev_string(string)
print(result)  # Output: "!setnavreC ,inoreM"

# 4. Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(number, range_start, range_end):
    return range_start <= number <= range_end

print(num_within(3, 2, 4))  # Output: True
print(num_within(3, 1, 3))  # Output: True
print(num_within(10, 2, 5))  # Output: False

# 5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    triangle = []  # List to store the rows of Pascal's triangle

    for i in range(n):  # Iterate 'n' times to generate 'n' rows
        row = [1]  # First element of each row is always 1

        if i > 0:
            previous_row = triangle[i - 1]  # Get the previous row from the triangle list
            for j in range(len(previous_row) - 1):
                # Calculate the sum of adjacent elements from the previous row and append it to the current row
                row.append(previous_row[j] + previous_row[j + 1])

            row.append(1)  # Last element of each row is always 1

        triangle.append(row)  # Append the current row to the triangle list

    # Print the triangle
    for row in triangle:  # Iterate over each row in the triangle list
        # Convert each number to a string and join them with spaces to form a string representation of the row
        print(" ".join(str(num) for num in row))
pascal(5)
