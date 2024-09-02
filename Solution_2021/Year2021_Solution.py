from Global.globals import getNameOfFile
from Solution.Solution import Solution

class Year2021_Solution(Solution):
    """
    Class containing the method for having solution of problems of year 2021.
    """

    year: int = 2021
    """
    Constant value that represents the year number. Used to find textfiles.
    """

    def getSolution(day: str, isFirstPart: bool):
        """
        Method to get solution of every day for which the solution is developped.
        Call the parent function with the corresponding arguments.
        """
        return Solution.getSolution(Year2021_Solution, Year2021_Solution.year, day, isFirstPart)
