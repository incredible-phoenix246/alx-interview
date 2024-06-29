README FILE

<!-- # #!/usr/bin/python3

# """

# Module to generate Pascal's Triangle

# """

# def pascal_triangle(int(n)):

# """

# Generate Pascal's Triangle up to the nth row (0-indexed).

# :param n: Number of rows of the Pascal's Triangle to generate.

# :type n: int

# :return: A list of lists representing the Pascal's Triangle.

# :rtype: list

# """

# if n <= 0:

# return []

# triangle = [[1]] # Initialize the first row of Pascal's Triangle

# for i in range(1, n):

# row = [1] # Start each row with a 1

# # Calculate the middle elements of the row

# row.extend(triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1]) - 1))

# row.append(1) # End each row with a 1

# triangle.append(row)

# return triangle -->
