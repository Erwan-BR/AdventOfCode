from Global.globals import getNameOfFile
from Solution_2015 import Year2015_Solution

class Solution:
    """
    Parent class for every Year's solution.
    """

    @staticmethod
    def getSolution(classOfCaller: type, year: int, day: str, isFirstPart: bool):
        """
        Function called outside of the class to get the solution of any day, for part one or two.
        
        Args:
            classOfCaller (type): Class of the caller, to help the constructor to find the solution in the children.
            year (int): Number of the year of the answer. Used to display error message.
            day (int): Day for which we want to recover the solution.
            isFirstPart (bool): Boolean indicating whether you want to retrieve the solution for day 1 or day 2.
                - True: Returns the solution for the first part of the problem.
                - False: Returns the solution for the second part of the problem.
            
        Handles:
            If the solution has not yet been developed, a message will be displayed. 
        """

        # Try to get the solution of the given day, for the given part.
        try:
            nameOfFunction: str = f"day_{day:02d}_Part_{"1" if isFirstPart else "2"}"

            methodToCall: function = getattr(classOfCaller, nameOfFunction)

            return methodToCall()
        
        # Except errors from a day / part that is not implemented yet.
        except AttributeError as e:
            print(f"Solution for year {year}, day {day}, part {"one" if isFirstPart else "two"} has not yet been developed.")
