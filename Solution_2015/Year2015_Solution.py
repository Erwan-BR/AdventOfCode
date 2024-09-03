from Global.globals import getLines, getLine
from Solution.Solution import Solution
from re import split
from hashlib import md5
import numpy as np

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
        line: str                  # Input of the problem, stored on a string.

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
        lines: list[str]                # All files of the input of the problem.
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
        lines: list[str]          # All files of the input of the problem.
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
        Helper for the solution for day 4.
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
        lines: list[str]                                        # All files of the input of the problem.
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
        lines: list[str]                                        # All files of the input of the problem.
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