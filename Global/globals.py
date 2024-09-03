import os

CURRENT_PATH = os.getcwd()

def getNameOfFile(year: int, day: int) -> str:
    """
    Function used to get the path of the input file. Input files should be in a subfolder "textfiles", and named
    x.txt where is x is the number of the day. if 10 > x, write 0x (for example 03.txt for day 3).

    Args:
        year (int): Year when the problem was published.
        day (int): Day when the problem was published.
    
    Returns:
        String representing the path of the textfile.
    """
    return f"{CURRENT_PATH}\\Solution_{year}\\textFiles\\{day:02d}.txt"

def getLines(year: int, day: int) -> list[str]:
    """
    Function used to get the lists of strings in the input file.

    Args:
        year (int): Year when the problem was published.
        day (int): Day when the problem was published.
    
    Returns:
        A list of strings that contains the input of the problem.
    """
    lines: list[str]        # List of strings that contains the input of the problem.

    # Open the input file to retrieve the lines.
    with open(getNameOfFile(year, day), 'r') as file:
        lines = file.readlines()
    
    return lines

def getLine(year: int, day: int) -> str:
    """
    Function used to get the string in the input file.

    Args:
        year (int): Year when the problem was published.
        day (int): Day when the problem was published.
    
    Returns:
        A string that contains the input of the problem.
    """
    line: list[str]        # String that contains the input of the problem.

    # Open the input file to retrieve the line.
    with open(getNameOfFile(year, day), 'r') as file:
        line = file.readline()
    
    return line