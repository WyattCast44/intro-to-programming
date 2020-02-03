# Header

"""
Week 5 Review - Part 2
Wyatt Castaneda
SWDV 600: INTRO TO PROGRAMMING
"""

# Problem 

"""
ou are working for a computer parts manufacturer that needs a new program to find sales information based on one of two pieces of information

- an invoice identifier (id) or
- a customer's last name (lname)

Your company logs each parts sale in an Excel file saved as a CSV file called `sales_data.csv` (NOTE: if you think no company would ever do this, you are incorrect: it has been done). The first line in that file contains the column headers: textual descriptions of what data is in each column. The columns are invoice id, a customer's first name, last name, part number, quantity, and total. 

Your goal is to make this file searchable. Your program should prompt the user for the following inputs, in this order:

- Whether they want to search using an invoice id (input of `id`) or by a customer's last name (input of `lname`). The program should reject any input that is not `id` or `lname`, forcing the user to choose one of those two options.
- The search term, either an `id` value or an `lname` value

After the user enters these inputs, the program should open the data file (note that the user does not input the data file), then search within the chosen column (i.e., either `id` or `lname`, but not both) for the input value. If the program finds a match in any invoice recrords, then it it should print (not save) all recorded invoices that match. Finally it should print the total number of records found that match the search term. 

Here are three examples:

Search by invoice id (id) or customer last name (lname)? firstname
ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search
Search by invoice id (id) or customer last name (lname)? lname
Enter your search term: Hutz
87681,Lionel,Hutz,218,1,50.83
34018,Lionel,Hutz,112,3,88.88
34018,Lionel,Hutz,386,3,86.04
34018,Lionel,Hutz,216,1,53.54
4 records found.

Search by invoice id (id) or customer last name (lname)? id
Enter your search term: 93303
93303,Frank,Grimes,392,2,90.74
93303,Frank,Grimes,142,3,73.2
93303,Frank,Grimes,353,1,45.87
3 records found.

Search by invoice id (id) or customer last name (lname)? lname
Enter your search term: Maryville
0 records found.

"""

# Solution

searchMethods = {
    "i": "invoice ID",
    "f": "first name",
    "l": "last name",
}

spacer = '\x20\x20\x20\x20\x20' 
tableHeader = f'\nID{spacer}First Name{spacer}Last Name{spacer}Part Number{spacer}Quantity{spacer}Total\n'
tableHeader = tableHeader + '---------------------------------------------------------------------------------'
tableFooter = '---------------------------------------------------------------------------------'
tableHeaderPositions = {
    'ID': tableHeader.find('ID'),
    'firstName': tableHeader.find('First Name'),
    'lastName': tableHeader.find('Last Name'),
    'partNumber': tableHeader.find('Part Number'),
    'quantity': tableHeader.find('Quantity'),
    'total': tableHeader.find('Total'),
}

def welcome():
    print('\nMaster Sales Program - v0.1.0')

def printSearchMethods():
    print('\nHow would you like to search?')
    print('-------------------------------')
    for key, term in searchMethods.items():
        print(f"- Enter '{key}' to search by {term}...")
    print('')

def promptForSearchMethod():
    printSearchMethods()

    method = input('> ')

    while not method in searchMethods:
        print(f"\nUnknown search method '{method}', please try again.")
        printSearchMethods()
        method = input('> ')

    return method

def promptForSearchTerm(method):
    print(f'\nEnter your search term: ({searchMethods[method]})')
    print('-------------------------------')
    return input('> ')

def openSalesData():
    return open('sales_data.csv')

def getSalesContents(fileObj):
    return fileObj.readlines()

def searchSales(term, sales, contents):
    matches = []

    for line in contents:
        if term in line:
            matches.append(line)
        
    return matches

def printResultsHeader():
    print(tableHeader)

def printResults(results):
    if len(results) == 0:
        print('\nNo results found!\n')
        return

    printResultsHeader()

    currentLine = ''

    for line in results:
        parts = line.split(',')
        for part in parts:
            currentLine = currentLine + f'{part}{spacer}'
        print(currentLine)

def main():
    method = promptForSearchMethod()
    term = promptForSearchTerm(method)
    sales = openSalesData()
    contents = getSalesContents(sales)
    sales.close()
    results = searchSales(term, sales, contents)
    printResults(results)

welcome()
main()