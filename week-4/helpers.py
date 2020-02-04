class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def success(message):
    return color.GREEN + message + color.END

def error(message):
    return color.RED + message + color.END

def info(message):
    return color.YELLOW + message + color.END

def bold(message):
    return color.BOLD + message + color.END

def underlined(message):
    return color.UNDERLINE + message + color.END

def spaces(num):
    return ('\x20' * num)

def buildTable(headers, rows):
    header = formatTableHeader(headers)
    border = formatHeaderBorder(header)
    headerPositions = determineHeaderPositions(headers, header)
    lines = formatRows(rows, headerPositions)

    table = f'{header}\n{border}\n'

    for line in lines:
        table = table + line + '\n'
    
    table = table + border

    table = table + f'\nRows Count: {len(lines)}'

    return table


def formatTableHeader(headers):

    header = ''

    for item in headers:
        itemLen = len(item)
        header = header + f'{item}{spaces(itemLen + 3)}'

    return header

def formatHeaderBorder(header):
    return ('-' * len(header))

def determineHeaderPositions(headers, header):
    headerPositions = []

    for item in headers:
        headerPositions.append(header.find(item))

    return headerPositions

def formatRows(rows, headerPositions):
    lines = []

    for line in rows:
        loop = 0
        currentLine = ''
        parts = line.split(',')

        for column in parts:
            currentLine = currentLine.ljust(headerPositions[loop], spaces(1))
            currentLine = currentLine + column
            currentLine = currentLine.replace('\n', '')
            loop = loop + 1
        
        lines.append(currentLine)

    return lines

def dd(*payloads):
    for payload in list(payloads):
        print(payload)
    quit()