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