## Task

There is an ant on an infinite coordinate grid. The ant can move 1 square up (x,y+1), down (x,y-1), left (x-1,y), right (x+1,y), one square per step. Cells in which the sum of the digits in the X coordinate plus the sum of the digits in the Y coordinate are greater than 25 are inaccessible to the ant. For example, a cell with coordinates (59, 79) is inaccessible because 5+9+7+9=30, which is more than 25. How many cells can an ant visit if its starting position is (1000,1000), (including the starting cell).

## Solution

- digit_sum function: This function takes an integer and returns the sum of its digits. It converts a number to a string, then each character in the string is converted back to an integer, and the numbers are summed.

- is_accessible function: This function takes x and y coordinates and checks whether the cell with these coordinates is accessible to the ant. To do this, it calls digit_sum for each coordinate and checks that the sum of the digits of the x and y coordinates does not exceed 25.

- count_accessible_cells function: This function takes the ant's starting coordinates (start_x, start_y) and uses breadth-first traversal to count the number of accessible cells starting from those coordinates.

A stack is created, to which the starting coordinates are added.
An empty visited set is created to keep track of cells that have already been visited.
A list of directions is created containing possible directions of movement: up, down, left and right.
While the stack is not empty:
We retrieve the coordinates (x, y) from the top of the stack.
If the cell with these coordinates has not been visited:
We add it to the set of visited ones.
If the cell is accessible (check using is_accessible), increase the accessible_cells counter by 1.
For each direction of movement:
We calculate new coordinates new_x and new_y.
We add them to the stack to check them in the next iterations.
Finally, we run count_accessible_cells with the ant's starting coordinates (1000, 1000) and print the result.

This algorithm efficiently finds all available cells starting from the given initial coordinates and counts their number.
