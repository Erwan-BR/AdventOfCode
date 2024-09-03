from Global.globals import getLines, getLine
from Solution.Solution import Solution

class Year2022_Solution(Solution):
    """
    Class containing the method for having solution of problems of year 2022.
    """

    year: int = 2022
    """
    Constant value that represents the year number. Used to find textfiles.
    """

    def getSolution(day: str, isFirstPart: bool):
        """
        Method to get solution of every day for which the solution is developped.
        Call the parent function with the corresponding arguments.
        """
        return Solution.getSolution(Year2022_Solution, Year2022_Solution.year, day, isFirstPart)
