1 #!/usr/bin/python3
  2 """
  3 Define a function that rotates an nxn 2D matrix 90 degrees clockwise     in-place.
  4 """
  5 
  6 
  7 def rotate_2d_matrix(matrix):
  8     n = len(matrix)
  9     
 10     # Step 1: Transpose the matrix (swap rows with columns)
 11     for i in range(n):
 12         for j in range(i, n):
 13             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 14     
 15     # Step 2: Reverse each row
 16     for i in range(n):
 17         matrix[i].reverse()
 18 
 19 
 20 # Test case 
 21 if __name__ == "__main__":
 22     matrix = [ 
 23         [1, 2, 3],
 24         [4, 5, 6],
 25         [7, 8, 9]
 26         ]
 27     
 28     rotate_2d_matrix(matrix)
 29     print(matrix)
