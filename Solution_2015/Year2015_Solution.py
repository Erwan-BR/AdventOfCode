from Global.globals import getLines, getLine, getNameOfFile
from Solution.Solution import Solution
from re import split, findall
from hashlib import md5
import numpy as np
from sys import maxsize
from json import load

class Year2015_Solution(Solution):
    """
    Class containing the method for having solution of problems of year 2015.
    """

    year: int = 2015
    """
    Constant value that represents the year number. Used to find textfiles.
    """

    @staticmethod
    def getSolution(day: str, isFirstPart: bool):
        """
        Method to get solution of every day for which the solution is developped.
        Call the parent function with the corresponding arguments.
        """
        return Solution.getSolution(Year2015_Solution, Year2015_Solution.year, day, isFirstPart)

    @staticmethod
    def day_01_Part_1() -> int:
        """
        Get solution for day 1, Part 1:
        https://adventofcode.com/2015/day/1

        Returns:
            Integer representing the number of the floor where Santa ends.
        """
        floorNumber: int = 0    # Number of the floor where Santas is actually.
        line: str               # Input of the problem, stored on a string.
        instruction: str        # Instruction the Santa has to follow

        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 1)
        
        # For each instruction of the input, increase or decrease the floor number.
        for instruction in line:
            if '(' == instruction:
                floorNumber += 1
            elif ')' == instruction:
                floorNumber -= 1
        
        # Return the computed floor where Santa is at the end.
        return floorNumber

    @staticmethod
    def day_01_Part_2() -> int:
        """
        Get solution for day 1, Part 2
        https://adventofcode.com/2015/day/1#part2

        Returns:
            Integer representing the position of the first character that causes Santa to enter in basement.
        """
        indexOfCharacter: int = 0   # Index of the current character.
        floorNumber: int = 0        # Floor number where Santa is currently.
        line: str                   # Input of the problem, stored on a string.

        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 1)
        
        # For each instruction of the input, increase or decrease the floor number.
        for letter in line:
            indexOfCharacter += 1
            if '(' == letter:
                floorNumber += 1
            elif ')' == letter:
                floorNumber -= 1
                # If Santa reached the basement, returns the index of the current character.
                if -1 == floorNumber:
                        return indexOfCharacter
        
        # Return -1 if no character leads him to enter the basement. Should not occur on well-constructed inputs.
        return -1

    @staticmethod
    def day_02_Part_1() -> int:
        """
        Get solution for day 2, Part 1
        https://adventofcode.com/2015/day/2

        Returns:
            Integer representing the number of square feet needed to wrap the gifts.
        """
        squareFootWrapping: int = 0     # Number of square foot of wrapping paper needed.
        lines: list[str]                # All lines of the input of the problem.
        line: str                       # String representing the input and the dimension of each gift
        
        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 2)

        # For each set of dimensions, compute the needed wrapping paper and add it to the sum.
        for line in lines:
            dimensions = split("x", line)
            dimensions = [(int)(dimension) for dimension in dimensions]

            squareFootWrapping += 2 * (dimensions[0]*dimensions[1] + dimensions[1]*dimensions[2] + dimensions[0]*dimensions[2])
            squareFootWrapping += min(dimensions[0]*dimensions[1], dimensions[1]*dimensions[2], dimensions[0]*dimensions[2])

        # Return the number of square feet of wrapping paper needed.
        return squareFootWrapping

    @staticmethod
    def day_02_Part_2() -> int:
        """
        Get solution for day 2, Part 2
        https://adventofcode.com/2015/day/2#part2

        Returns:
            Integer representing the length of the ribbon needed.
        """
        lengthRibbon: int = 0     # Length of ribbon needed.
        lines: list[str]          # All lines of the input of the problem.
        line: str                 # String representing the input and the dimension of each gift
        
        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 2)

        # For each set of dimensions, compute the needed ribbon and add it to the sum.
        for line in lines:
            dimensions = split("x", line)
            dimensions = [(int)(dimension) for dimension in dimensions]

            lengthRibbon += np.prod(dimensions)
            lengthRibbon += 2 * (sum(dimensions))
            lengthRibbon -= 2 * max(dimensions)

        # Return the length of ribbon needed.
        return lengthRibbon
    
    @staticmethod
    def day_03_Part_1() -> int:
        """
        Get solution for day 3, Part 1
        https://adventofcode.com/2015/day/3

        Returns:
            Integer representing the number of house that receives at least one present.
        """
        currentCoordinates: list[int] = [0, 0]                                  # Coordinates of the Santa at a given iteration.
        visitedCoordinates: set[tuple[int]] = {(tuple)(currentCoordinates)}     # Coordinates of the houses that receives at least one present
        line: str                                                               # String representing the input
        
        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 3)
        
        # For each instruction, compute the new coordinate and add it to the set of visited coordinates
        for letter in line:
            if '<' == letter:
                currentCoordinates[0] -= 1
            elif '>' == letter:
                currentCoordinates[0] += 1
            elif '^' == letter:
                currentCoordinates[1] += 1
            elif 'v' == letter:
                currentCoordinates[1] -= 1
            visitedCoordinates.add((tuple)(currentCoordinates))
        
        # Return the number of houses visited by Santa
        return len(visitedCoordinates)
    
    @staticmethod
    def day_03_Part_2() -> int:
        """
        Get solution for day 3, Part 2
        https://adventofcode.com/2015/day/3#part2

        Returns:
            Integer representing the number of house that receives at least one present.
        """
        currentCoordinates: list[int] = [0, 0]                                # Coordinates of the Santa / Robo-Santa at a given iteration.
        visitedCoordinates: set[tuple[int]] = {(tuple)(currentCoordinates)}   # Coordinates of the houses visited by Santa or Robo-Santa.
        line: str                                                             # String representing the input

        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 3)
        
        
        # For each instruction for Santa, compute the new coordinate and add it to the set of visited coordinates
        for index in range(0, len(line), 2):
            if '<' == line[index]:
                currentCoordinates[0] -= 1
            elif '>' == line[index]:
                currentCoordinates[0] += 1
            elif '^' == line[index]:
                currentCoordinates[1] += 1
            elif 'v' == line[index]:
                currentCoordinates[1] -= 1
            visitedCoordinates.add((tuple)(currentCoordinates))
        
        # Re-init the coordinate to deal with Robo-Santa moovements
        currentCoordinates = [0, 0]

        # For each instruction for Robo-Santa, compute the new coordinate and add it to the set of visited coordinates
        for index in range(1, len(line), 2):
            if '<' == line[index]:
                currentCoordinates[0] -= 1
            elif '>' == line[index]:
                currentCoordinates[0] += 1
            elif '^' == line[index]:
                currentCoordinates[1] += 1
            elif 'v' == line[index]:
                currentCoordinates[1] -= 1
            visitedCoordinates.add((tuple)(currentCoordinates))

        # Return the number of houses visited
        return len(visitedCoordinates)
    
    @staticmethod
    def day_04_helper_findFirstWithNZerosWhenEncoded(input: str, numberOfZeros: int) -> int:
        """
        Helper for the solution for day 4. Find the first number to concatenate at the end of the input to have numberOfZeros when encoded.
        https://adventofcode.com/2015/day/4

        Returns:
            Integer representing the number of iterations to make before having numberOfZeros 0 at the beginning of the encoded string.
        
        Args:
            input (str): String that has to be followed by the output number, that we need to encode. 
            numberOfZeros (int): Number of Zeros at the beginning of the econded string we are looking for.
        """

        numberToConcatenate: int = 0        # Number at the end of the string
        
        # While we don't have numberOfZeros 0 at the beginning of the encoded string, continue with the next integer.
        while not md5(f"{input}{numberToConcatenate}".encode()).hexdigest().startswith("0" * numberOfZeros):
            numberToConcatenate += 1
        
        # Return the first integer that comply to the rules.
        return numberToConcatenate

    @staticmethod
    def day_04_Part_1() -> int:
        """
        Get solution for day 4, Part 1
        https://adventofcode.com/2015/day/4

        Returns:
            Integer representing the number of iterations to make before having 5 0 at the beginning of the encoded string.
        """
        numberToConcatenate: int            # Number at the end of the string
        line: str                           # String representing the input
        
        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 4)
        
        # Retrieve the number that should be concatenated at the end thanks to the helper function.
        numberToConcatenate = Year2015_Solution.day_04_helper_findFirstWithNZerosWhenEncoded(line, 5)

        # Return the smallest integer allows to start by 5 zeros when md5-encoded.
        return numberToConcatenate
    
    @staticmethod
    def day_04_Part_2() -> int:
        """
        Get solution for day 4, Part 2
        https://adventofcode.com/2015/day/4#part2

        Returns:
            Integer representing the number of iterations to make before having 6 Zeros at the beginning of the encoded string.
        """
        numberToConcatenate: int            # Number at the end of the string
        line: str                           # String representing the input
        
        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 4)

        
        # Retrieve the number that should be concatenated at the end thanks to the helper function.
        numberToConcatenate = Year2015_Solution.day_04_helper_findFirstWithNZerosWhenEncoded(line, 6)

        # Return the smallest integer allows to start by 6 zeros when md5-encoded.
        return numberToConcatenate
    
    @staticmethod
    def day_05_Part_1() -> int:
        """
        Get solution for day 5, Part 1
        https://adventofcode.com/2015/day/5

        Returns:
            Integer representing the number of nice strings.
        """
        numberOfNiceString: int = 0                             # Number of nice strings found.
        listOfNaughty: list[str] = ["ab", "cd", "pq", "xy"]     # Set containing the naughty characters that should not be in the string.
        listOfVowels: list[str] = ['a', 'e', 'i', 'o', 'u']     # Set containing the different vowels.
        lines: list[str]                                        # All lines of the input of the problem.
        line: str                                               # String representing the input and the strings that might be nine.

        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 5)

        
        # Iterating among all string and check if they respect the condition.
        for line in lines:
            numberOfVowels: int = 0
            isContainingDouble: bool = False
            isContainingNaughtyElement: bool = False
            
            # Check if first letter is a vowel.
            if line[0] in listOfVowels:
                numberOfVowels += 1

            # Iterating among all pair of letter (starting by one)
            for indexOfLetter in range(1, len(line)):
                
                # Check if the pair is naughty
                if line[indexOfLetter - 1: indexOfLetter + 1] in listOfNaughty:
                    isContainingNaughtyElement = True
                    break
                
                # Check if we found at least one double
                if line[indexOfLetter] == line[indexOfLetter - 1]:
                    isContainingDouble = True
                
                # Check if the letter is a vowel.
                if line[indexOfLetter] in listOfVowels:
                    numberOfVowels += 1

            # If all condition are met, we can increment by one the number of nice strings.
            if isContainingDouble and (3 <= numberOfVowels) and not isContainingNaughtyElement:
                numberOfNiceString += 1

        # Return the number of string that are nice.
        return numberOfNiceString
    
    @staticmethod
    def day_05_Part_2() -> int:
        """
        Get solution for day 5, Part 2
        https://adventofcode.com/2015/day/5#part2

        Returns:
            Integer representing the number of nice strings.
        """
        numberOfNiceString: int = 0                             # Number of nice strings found.
        lines: list[str]                                        # All lines of the input of the problem.
        line: str                                               # String representing the input and the strings that might be nine.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 5)

        # Iterating among all string and check if they respect the condition.
        for line in lines:
            pairOfConsecutiveLetters: dict[str, int] = dict()
            isPaternTwiceNotOverlapping: bool = False
            isRepeatedWithOneSpace: bool = False
            
            # Check if a letter is reated with a letter in the middle of them.
            for indexOfLetter in range(2, len(line)):
                if line[indexOfLetter] == line[indexOfLetter - 2]:
                    isRepeatedWithOneSpace = True
                    break
            
            # Check if a pair of two non-overlapping letters is in the string
            for indexOfLetter in range(1, len(line)):
                currentSubstring: str = line[indexOfLetter - 1: indexOfLetter + 1]
                
                if currentSubstring not in pairOfConsecutiveLetters:
                    pairOfConsecutiveLetters[currentSubstring] = indexOfLetter - 1
                
                elif pairOfConsecutiveLetters[currentSubstring] != (indexOfLetter - 2):
                    isPaternTwiceNotOverlapping = True
                    break

            # If all condition are met, we can increment by one the number of nice strings.
            if isRepeatedWithOneSpace and isPaternTwiceNotOverlapping:
                numberOfNiceString += 1

        # Return the number of string that are nice.
        return numberOfNiceString
    
    @staticmethod
    def day_06_Part_1() -> int:
        """
        Get solution for day 6, Part 1
        https://adventofcode.com/2015/day/6

        Returns:
            Integer representing the number of lights are lit.
        """
        lightsGrid: list[int] = [[0 for _ in range(1000)] for _ in range(1000)]     # Grid that contains the lights information
        lines: list[str]                                                            # All lines of the input of the problem.
        line: str                                                                   # String representing the input and the strings that might be nine.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 6)

        # Iterating among all instructions
        for line in lines:
            # Retrieve the integers values
            numbers = findall(r'\b\d+\b', line)
            numbers = [int(e) for e in numbers]

            # Switch on all lights on the rectangle
            if line.startswith("turn on"):
                for i in range(numbers[0], numbers[2] + 1):
                    for j in range(numbers[1], numbers[3] + 1):
                        lightsGrid[i][j] = 1
            # Switch off all lights on the rectangle
            elif line.startswith("turn off"):
                for i in range(numbers[0], numbers[2] + 1):
                    for j in range(numbers[1], numbers[3] + 1):
                        lightsGrid[i][j] = 0
            # Toggle all lights on the rectangle
            elif line.startswith("toggle"):
                for i in range(numbers[0], numbers[2] + 1):
                    for j in range(numbers[1], numbers[3] + 1):
                        lightsGrid[i][j] = 1 - lightsGrid[i][j]
        
        # Compute the number of lights that are on.
        return sum(sum(lightsGrid[i]) for i in range(1000))
    
    @staticmethod
    def day_06_Part_2() -> int:
        """
        Get solution for day 6, Part 2
        https://adventofcode.com/2015/day/6#part2

        Returns:
            Integer representing the total brightness.
        """
        lightsGrid: list[int] = [[0 for _ in range(1000)] for _ in range(1000)]     # Grid that contains the lights information
        lines: list[str]                                                            # All lines of the input of the problem.
        line: str                                                                   # String representing the input and the strings that might be nine.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 6)

        # Iterating among all instructions
        for line in lines:
            # Retrieve the integers values
            numbers = findall(r'\b\d+\b', line)
            numbers = [int(e) for e in numbers]

            # Increase the brightness on the rectangle
            if line.startswith("turn on"):
                for i in range(numbers[0], numbers[2] + 1):
                    for j in range(numbers[1], numbers[3] + 1):
                        lightsGrid[i][j] += 1
            # Decrease the brightness on the rectangle
            elif line.startswith("turn off"):
                for i in range(numbers[0], numbers[2] + 1):
                    for j in range(numbers[1], numbers[3] + 1):
                        lightsGrid[i][j] = max(0, lightsGrid[i][j] - 1)
            # Increase two times the brightness on the rectangle
            elif line.startswith("toggle"):
                for i in range(numbers[0], numbers[2] + 1):
                    for j in range(numbers[1], numbers[3] + 1):
                        lightsGrid[i][j] += 2
        
        # Compute the total brightness.
        return sum(sum(lightsGrid[i]) for i in range(1000))
    
    @staticmethod
    def day_07_helper_getDictAndOperations() -> tuple[dict[str, int], list[tuple[str, str, str, str]]]:
        """
        Helper for the solution for day 7. Construct dictionnaries of wires and the list of all the operations.
        https://adventofcode.com/2015/day/7

        Returns:
            A tuple containing two elements:
                - A dictionnary. Keys: Name of wire / integer: Both are strings. Values: Value of the signal in the key.
                - A tuple containing 4 elements:
                    - 0 and 2 are the input of the operation.
                    - 1 is the string reprenseting the operation.
                    - 3 is the output wire.
        """
        dictOfValues: dict[str, int] = {}                   # First part of the output.
        operations: list[tuple[str, str, str, str]] = []    # Second part of the output
        patternString: str = r"\b[a-zA-Z0-9]+\b"            # Patterns for finding the elements of the operation in each line
        lines: list[str]                                    # All lines of the input of the problem.
        line: str                                           # String representing the input and the strings that might be nine.
        tabOfVal: list[str]                                 # Table that will contains the elements of the REGEX.
        
        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 7)
            
        # Retrieve every operations that needs to be done.
        for line in lines:

            # Retrieve the operation
            tabOfVal = findall(patternString, line)

            # len 2 is only for direct afectation
            if 2 == len(tabOfVal):
                # If the first value is numeric, then we can store the value of the wire in the dict.
                if tabOfVal[0].isnumeric():
                    dictOfValues[tabOfVal[1]] = int(tabOfVal[0])
                
                # Else, both wire should be saved (if not done) in the dict to make the equal latter.
                else:
                    operations.append((tabOfVal[0], "EQUAL", "", tabOfVal[1]))
                    if tabOfVal[0] not in dictOfValues:
                        dictOfValues[tabOfVal[0]] = -1
                    if tabOfVal[1] not in dictOfValues:
                        dictOfValues[tabOfVal[1]] = -1
            
            # len 3 is only when a NOT operator is done.
            # Both wire should be saved (if not done) in the dict to make the not latter.
            elif 3 == len(tabOfVal):
                operations.append((tabOfVal[1], "NOT", "" , tabOfVal[2]))
                if tabOfVal[1] not in dictOfValues:
                        dictOfValues[tabOfVal[1]] = -1
                if tabOfVal[2] not in dictOfValues:
                        dictOfValues[tabOfVal[2]] = -1
            
            # len 4 is for all other operators: AND, OR, LSHIFT, RSHIFT
            # Wires should be saved (if not done) in the dict to make the operator latter.
            else :
                operations.append(tuple(tabOfVal))
                if tabOfVal[0] not in dictOfValues:
                    dictOfValues[tabOfVal[0]] = int(tabOfVal[0]) if tabOfVal[0].isnumeric() else -1
                if tabOfVal[2] not in dictOfValues:
                    dictOfValues[tabOfVal[2]] = int(tabOfVal[2]) if tabOfVal[2].isnumeric() else -1
                if tabOfVal[3] not in dictOfValues:
                    dictOfValues[tabOfVal[3]] = -1
        
        return (dictOfValues, operations)

    @staticmethod
    def day_07_helper_findValueOfWireA(dictOfValues: dict[str, int], operations: list[tuple[str, str, str, str]]) -> int:
        """
        Helper for the solution for day 7. Compute the different operations while the value of wire A is not found.
        https://adventofcode.com/2015/day/7

        Args:
            - dictOfValues (dict[str, int]): Dictionnary containing all wire and their values
            - operations (list[tuple[str, str, str, str]]): List of tuple containing all operations that needs to be done.
        Returns:
            Value of the Wire A as soon as we got it.
        """

        dictOfValuesLocal: dict[str, int] = dictOfValues.copy()                 # Copy of the dict, to avoid overwritting values
        operationsLocal: list[tuple[str, str, str, str]] = operations[:]        # Copy of the operation, to avoid delete the needed operation
        
        functionsMap = {"AND": lambda a, b: a & b,                              # Map of the function, that allows to take a string and make the
                        "OR": lambda a, b: a ^ b,                               # corresponding operation
                        "LSHIFT": lambda a, b: a << b,
                        "RSHIFT": lambda a, b: a >> b}

        # While the value of the Wire a is not found, we iterate among all operations to make those that are possible
        while -1 == dictOfValuesLocal["a"]:
            for operationIndex in range(len(operationsLocal) -1, -1, -1):
                
                # NOT and EQUAL operations only
                if "" == operationsLocal[operationIndex][2]:
                    if -1 != dictOfValuesLocal[operationsLocal[operationIndex][0]]:
                        if "NOT" == operationsLocal[operationIndex][1]:
                            dictOfValuesLocal[operationsLocal[operationIndex][3]] = 65535 - dictOfValuesLocal[operationsLocal[operationIndex][0]]
                        elif "EQUAL" == operationsLocal[operationIndex][1]:
                            dictOfValuesLocal[operationsLocal[operationIndex][3]] = dictOfValuesLocal[operationsLocal[operationIndex][0]]
                        
                        del operationsLocal[operationIndex]
                
                # All other operations: OR, AND, LSHIFT, RSHIFT. Use the operation declared in functionsMap
                elif -1 != dictOfValuesLocal[operationsLocal[operationIndex][0]] and -1 != dictOfValuesLocal[operationsLocal[operationIndex][2]] :
                    if operationsLocal[operationIndex][1] in ("AND", "OR", "LSHIFT", "RSHIFT"):
                        dictOfValuesLocal[operationsLocal[operationIndex][3]] = functionsMap[operationsLocal[operationIndex][1]](dictOfValuesLocal[operationsLocal[operationIndex][0]], dictOfValuesLocal[operationsLocal[operationIndex][2]])
                    
                    del operationsLocal[operationIndex]
        
        return dictOfValuesLocal["a"]
    
    @staticmethod
    def day_07_Part_1() -> int:
        """
        Get solution for day 7, Part 1
        https://adventofcode.com/2015/day/7

        Returns:
            Integer representing the value of the signal in the wire A.
        """
        dictOfValues: dict[str, int]                                                        # Dict containing the information of all wires.
        operations: list[tuple[str, str, str, str]]                                         # List of all the operations given in the input.
        outputOfA: int                                                                      # Value returned by the helper function.

        # Retrieve dict and list from the helper function
        dictOfValues, operations = Year2015_Solution.day_07_helper_getDictAndOperations()

        # Compute the value of the wires until the value of A is found
        outputOfA = Year2015_Solution.day_07_helper_findValueOfWireA(dictOfValues, operations)

        # Return the value of the wire A
        return outputOfA
    
    @staticmethod
    def day_07_Part_2() -> int:
        """
        Get solution for day 7, Part 2
        https://adventofcode.com/2015/day/7#part2

        Returns:
            Integer representing the value of the signal in the wire A after 2 iteration (value of A overwrite the value of B).
        """
        dictOfValues: dict[str, int]                                                        # Dict containing the information of all wires.
        operations: list[tuple[str, str, str, str]]                                         # List of all the operations given in the input.
        outputOfA: int                                                                      # Value returned by the helper function.

        # Retrieve dict and list from the helper function
        dictOfValues, operations = Year2015_Solution.day_07_helper_getDictAndOperations()

        # Compute the value of the wires until the value of A is found
        outputOfA = Year2015_Solution.day_07_helper_findValueOfWireA(dictOfValues, operations)

        # Overwrite the value of wire B and reset the value of A
        dictOfValues["b"] = outputOfA
        
        # Compute the value of the wires until the value of A is found
        outputOfA = Year2015_Solution.day_07_helper_findValueOfWireA(dictOfValues, operations)

        # Return the value of the wire A
        return outputOfA
    
    @staticmethod
    def day_08_Part_1() -> int:
        """
        Get solution for day 8, Part 1
        https://adventofcode.com/2015/day/8

        Returns:
            Integer representing the number of character that are done for coding but not present in litteral.
        """
        numberCharacterOfCode: int = 0      # Number of character that are written in the code
        numberCharacterLitteral: int = 0    # Number of character that it represents.
        currentNumberCharacter: int         # Number of character by line.
        lines: list[str]                    # All lines of the input of the problem.
        line: str                           # String representing the input and the strings that might be nine.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 8)
        lines = [line.strip() for line in lines]

        # Iterating among all strings
        for line in lines:

            # Retrieve the number of character on the line, add it to the code
            # And delete 2 for Litteral for the first and last "
            currentNumberCharacter = len(line)
            numberCharacterOfCode += currentNumberCharacter
            numberCharacterLitteral += currentNumberCharacter - 2

            # Iterating among all letters
            charIndex: int = 0
            while charIndex < len(line):
                # If we find a \ character, it means that there are more characters for code than litteral
                if "\\" == line[charIndex]:
                    # If the next one is a \ or a ", there are 2 characters of code for 1 litteral
                    if line[charIndex + 1] in ("\"", "\\"):
                        numberCharacterLitteral -= 1
                        charIndex += 1
                    # If the next one is a #, there are 4 characters of code for 1 litteral
                    elif "x" == line[charIndex + 1]:
                        numberCharacterLitteral -= 3
                        charIndex += 3
                charIndex += 1

        # Return the number of characters that are done for code only.
        return numberCharacterOfCode - numberCharacterLitteral

    @staticmethod
    def day_08_Part_2() -> int:
        """
        Get solution for day 8, Part 2
        https://adventofcode.com/2015/day/8#part2

        Returns:
            Integer representing the number of character should be added if we want to have the code in an encoded.
        """
        numberCharacterOfCode: int = 0      # Number of character that are written in the code
        numberCharacterEncoded: int = 0     # Number of character that it would be once encoded.
        currentNumberCharacter: int         # Number of character by line.
        lines: list[str]                    # All lines of the input of the problem.
        line: str                           # String representing the input and the strings that might be nine.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 8)
        lines = [line.strip() for line in lines]

        # Iterating among all strings
        for line in lines:
            # Retrieve the number of character on the line, add it to the code
            # And add 4 for encoded for the first and last "
            currentNumberCharacter = len(line)
            numberCharacterOfCode += currentNumberCharacter
            numberCharacterEncoded += currentNumberCharacter + 4

            # Each time a \\ or a \" is found, add 1 character for encoding.
            for charIndex in range(1, len(line) - 1):
                if line[charIndex] in ("\\", "\""):
                    numberCharacterEncoded += 1

        # Return the number of character added for the encoding.
        return numberCharacterEncoded - numberCharacterOfCode
    
    day_09_distanceSolution: int = maxsize

    @staticmethod
    def day_09_helper_dfs(listOfVisitedCities: list[int], matrixOfDistances: list[list[int]], currentDistance: int, isMin: bool) -> None:
        """
        Helper for the solution for day 9. Use DFS to find the smallest distance.
        https://adventofcode.com/2015/day/9

        Args:
            - listOfVisitedCities (list[int]): List of all cities that has been visited in the current path.
            - matrixOfDistances (list[list[int]]): Distance between every cities.
            - currentDistance (int): Distance travelled for the current path.
            - isMin (bool): True if the MIN function is applied, FALSE if the MAX function is applied.
        """
        indexOfCity: int            # Index of the cities that we are looking for minimizing distances.
        
        # Iterating among all cities to find the next one that Santa is going to visit.
        for indexOfCity in range(len(matrixOfDistances)):
            # If the city is visited, we don't want to go in this one anymore.
            if indexOfCity in listOfVisitedCities:
                continue

            # Add the city to the list of visited cities. Add the distance to the current distance.
            listOfVisitedCities.append(indexOfCity)
            currentDistance += matrixOfDistances[listOfVisitedCities[-2]][listOfVisitedCities[-1]]
            
            # If all cities are visited, we can try saving the new distance.
            if len(matrixOfDistances) == len(listOfVisitedCities):
                if isMin:
                    Year2015_Solution.day_09_distanceSolution = min(Year2015_Solution.day_09_distanceSolution, currentDistance)
                else:
                    Year2015_Solution.day_09_distanceSolution = max(Year2015_Solution.day_09_distanceSolution, currentDistance)
            
            # If we want the min distance, we want to continue only if the distance is smaller than the one we already have.
            elif isMin:
                if Year2015_Solution.day_09_distanceSolution > currentDistance:
                    Year2015_Solution.day_09_helper_dfs(listOfVisitedCities, matrixOfDistances, currentDistance, isMin)
            # Else, we want the max so we always keep doing dfs
            else:
                Year2015_Solution.day_09_helper_dfs(listOfVisitedCities, matrixOfDistances, currentDistance, isMin)
            
            # Delete the last path and substract the useless distance.
            currentDistance -= matrixOfDistances[listOfVisitedCities[-2]][listOfVisitedCities[-1]]
            listOfVisitedCities.pop()
            
    @staticmethod
    def day_09_helper_buildMatrixOfDistances() -> list[list[int]]:
        """
        Helper for the solution for day 9. Construct the distance matrix between each places. 
        https://adventofcode.com/2015/day/9

        Returns:
            - matrixOfDistances (list[list[int]]): Distance between every cities.
        """
        dictOfCitiesAndIndex: dict[str, int] = {}       # Dictionary to find where the distances should be written in matrix.
        lastIndex: int = 0                              # Integer to map name of cities to index.
        matrixOfDistances: list[list[int]]              # Output: Matrix of the distances between each cities.
        lines: list[str]                                # All lines of the input of the problem.
        line: str                                       # String representing the input line by line.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 9)
        
        # Construct the dict to know which city correspond to which path
        for line in lines:
            strings = findall(r"\b[a-zA-Z]+\b", line)
            if strings[0] not in dictOfCitiesAndIndex:
                dictOfCitiesAndIndex[strings[0]] = lastIndex
                lastIndex += 1
            if strings[2] not in dictOfCitiesAndIndex:
                dictOfCitiesAndIndex[strings[2]] = lastIndex
                lastIndex += 1
        
        # Fill a matrix with INFINITE distances
        matrixOfDistances = [[maxsize for _ in range(lastIndex)] for _ in range(lastIndex)]

        # Distance for going from a place to the same place is 0.
        for lineOfMatrix in range(len(matrixOfDistances)):
            matrixOfDistances[lineOfMatrix][lineOfMatrix] = 0

        # Retrieve the given distances.
        for line in lines:
            strings = findall(r"\b[a-zA-Z]+\b", line)
            distance = int(findall(r"\b[0-9]+\b", line)[0])

            matrixOfDistances[dictOfCitiesAndIndex[strings[0]]][dictOfCitiesAndIndex[strings[2]]] = distance
            matrixOfDistances[dictOfCitiesAndIndex[strings[2]]][dictOfCitiesAndIndex[strings[0]]] = distance
        
        # Return the matrix with all distances
        return matrixOfDistances

    @staticmethod
    def day_09_Part_1() -> int:
        """
        Get solution for day 9, Part 1
        https://adventofcode.com/2015/day/9

        Returns:
            Distance of the shortest route Santa can take to go through all locations.
        """
        matrixOfDistances: list[list[int]]  # Matrix containing all the distances between every locations
        
        # Set the solution to max value to make the comparaison logical with min function
        Year2015_Solution.day_09_distanceSolution = maxsize

        # Retrieve the matrix thanks to the helper function
        matrixOfDistances = Year2015_Solution.day_09_helper_buildMatrixOfDistances()
        
        # Find the smallest route by starting from each cities.
        for indexCity in range(len(matrixOfDistances)):
            Year2015_Solution.day_09_helper_dfs([indexCity], matrixOfDistances, 0, True)

        # Return the smallest path found
        return Year2015_Solution.day_09_distanceSolution
    
    @staticmethod
    def day_09_Part_2() -> int:
        """
        Get solution for day 9, Part 2
        https://adventofcode.com/2015/day/9#part2

        Returns:
            Distance of the longest route Santa can take to go through all locations.
        """
        matrixOfDistances: list[list[int]]  # Matrix containing all the distances between every locations

        # Set the solution to min value to make the comparaison logical with max function
        Year2015_Solution.day_09_distanceSolution = 0

        # Retrieve the matrix thanks to the helper function
        matrixOfDistances = Year2015_Solution.day_09_helper_buildMatrixOfDistances()
        
        # Find the longest route by starting from each cities.
        for indexStart in range(len(matrixOfDistances)):
            Year2015_Solution.day_09_helper_dfs([indexStart], matrixOfDistances, 0, False)
        
        # Return the longest path found
        return Year2015_Solution.day_09_distanceSolution
    
    @staticmethod
    def day_10_helper_getLookAndSayLengthAfterOccurences(numberOfOccurences: int) -> int:
        """
        Helper for the solution for day 10. Find the length of the message of look-and-say after a given number of iterations.
        https://adventofcode.com/2015/day/10

        Returns:
            Length of the string after numberOfOccurences play of look-and-say.
        
        Args:
            numberOfOccurences (int): Number of game the Elves will play.
        """
        line: str                           # Input of the problem, stored on a string.
        charIndex: int                      # Index of the instruction the Santa has to follow
        newReadValue: str                   # New version of what is read by the elves at step n
        numberOfOccurenceLastDigit: int     # Number of time the last integer is written
        
        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 10)

        # Play the game numberOfOccurences times
        for _ in range(numberOfOccurences):
            newReadValue = ""
            numberOfOccurenceLastDigit = 1
            
            # Iterating among all value written in the string.
            for charIndex in range(1, len(line)):
                # If we see the same character as before, we say it and add it to the string
                if line[charIndex] == line[charIndex - 1]:
                    numberOfOccurenceLastDigit += 1
                # Else, keep counting the same character
                else:
                    newReadValue += str(numberOfOccurenceLastDigit) + line[charIndex - 1]
                    numberOfOccurenceLastDigit = 1
            
            # The elves has to say the last character they see.
            newReadValue += str(numberOfOccurenceLastDigit) + line[-1]

            # Update the content of the input for next iteration
            line = newReadValue
        
        # Return the number of characters in the sentence said by the elves after numberOfOccurences games.
        return len(line)
    
    @staticmethod
    def day_10_Part_1() -> int:
        """
        Get solution for day 10, Part 1
        https://adventofcode.com/2015/day/10

        Returns:
            Numbers of elements in the string after the Elves made 40 games of look-and-say.
        """
        solutionAfterFortyGames: int = Year2015_Solution.day_10_helper_getLookAndSayLengthAfterOccurences(40)  # Length of the string after 40 games of look-and-say
        
        return solutionAfterFortyGames
    
    @staticmethod
    def day_10_Part_2() -> int:
        """
        Get solution for day 10, Part 2
        https://adventofcode.com/2015/day/10#part2

        Returns:
            Numbers of elements in the string after the Elves made 50 games of look-and-say.
        """
        solutionAfterFiftyGames: int = Year2015_Solution.day_10_helper_getLookAndSayLengthAfterOccurences(50)  # Length of the string after 40 games of look-and-say

        return solutionAfterFiftyGames
    
    @staticmethod
    def day_11_helper_doesStringContainsIncreasingSubsequence(stringToCheck: str) -> bool:
        """
        Helper for the solution for day 11. Check if a string contains at least one increasing subsequence between 3 consecutive chars.
        https://adventofcode.com/2015/day/11

        Returns:
            Booleans that states if the string contains an increasing subsequence of 3 consecutives characters.
        
        Args:
            stringToCheck (str): String where we check if it contains an increasing subsequence of 3 consecutives characters.
        """
        # Boolean to check the presence of any subsequence
        isIncreasingSubsequence: bool = any(ord(stringToCheck[charIndex - 2]) == (ord(stringToCheck[charIndex - 1]) - 1) \
            and ord(stringToCheck[charIndex - 1]) == (ord(stringToCheck[charIndex]) - 1) for charIndex in range(2, len(stringToCheck)))

        return isIncreasingSubsequence
    
    @staticmethod
    def day_11_helper_doesStringContainsTwoPairs(stringToCheck: str) -> bool:
        """
        Helper for the solution for day 11. Check if the string contains 2 non-overlapping pair of letters.
        https://adventofcode.com/2015/day/11

        Returns:
            Booleans that states if the string contains 2 non-overlapping pair of letters.
        
        Args:
            stringToCheck (str): String where we check if it contains 2 non-overlapping pair of letters.
        """
        charIndex:int = 1                   # Index of the char that we are looking at on the input string.
        numberOfPairOfLetters: int = 0      # Number of non-overlapping pair of characters.

        # Iterate among all indexes
        while charIndex < len(stringToCheck):
            # If the char are the same, we increment the number of pairs of letters
            if stringToCheck[charIndex] == stringToCheck[charIndex - 1]:
                numberOfPairOfLetters += 1
                
                # If we already have 2 non-overlapping pair, we can return True
                if 2 == numberOfPairOfLetters:
                    return True
                
                # Increase by one the index to avoid considering 'aaa' as 2 pairs.
                charIndex += 1
            
            # Go to next index to check another pair.
            charIndex += 1
        
        # 2 non-overlapping pairs are not found in the string.
        return False

    @staticmethod
    def day_11_helper_IncrementByOneFromIndex(currentPassword: str, charIndex: int) -> str:
        """
        Helper for the solution for day 11. Increment by one a given index to have another Password.
        https://adventofcode.com/2015/day/11

        Handles:
            If we have a 'z' to increment, it will be replaced by 'a' and the previous is incremented.
            If all letters to increment where 'z', they are replaced by 'a' and an 'a' is added at the beginning.
            If we have a forbidden letter, we update it.
        
        Returns:
            The password with an update at the charIndex.
        
        Args:
            currentPassword (str): Password that has to be incremented.
            charIndex (int): Index of the letter to increment.
        """

        # While we found 'z' in the Password', we have to place it to 'a' and go to the previous letter to increment
        while "z" == currentPassword[charIndex]:
            currentPassword = currentPassword[:charIndex] + "a" + currentPassword[charIndex + 1:]
            charIndex -= 1

            # If all letters from 0 to charIndex were z, like 'zzzbb' and charIndex = 1, the next one should be 'aaaazbb'
            if -1 == charIndex:
                currentPassword = "a" + currentPassword
                return currentPassword
        
        # Replace the current index to the next one in the alphabetical order
        currentPassword = currentPassword[:charIndex] + chr(ord(currentPassword[charIndex]) + 1) + currentPassword[charIndex + 1:]
        
        # Replace forbidden letters
        currentPassword = Year2015_Solution.day_11_helper_replaceForbiddenLetter(currentPassword)

        # Return the next passowrd in the alphabetical order, while replacing the forbidden characters.
        return currentPassword
    
    @staticmethod
    def day_11_helper_replaceForbiddenLetter(currentPassword: str) ->str:
        """
        Helper for the solution for day 11. Replace the forbidden letters to the one after in the alphabtical order.
        https://adventofcode.com/2015/day/11

        Returns:
            Password with forbidden letters replaced. 
        
        Args:
            currentPassword (str): Password with letters that may be illegal.
        """
        # Because the password can't contain 'i', 'l', or 'o', we can place those values to the next in the alphabetical order. 
        currentPassword = currentPassword.replace('i', 'j')
        currentPassword = currentPassword.replace('l', 'm')
        currentPassword = currentPassword.replace('o', 'p')

        # Return the password without forbidden letters
        return currentPassword

    @staticmethod
    def day_11_helper_findFollowingPassword(currentPassword: str) -> str:
        """
        Helper for the solution for day 11. Find the next password when we already know the current one.
        https://adventofcode.com/2015/day/11

        Returns:
            New Santa's password.
        
        Args:
            currentPassword (str): Password that Santa forgot.
        """
        charIndex: int      # Index of the letter in the password that will help to increment the password to another one.

        # Replace forbidden letters
        currentPassword = Year2015_Solution.day_11_helper_replaceForbiddenLetter(currentPassword)
        
        # While a valid password is not found, we have to search for a new one.
        while (True):
            
            # If the password is valid, we can stop searching for another one.
            if Year2015_Solution.day_11_helper_doesStringContainsIncreasingSubsequence(currentPassword) \
            and Year2015_Solution.day_11_helper_doesStringContainsTwoPairs(currentPassword):
                break
            
            # Start from the last index.
            charIndex = len(currentPassword) - 1

            # If the last letter is the same as the next one, we just increment. The idea is to try to make a increasing subsequence.
            if currentPassword[charIndex] == currentPassword[charIndex - 1]:
                currentPassword = Year2015_Solution.day_11_helper_IncrementByOneFromIndex(currentPassword, charIndex)
            
            # Else, if the last letter is before, we change the last letter to it equal to the previous one to have a new pair.
            elif ord(currentPassword[charIndex]) < ord(currentPassword[charIndex - 1]):
                currentPassword = currentPassword[:charIndex] + currentPassword[charIndex - 1] + currentPassword[charIndex + 1:]
            
            # Else, the last letter is greater than the previous (for example 'bc')
            # At this moment, we increment the one before to have 'cc' and then create a new pair.
            else:
                charIndex -= 1
                currentPassword = Year2015_Solution.day_11_helper_IncrementByOneFromIndex(currentPassword, charIndex)
                currentPassword = currentPassword[:-1] + currentPassword[-2]
        
        # Return the next password of Santa.
        return currentPassword   

    @staticmethod
    def day_11_Part_1() -> int:
        """
        Get solution for day 11, Part 1
        https://adventofcode.com/2015/day/11

        Returns:
            The next password that Santa should have following the rules of the Security-Elf
        """
        line: str               # Input of the problem, which is the previous password of Santa.

        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 11)
        
        # Retrieve the next password
        line = Year2015_Solution.day_11_helper_findFollowingPassword(line)

        # Return the new password of Santa
        return line

    @staticmethod
    def day_11_Part_2() -> str:
        """
        Get solution for day 11, Part 2
        https://adventofcode.com/2015/day/11#part2

        Returns:
            The password of Santa updated 2 times, according to the new Security-Elf rules.
        """
        line: str               # Input of the problem, which is the previous password of Santa.

        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 11)

        # Find the next password of Santa
        line = Year2015_Solution.day_11_helper_findFollowingPassword(line)

        # Increment by one the password before finding a new password
        line = Year2015_Solution.day_11_helper_IncrementByOneFromIndex(line, len(line) - 1)

        # Find the next password of Santa
        line = Year2015_Solution.day_11_helper_findFollowingPassword(line)

        # Return the updated password of Santa
        return line
    
    @staticmethod
    def day_12_helper_computeSumInsideDict(dictToComputeSum: dict) -> int:
        """
        Helper for the solution for day 12. Compute the sum inside a dict, without counting elements if "red" is a value.
        https://adventofcode.com/2015/day/12

        Returns:
            Sum of all elements inside the dict that should be counted. If "red" is a value, the output is 0.
        
        Args:
            dictToComputeSum (dict): Dictionarry that represents a JSON element.
        """
        totalSum: int = 0       # Sum of all elements inside the dict.

        for _, value in dictToComputeSum.items():
            # If the value is an integer, we can add it to the sum.
            if type(value) is int:
                totalSum += value
            # If the value is a string, we have to return 0 if the value is "red".
            if type(value) is str:
                if "red" == value:
                    return 0
            # If the value is a dict, we add the inner dict sum.
            if type(value) is dict:
                totalSum += Year2015_Solution.day_12_helper_computeSumInsideDict(value)
            # If the value is a list, we add the inner list sum.
            if type(value) is list:
                totalSum += Year2015_Solution.day_12_helper_computeSumInsideList(value)
        
        # Return the computed sum when "red" is not a value of the dictionnary.
        return totalSum
    
    @staticmethod
    def day_12_helper_computeSumInsideList(listToComputeSum: list) -> int:
        """
        Helper for the solution for day 12. Compute the sum inside a list.
        https://adventofcode.com/2015/day/12

        Returns:
            Sum of all elements inside the list that should be counted. 

        Args:
            listToComputeSum (list): List that represents a JSON element.
        """
        totalSum: int = 0       # Sum of all elements inside the list.

        # Iterate among all elements of the list.        
        for element in listToComputeSum:
            # If the value is an integer, we can add it to the sum.
            if type(element) is int:
                totalSum += element
            
            # If the value is a dict, we add the inner dict sum.
            elif type(element) is dict:
                totalSum += Year2015_Solution.day_12_helper_computeSumInsideDict(element)
            
            # If the value is a list, we add the inner list sum.
            elif type(element) is list:
                totalSum += Year2015_Solution.day_12_helper_computeSumInsideList(element)
            
        # Return the total sum of all the list.
        return totalSum

    @staticmethod
    def day_12_Part_1() -> int:
        """
        Get solution for day 11, Part 1
        https://adventofcode.com/2015/day/12

        Returns:
            The Sum of all integers on the JSON file of the Elves document.
        """
        line: str                           # Input of the problem, stored on a string.
        totalSum: int                       # Sum of all numbers in the document.
        regexForIntegers: str = r"-?\d+"    # Regex used to find all integers, that may be negative and composed of mulitples digits.
        integers: list[type]                # List of all the integers found in the input.

        # Retrieve the input of the problem.
        line = getLine(Year2015_Solution.year, 12)

        # Find all the integers of the document.
        integers = findall(regexForIntegers, line)

        # Convert the integers that were in str to int.
        integers = [int(integer) for integer in integers]

        # Compute the sum of all integers
        totalSum = sum(integers)

        # Return the sum of everything in the Elves document.
        return totalSum

    @staticmethod
    def day_12_Part_2() -> int:
        """
        Get solution for day 12, Part 2
        https://adventofcode.com/2015/day/12#part2

        Returns:
            The Sum of all integers on the JSON file without counting twice "red" elements.
        """
        
        totalSum: int                       # Sum of all numbers in the document.
        dictOfCurrentElements: dict         # Dictionnary of the elements found in the JSON input.

        # Retrieve the input of the problem.
        with open(getNameOfFile(Year2015_Solution.year, 12), mode="r", encoding="utf-8") as file:
            dictOfCurrentElements = load(file)

        # Find the sum of all elements without counting twice the "red" elements.
        totalSum = Year2015_Solution.day_12_helper_computeSumInsideDict(dictOfCurrentElements)

        # Return the sum of according to the new rule in the Elves document.
        return totalSum
    
    day_13_happinessSolution: int = - maxsize

    @staticmethod
    def day_13_helper_dfs(listOfPersonAtDinningTable: list[int], matrixOfHappiness: list[list[int]], currentHappiness: int) -> None:
        """
        Helper for the solution for day 13. Use DFS to find the maximum happiness.
        https://adventofcode.com/2015/day/13

        Args:
            - listOfPersonAtDinningTable (list[int]): List of all persons at the table, in the order they are.
            - matrixOfHappiness (list[list[int]]): Matrix that contains the happiness of people when they are next to the other.
            - currentHappiness (int): Happiness of the current configuration.
        """
        indexOfPerson: int            # Index of the person that we are looking for maximizing happiness.

        # Iterating among all persons to find the next one should be at the table
        for indexOfPerson in range(len(matrixOfHappiness)):
            # If the person is at the table, we don't want to add him a second time.
            if indexOfPerson in listOfPersonAtDinningTable:
                continue

            # Add the person to the list of person at the table. Add the happiness gain / lost to the current happiness
            listOfPersonAtDinningTable.append(indexOfPerson)
            currentHappiness += matrixOfHappiness[listOfPersonAtDinningTable[-2]][listOfPersonAtDinningTable[-1]]
            currentHappiness += matrixOfHappiness[listOfPersonAtDinningTable[-1]][listOfPersonAtDinningTable[-2]]
            
            # If all persons are on the table, we store the max happiness.
            if len(matrixOfHappiness) == len(listOfPersonAtDinningTable):
                Year2015_Solution.day_13_happinessSolution = max(Year2015_Solution.day_13_happinessSolution, \
                                                                 currentHappiness + matrixOfHappiness[listOfPersonAtDinningTable[-1]][listOfPersonAtDinningTable[0]] \
                                                                 + matrixOfHappiness[listOfPersonAtDinningTable[0]][listOfPersonAtDinningTable[-1]])
            
            # if not everyone is here, we should try adding more
            else:
                Year2015_Solution.day_13_helper_dfs(listOfPersonAtDinningTable, matrixOfHappiness, currentHappiness)

            # Delete the last person and substract the useless happiness.
            currentHappiness -= matrixOfHappiness[listOfPersonAtDinningTable[-2]][listOfPersonAtDinningTable[-1]]
            currentHappiness -= matrixOfHappiness[listOfPersonAtDinningTable[-1]][listOfPersonAtDinningTable[-2]]
            listOfPersonAtDinningTable.pop()
            
    @staticmethod
    def day_13_helper_buildMatrixOfHappiness() -> list[list[int]]:
        """
        Helper for the solution for day 13. Construct the distance happiness between each persons. 
        https://adventofcode.com/2015/day/13

        Returns:
            - matrixOfHappiness (list[list[int]]): Happiness between every persons.
        """
        dictOfHappinessAndIndex: dict[str, int] = {}    # Dictionary to find where the happiness should be written in matrix.
        lastIndex: int = 0                              # Integer to map name of persons to index.
        matrixOfHappiness: list[list[int]]              # Output: Matrix of the happiness between each person.
        lines: list[str]                                # All lines of the input of the problem.
        line: str                                       # String representing the input line by line.

        # Retrieve all lines of the input file
        lines = getLines(Year2015_Solution.year, 13)
        
        # Construct the dict to know which name correspond to which happiness
        for line in lines:
            strings = findall(r"\b[a-zA-Z]+\b", line)
            if strings[0] not in dictOfHappinessAndIndex:
                dictOfHappinessAndIndex[strings[0]] = lastIndex
                lastIndex += 1
            if strings[-1] not in dictOfHappinessAndIndex:
                dictOfHappinessAndIndex[strings[-1]] = lastIndex
                lastIndex += 1
        
        # Fill a matrix with - INFINITE happiness
        matrixOfHappiness = [[- maxsize for _ in range(lastIndex)] for _ in range(lastIndex)]

        # Happiness for a person next to himself is 0.
        for lineOfMatrix in range(len(matrixOfHappiness)):
            matrixOfHappiness[lineOfMatrix][lineOfMatrix] = 0

        # Retrieve the given happiness.
        for line in lines:
            strings = findall(r"\b[a-zA-Z]+\b", line)
            happiness = int(findall(r"\b[0-9]+\b", line)[0])

            matrixOfHappiness[dictOfHappinessAndIndex[strings[0]]][dictOfHappinessAndIndex[strings[-1]]] = happiness

            # If the happiness is lost, it's negative happiness.
            if "would lose" in line:
                matrixOfHappiness[dictOfHappinessAndIndex[strings[0]]][dictOfHappinessAndIndex[strings[-1]]] *= -1
        
        # Return the matrix with all happiness.
        return matrixOfHappiness

    @staticmethod
    def day_13_helper_AddMyselfToTable(matrixOfHappiness: list[list[int]]) -> None:
        """
        Helper for the solution for day 13. Add myself to the matrix of happiness. 
        https://adventofcode.com/2015/day/13

        Returns:
            - None because the list is modified in place.
        """
        lineOfHappiness: list[int]      # Line of happiness of everyone

        # Add a 0 relationship to me for everyone
        for lineOfHappiness in matrixOfHappiness:
            lineOfHappiness.append(0)
        
        # Add a 0 relationship for everyone to me
        matrixOfHappiness.append([0 for _ in range(len(matrixOfHappiness))])
    
    @staticmethod
    def day_13_Part_1() -> int:
        """
        Get solution for day 13, Part 1
        https://adventofcode.com/2015/day/13

        Returns:
            Maximum happiness we can have when making the table configuration
        """
        matrixOfHappiness: list[list[int]]  # Matrix containing all the happiness between everyone
        
        # Set the solution to max value to make the comparaison logical with min function
        Year2015_Solution.day_13_happinessSolution = - maxsize

        # Retrieve the matrix thanks to the helper function
        matrixOfHappiness = Year2015_Solution.day_13_helper_buildMatrixOfHappiness()
        
        # Find the max happiness possible. The person who sits first does not change anyhting as the table is round.
        Year2015_Solution.day_13_helper_dfs([0], matrixOfHappiness, 0)

        # Return the max happiness found
        return Year2015_Solution.day_13_happinessSolution
    
    @staticmethod
    def day_13_Part_2() -> int:
        """
        Get solution for day 13, Part 2
        https://adventofcode.com/2015/day/13#part2

        Returns:
            Maximum happiness we can have when making the table configuration with me at the table !
        """
        matrixOfHappiness: list[list[int]]  # Matrix containing all the happiness between everyone
        
        # Set the solution to max value to make the comparaison logical with min function
        Year2015_Solution.day_13_happinessSolution = - maxsize

        # Retrieve the matrix thanks to the helper function
        matrixOfHappiness = Year2015_Solution.day_13_helper_buildMatrixOfHappiness()

        # Add myself to the table
        Year2015_Solution.day_13_helper_AddMyselfToTable(matrixOfHappiness)
        
        # Find the max happiness possible. The person who sits first does not change anyhting as the table is round.
        Year2015_Solution.day_13_helper_dfs([0], matrixOfHappiness, 0)

        # Return the max happiness found
        return Year2015_Solution.day_13_happinessSolution

    @staticmethod
    def day_14_helper_getSpeedAndTimesForReindeers() -> list[list[int]]:
        """
        Helper for the solution for day 14. Create a matrix with all informations for all reindeers. 
        https://adventofcode.com/2015/day/14

        Returns:
            A list where in each element we have:
                - 0. The speed when mooving
                - 1. The time the reindeer can move
                - 2. The time the reindeer will rest
        """
        lines: list[str]                                         # All lines of the input of the problem.
        line: str                                                # String representing the input line by line.
        regexForFidingIntegers: str = "[0-9]+"                   # Regex used to find all numerics value in the input.
        distancesByTimeForEachReindeer: list[list[int]] = []     # List of all distances that reindeer can make in the associated time

        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 14)

        # Iterating among all lines to retrieve informations of speed and rest time
        for line in lines:
            distancesByTimeForEachReindeer.append(findall(regexForFidingIntegers, line))
            distancesByTimeForEachReindeer[-1] = [int(val) for val in distancesByTimeForEachReindeer[-1]]

        return distancesByTimeForEachReindeer

    @staticmethod
    def day_14_Part_1():
        """
        Get solution for day 14, Part 1
        https://adventofcode.com/2015/day/14

        Returns:
            Distance the winning reindeer traveled for Reindeer Olympics!
        """
        numberOfSeconds: int = 2503                              # Number of seconds the race last.
        distancesByTimeForEachReindeer: list[list[int]] = []     # List of all distances that reindeer can make in the associated time
        mostDistanceTravelled: int = 0                           # Value of the most distance done.

        # Retrieve Reindeers informations
        distancesByTimeForEachReindeer = Year2015_Solution.day_14_helper_getSpeedAndTimesForReindeers()
        
        # Iterating among all reindeer to find the distance he made, and store the distance if it's the max ever made.
        for reindeer in distancesByTimeForEachReindeer:
            
            # Compute the number of 'full traject' (Fly + rest)
            nbOfTrajectWithBreak: int = int(numberOfSeconds / (reindeer[1] + reindeer[2]))
            # Compute the number of seconds the reindeer will fly after his last break
            nbSecondsLeft: int = min(reindeer[1], numberOfSeconds - nbOfTrajectWithBreak * (reindeer[1] + reindeer[2]))

            # Compute the distance of the current reindeer. 
            currentDistance: int = reindeer[0] * (nbOfTrajectWithBreak * reindeer[1] + nbSecondsLeft)

            # Compute the most distance travelled.
            mostDistanceTravelled = max(mostDistanceTravelled, currentDistance)
        
        # Return the most distance that has been travelled.
        return mostDistanceTravelled
    
    @staticmethod
    def day_14_Part_2():
        """
        Get solution for day 14, Part 2
        https://adventofcode.com/2015/day/14#part2

        Returns:
            Distance the winning reindeer traveled for Reindeer Olympics with new rules!
        """
        numberOfSeconds: int = 2503                              # Number of seconds the race last.
        distancesByTimeForEachReindeer: list[list[int]] = []     # List of all distances that reindeer can make in the associated time
        distanceAndScoreByReindeer: list[int] = []               # Store the distance and the score of a reinder after n second.
        nbOfReindeer: int                                        # Number of reindeer making the race

        # Retrieve Reindeers informations
        distancesByTimeForEachReindeer = Year2015_Solution.day_14_helper_getSpeedAndTimesForReindeers()
        
        # Compute the number of reindeer
        nbOfReindeer = len(distancesByTimeForEachReindeer)

        # All reindeer are at distance 0 and score 0.
        distanceAndScoreByReindeer = [[0, 0] for _ in range(nbOfReindeer)]
            
        # Iterating among all seconds to see where reindeers are and check who has the biggest score.
        for currentTime in range(numberOfSeconds):
            
            # Store the list of all reindeers position
            listIndexMostTravelled:list[int] = [0]
    
            for indexReindeer in range(nbOfReindeer):
                # If the deer is in a mooving phase, make him move
                if distancesByTimeForEachReindeer[indexReindeer][1] > currentTime % (distancesByTimeForEachReindeer[indexReindeer][1] + distancesByTimeForEachReindeer[indexReindeer][2]):
                    distanceAndScoreByReindeer[indexReindeer][0] += distancesByTimeForEachReindeer[indexReindeer][0]
                
                # For all reindeers of index 1 or more, check if the have the max distance
                if 0 != indexReindeer:
                    # If he is not the only one in front, he will win also 1 point as the other one
                    if distanceAndScoreByReindeer[listIndexMostTravelled[0]][0] == distanceAndScoreByReindeer[indexReindeer][0]:
                        listIndexMostTravelled.append(indexReindeer)
                    # If he is the only one at the front of the course, he is the only one to get one point
                    elif distanceAndScoreByReindeer[listIndexMostTravelled[0]][0] < distanceAndScoreByReindeer[indexReindeer][0]:
                        listIndexMostTravelled = [indexReindeer]
            
            # Give one point to all of them who are at the front of the race
            for reindeer in listIndexMostTravelled:
                distanceAndScoreByReindeer[reindeer][1] += 1
        
        # Return the most distance that has been travelled.
        return max(distanceAndScoreByReindeer[indexReindeer][1] for indexReindeer in range(nbOfReindeer))
    
    day_15_cookieWithMaxScore = 0

    @staticmethod
    def day_15_helper_getMaxScore(listOfIngredients: list[dict[str, int]], quantityOfIngredients: list[int], isCalorieCounted: bool):
        """
        Helper for the solution for day 15. Create all possibles cookies combinaison.
        https://adventofcode.com/2015/day/15

        Args:
            - listOfIngredients (list[dict[str, int]]): List of all ingredients with their caracteristics stored in a map.
            - quantityOfIngredients (list[int]): Number of teaspoon of each ingredient, in the same order.
            - isCalorieCounted (bool): A boolean that states is the calorie is checked. When checked, they have to be 500.
        """
        numberOfTeaspoon: int = 100         # Number of teaspoon of ingredients that should be used.
        
        # If all ingredients are used, we can try to update the best cookie if the calorie are not counted or equal to 500.
        if len(quantityOfIngredients) == len(listOfIngredients):
            if not isCalorieCounted or 500 == sum(quantityOfIngredients[i] * listOfIngredients[i]["calories"] for i in range(len(listOfIngredients))):
                Year2015_Solution.day_15_cookieWithMaxScore = max(Year2015_Solution.day_15_cookieWithMaxScore, Year2015_Solution.day_15_helper_computeCookieValue(listOfIngredients, quantityOfIngredients))
        
        # If one ingredient is missing only, the quantity has to be the number of missing teaspoon. Add it and and the next call it will check which
        # Cookie is the best.
        elif len(quantityOfIngredients) == (len(listOfIngredients) - 1):
            quantityOfIngredients.append(numberOfTeaspoon - sum(quantityOfIngredients))
            Year2015_Solution.day_15_helper_getMaxScore(listOfIngredients, quantityOfIngredients, isCalorieCounted)
            quantityOfIngredients.pop()
        
        # If multiple ingredient are missing, multiple choice can be done. We could add from 0 to nbMissingIngredients the next ingredient.
        else:
            for i in range(0, numberOfTeaspoon - sum(quantityOfIngredients)):
                quantityOfIngredients.append(i)
                Year2015_Solution.day_15_helper_getMaxScore(listOfIngredients, quantityOfIngredients, isCalorieCounted)
                quantityOfIngredients.pop()
    
    @staticmethod
    def day_15_helper_computeCookieValue(listOfIngredients: list[dict[str, int]], quantityOfIngredients: list[int]) -> int:
        """
        Helper for the solution for day 15. Compute the score of a given cookie.
        https://adventofcode.com/2015/day/15

        Args:
            - listOfIngredients (list[dict[str, int]]): List of all ingredients with their caracteristics stored in a map.
            - quantityOfIngredients (list[int]): Number of teaspoon of each ingredient, in the same order.
        Returns:
            Score of the current cookie.
        """
        numberOfElements = len(listOfIngredients)                           # Number of caracteristic an ingredient has.
        scores = [0 for _ in range(len(listOfIngredients[0]) - 1)]          # Score for each caracteristic of a cookie.
        ingredientIndex: int                                                # Index of a caracteristic in the map of cookies.
        scoresIndex: int                                                    # Index of the score we are looking at when looking an ingredient.
        
        # Iterating among all characteristics
        for ingredientIndex in range(numberOfElements):
            
            # Re-Initialize the index of the score of the map
            scoresIndex = 0
            
            # Iterating among all caracteristics
            for key, val in listOfIngredients[ingredientIndex].items():
                
                # If the caracteristic is calories, it does not count for score
                if "calories" == key:
                    continue
                
                # Compute the score of the caracteristic
                scores[scoresIndex] += quantityOfIngredients[ingredientIndex] * val
                # Go to the next caracteristic to count
                scoresIndex += 1

        # If we have at least one negative score, the global score of the cookie is 0.
        if any(element <= 0 for element in scores):
            return 0
        
        # Return the score of a cookie: the product of all caracteristics.
        return np.prod(scores)

    @staticmethod
    def day_15_helper_constructTableOfIngredients() -> list[dict[str, int]]:
        """
        Helper for the solution for day 15. Create a table that contains all mapping of information for each ingredients.
        https://adventofcode.com/2015/day/15

        Returns:
            A list which contains the map of each ingredient.
        """
        listOfAllIngredients: list[dict[str, int]] = []              # Output table that contains all needed information.
        mappingOfOneIngredient: dict[str, int]                       # One map for a given ingredient.
        lines: list[str]                                            # All lines of the input of the problem.
        line: str                                                   # String representing the input line by line.
        regexForIngredients: str = r'\b[A-Za-z]+\s[-]?\d+\b'        # Regex for finding informations of the ingredients.
        matches: list[list[str]]                                    # Table that contain the output of the search via the regex.

        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 15)

        # Iterating among all ingredients
        for line in lines:
            # Find all caracteristics of the ingredient
            matches = findall(regexForIngredients, line)

            # Construct the information of the current ingredient 
            mappingOfOneIngredient = {m.split()[0]: int(m.split()[1]) for m in matches}

            # Add the ingredient to the list of known ingredients
            listOfAllIngredients.append(mappingOfOneIngredient)
        
        # Return all ingredients formatted
        return listOfAllIngredients

    @staticmethod
    def day_15_Part_1() -> int:
        """
        Get solution for day 15, Part 1
        https://adventofcode.com/2015/day/15

        Returns:
            The best score a cookie can have!
        """
        tableOfIngredients: list[dict[str, int]]        # Table of used ingredients
        
        # Retrieve ingredients and their caracteristics
        tableOfIngredients = Year2015_Solution.day_15_helper_constructTableOfIngredients()

        # Re-initialize the max score ever found.
        Year2015_Solution.day_15_cookieWithMaxScore = 0

        # Find the cookie with the best score, without looking at calories.
        Year2015_Solution.day_15_helper_getMaxScore(tableOfIngredients, [], False)

        # Return the best score obtained.
        return Year2015_Solution.day_15_cookieWithMaxScore

    @staticmethod
    def day_15_Part_2() -> int:
        """
        Get solution for day 15, Part 2
        https://adventofcode.com/2015/day/15#part2

        Returns:
            The best score a cookie can have when calories should be 500!
        """
        tableOfIngredients: list[dict[str, int]]        # Table of used ingredients
        
        # Retrieve ingredients and their caracteristics
        tableOfIngredients = Year2015_Solution.day_15_helper_constructTableOfIngredients()

        # Re-initialize the max score ever found.
        Year2015_Solution.day_15_cookieWithMaxScore = 0

        # Find the cookie with the best score, and taking care of the number of calories.
        Year2015_Solution.day_15_helper_getMaxScore(tableOfIngredients, [], True)

        # Return the best score obtained.
        return Year2015_Solution.day_15_cookieWithMaxScore

    @staticmethod
    def day_16_helper_getInformationFromMFCSAM() -> dict[str: int]:
        """
        Helper for the solution for day 16. Create a dict with all information from the MFCSAM.
        https://adventofcode.com/2015/day/16

        Returns:
            A dict with all information from the MFCSAM.
        """
        informationFromMFCSAM: dict[str: int] = {}                 # Dictionnary that contains information of the letter received.
        
        # Fill the information
        informationFromMFCSAM["children"]    = 3
        informationFromMFCSAM["cats"]        = 7
        informationFromMFCSAM["samoyeds"]    = 2
        informationFromMFCSAM["pomeranians"] = 3
        informationFromMFCSAM["akitas"]      = 0
        informationFromMFCSAM["vizslas"]     = 0
        informationFromMFCSAM["goldfish"]    = 5
        informationFromMFCSAM["trees"]       = 3
        informationFromMFCSAM["cars"]        = 2
        informationFromMFCSAM["perfumes"]    = 1

        # Return all information we have.
        return informationFromMFCSAM
    
    @staticmethod
    def day_16_Part_1() -> int:
        """
        Get solution for day 16, Part 1
        https://adventofcode.com/2015/day/16

        Returns:
            Which one of the 500 aunt Sue send a gift.
        """
        lines: list[str]                                            # All lines of the input of the problem.
        line: str                                                   # String representing the input line by line.
        matches: list[str]                                          # Matches of the information we have about the current Aunt Sue.
        regexForItemAndValue: str = r'\b[A-Za-z]+:\s\d+\b'          # Regex for finding information about the current Sue
        informationFromMFCSAM: dict[str: int]                       # Dictionnary that contains information of the letter received.
        areAllInformationCorrect: bool                              # States if all information are passing for the current Sue.

        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 16)

        # Retrieve the information from the letter
        informationFromMFCSAM = Year2015_Solution.day_16_helper_getInformationFromMFCSAM()

        # Iterate among all aunts
        for index, line in enumerate(lines):
            
            # Find all characteristic of the current Sue and store it in a map
            matches = findall(regexForItemAndValue, line)
            mappingOfInformations = {match.split()[0][:-1]: int(match.split()[1]) for match in matches}
            
            # Re-init the information correctness
            areAllInformationCorrect = True
            
            # Iterating among all elements of the current Sue. If she does not have the spicificy or have a different value
            # Then it's not the correct Aunt.
            for key, value in mappingOfInformations.items():
                if key not in informationFromMFCSAM or value != informationFromMFCSAM[key]:
                    areAllInformationCorrect = False
                    break
            
            # If every elements were correct, we return the Aunt index.
            if areAllInformationCorrect:
                return index + 1
        
        # Should not be there, it would mean that no Sue is valid.
        return -1
    
    @staticmethod
    def day_16_Part_2() -> int:
        """
        Get solution for day 16, Part 2
        https://adventofcode.com/2015/day/16#part2

        Returns:
            Which one of the 500 aunt Sue send a gift.
        """
        lines: list[str]                                            # All lines of the input of the problem.
        line: str                                                   # String representing the input line by line.
        matches: list[str]                                          # Matches of the information we have about the current Aunt Sue.
        regexForItemAndValue: str = r'\b[A-Za-z]+:\s\d+\b'          # Regex for finding information about the current Sue
        informationFromMFCSAM: dict[str: int]                       # Dictionnary that contains information of the letter received.
        areAllInformationCorrect: bool                              # States if all information are passing for the current Sue.

        # Retrieve the input of the problem.
        lines = getLines(Year2015_Solution.year, 16)

        # Retrieve the information from the letter
        informationFromMFCSAM = Year2015_Solution.day_16_helper_getInformationFromMFCSAM()

        # Iterate among all aunts
        for index, line in enumerate(lines):
            
            # Find all characteristic of the current Sue and store it in a map
            matches = findall(regexForItemAndValue, line)
            mappingOfInformations = {match.split()[0][:-1]: int(match.split()[1]) for match in matches}
            
            # Re-init the information correctness
            areAllInformationCorrect = True
            
            # Iterating among all elements of the current Sue.
            for key, value in mappingOfInformations.items():
                # If the key is not present on tha machine response, it's not the correct Sue.
                if key not in informationFromMFCSAM:
                    areAllInformationCorrect = False
                    break
                
                # The correct Sue should have more cats and tree than what the machine says.
                if key in ("cats", "tree"):
                    if value <= informationFromMFCSAM[key]:
                        areAllInformationCorrect = False
                        break
                # The correct Sue should have less cats and tree than what the machine says.
                elif key in ("pomeranians", "goldfish"):
                    if value >= informationFromMFCSAM[key]:
                        areAllInformationCorrect = False
                        break
                # The correct Sue should have more the same value for all other element.
                elif value != informationFromMFCSAM[key]:
                        areAllInformationCorrect = False
                        break
            
            # If every elements were correct, we return the Aunt index.
            if areAllInformationCorrect:
                return index + 1
        
        # Should not be there, it would mean that no Sue is valid.
        return -1
