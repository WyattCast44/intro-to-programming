def spaces(num):
    return ('\x20' * num)

def printTable(headers, rows):
    header = formatTableHeader(headers)
    border = formatHeaderBorder(header)
    headerPositions = determineHeaderPositions(headers, header)
    lines = formatRows(rows, headerPositions)

    print(f'\n{header}\n{border}')

    for line in lines:
        print(line)
    
    print(border)

    print(f'Count: {len(lines)}')


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