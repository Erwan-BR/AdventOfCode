from Global.globals import getLines, getLine
from Solution.Solution import Solution
from re import split, findall
from hashlib import md5
import numpy as np
from typing import Callable
from sys import maxsize

class Year2015_Solution(Solution):
    """
    Class containing the method for having solution of problems of year 2015.
    """

    year: int = 2015
    """
    Constant value that represents the year number. Used to find textfiles.
    """

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
        https://adventofcode.com/2015/day/1

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
        https://adventofcode.com/2015/day/2

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
        https://adventofcode.com/2015/day/3

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
        https://adventofcode.com/2015/day/4

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
        https://adventofcode.com/2015/day/5

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
            pairOfConsecutiveLetters: map[str, int] = dict()
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
        Get solution for day 6, Part 1
        https://adventofcode.com/2015/day/6

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
        https://adventofcode.com/2015/day/7

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
        https://adventofcode.com/2015/day/8

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
    def day_09_helper_buildDictOfCitiesAndMatrixOfDistances() -> list[list[int]]:
        """
        Helper for the solution for day 9. Construct the distance matrix between each places. 
        https://adventofcode.com/2015/day/9

        Returns:
            - listOfVisitedCities (list[int]): list of the cities visited, in the right order
            - matrixOfDistances (list[list[int]]): Distance between every cities.
            - currentDistance (int): Distance done for visiting all vities from listOfVisitedCities.
            - fctToCall (Callable[int]): Function that should be applied for visiting the cities. Should be min / max.
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
        matrixOfDistances = Year2015_Solution.day_09_helper_buildDictOfCitiesAndMatrixOfDistances()
        
        # Find the smallest route by starting from each cities.
        for indexCity in range(len(matrixOfDistances)):
            Year2015_Solution.day_09_helper_dfs([indexCity], matrixOfDistances, 0, True)

        # Return the smallest path found
        return Year2015_Solution.day_09_distanceSolution
    
    @staticmethod
    def day_09_Part_2() -> int:
        matrixOfDistances: list[list[int]]

        Year2015_Solution.day_09_distanceSolution = 0

        matrixOfDistances = Year2015_Solution.day_09_helper_buildDictOfCitiesAndMatrixOfDistances()
        
        for indexStart in range(len(matrixOfDistances)):
            Year2015_Solution.day_09_helper_dfs([indexStart], matrixOfDistances, 0, False)

        return Year2015_Solution.day_09_distanceSolution