# Header

"""
Week 4 Review - Part 2
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
Write a program that takes some sales numbers from a file written as dollars (e.g., $1120.47), sums them across rows, and outputs the rows again with the sum at the end. For example for an input file named `17-oct-sales.txt` with these contents:

$1120.47 $944.42
$72.29 $588.23
$371.21 $2183.84
your program would output to another file the contents:

$ 1120.47  $  944.42  $ 2064.89
$   72.29  $  588.23  $  660.52
$  371.21  $ 2183.84  $ 2555.05
Notice how in the output file all the numbers are nicely formatted with right alignment. Hint: you will probably need to use splitting, string slicing, converting data types, and string formatting.

You program should prompt a user to input a file containing the sales numbers. Then prompt the user to enter a file name for outputting the sales numbers and their totals, formatted as indicated in the example above. Here is an example interaction:

Enter sales file name: 17-oct-sales.txt
Enter name for total sales file: 17-oct-totals.txt

Done writing totals to 17-oct-total.txt
"""

# Solution

from helpers import *

tableHeaders = [
    "Sale [NUMBER]",
    "Total"
]

def main():
    sales = open('17-oct-sales.txt').readlines().close()
    print(sales)

main()