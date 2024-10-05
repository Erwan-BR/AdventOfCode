import os

class ReadFile():
    
    CURRENT_PATH = os.getcwd()
    
    def getNameOfFile(day: int) -> str:
        """
        Function used to get the path of the input file. Input files should be in a subfolder "textfiles", and named
        x.txt where is x is the number of the day. if 10 > x, write 0x (for example 03.txt for day 3).

        Args:
            day (int): Day when the problem was published.
        
        Returns:
            String representing the path of the textfile.
        """
        return os.path.join(ReadFile.CURRENT_PATH, "textFiles", f"{day:02d}.txt")

    @staticmethod
    def getLine(day: int) -> str:
        """
        Function used to get the string in the input file.

        Args:
            day (int): Day when the problem was published.
        
        Returns:
            A string that contains the input of the problem.
        """
        line: str        # String that contains the input of the problem.
        
        try:
            # Open the input file to retrieve the line.
            with open(ReadFile.getNameOfFile(day), 'r') as file:
                line = file.readline()
            return line
        except Exception:
            print(f"An error occurred, the file cannot be opened.")
            return ""
    
    @staticmethod
    def getLines(day: int) -> list[str]:
        """
        Function used to get the strings in the input file that contains multiple lines.

        Args:
            day (int): Day when the problem was published.
        
        Returns:
            A list of strings that contains the input of the problem.
        """
        lines: list[str]        # List of strings that contains the input of the problem.

        try:
            # Open the input file to retrieve the lines.
            with open(ReadFile.getNameOfFile(day), 'r') as file:
                lines = file.readlines()
                return lines
        
        except Exception:
            print(f"An error occurred, the file cannot be opened.")
            return []
