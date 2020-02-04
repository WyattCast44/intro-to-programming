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

tableRows = []
tableRowsFormatted = []
tableHeaders = []
numberOfSalesHeaders = 2

def buildTableHeaders():
    for index in range(numberOfSalesHeaders):
        tableHeaders.append(f'Sale #{index + 1}')
    tableHeaders.append('Total')

def main():
    global numberOfSalesHeaders

    # Get the sales data
    data = open('17-oct-sales.txt')
    rows = data.readlines()
    data.close()
    
    # Parse the data
    for row in rows:

        # Split up the row into sales
        sales = row.split(' ')

        # Count how many sales this row contains
        salesCount = len(sales)

        # Make sure the sales headers count is updated
        if salesCount > numberOfSalesHeaders:
            numberOfSalesHeaders = salesCount

        # Convert row currency strings into sumable floats
        salesAmounts = [float(sale.replace('$', '')) for sale in sales] 

        # Determine the row total
        rowTotal = round(sum(salesAmounts), 2)

        # Append total to row
        salesAmounts.append(rowTotal)

        # Format back into strings with currency and join all columns by ','
        salesFormatted = ','.join([f'${sale}' for sale in salesAmounts])

        # Append these rows to the table rows
        tableRows.append(salesFormatted)

        ## TODO: Make sure that totals row is always pushed to the furthest end
    
    # Pad each row so that the totals column is always the last column
    for row in tableRows:
        
        # Split row into items
        sales = row.split(',')

        # Remove the total column
        total = sales.pop()

        # Determine the number of sales in row
        salesCount = len(sales)

        if salesCount < numberOfSalesHeaders:
            # Append empty spaces to row
            for index in range(numberOfSalesHeaders - salesCount):
                sales.append('')
        
        sales.append(total)

        salesFormatted = ','.join([sale for sale in sales])

        tableRowsFormatted.append(salesFormatted)

    buildTableHeaders()
    printTable(tableHeaders, tableRowsFormatted)

main()