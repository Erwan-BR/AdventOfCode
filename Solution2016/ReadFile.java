package Solution2016;

import java.io.File;
import java.io.FileNotFoundException;

import java.util.Scanner;
import java.util.ArrayList;

public class ReadFile
{
    /**
     * Function used to get the path of the input file. Input files should be in a subfolder "textfiles", and named
     * x.txt where is x is the number of the day. if 10 > x, write 0x (for example 03.txt for day 3).
     *
     * @param day Day when the problem was published.
     * @return String representing the path of the textfile.
     */
    private static String getNameOfFile(final int day)
    {
        String representationOfDay = "textfiles/";

        representationOfDay += (day < 10) ? "0" + String.valueOf(day) : String.valueOf(day);

        representationOfDay += ".txt";

        return representationOfDay;
    }

    /**
     * Function used to get the string in the input file.
     * Handle FileNotFoundException and return an empty String in this case.
     *
     * @param day Day when the problem was published.
     * @return A string that contains the input of the problem.
     */
    public static String getLine(final int day)
    {
        // Try to open the file, get the line in the data object and then return it.
        try
        {
            final String fileName = getNameOfFile(day);
            final File fileToOpen = new File(fileName);
            final Scanner scannerOfFile = new Scanner(fileToOpen);
            
            final String line = scannerOfFile.nextLine();
            scannerOfFile.close();
            
            return line;
        }
        // Catch the error that indicates the file was not found.
        catch (Exception e)
        {
            System.err.println("An error occurred, the file cannot be opened.");
            e.printStackTrace();
            return "";
        }
    }
    
    /**
     * Function used to get the strings in the input file that contains multiple lines.
     * Handle FileNotFoundException and return an empty String in this case.
     *
     * @param day Day when the problem was published.
     * @return A list of strings that contains the input of the problem.
     */
    public static ArrayList<String> getLines(final int day)
    {
        // Try to open the file, get the lines in the data object and then return it.
        try
        {
            ArrayList<String> lines = new ArrayList<String>();

            final String fileName = getNameOfFile(day);
            final File fileToOpen = new File(fileName);
            final Scanner scannerOfFile = new Scanner(fileToOpen);
            
            // While there is some line after the current one, read the next one and add it to the 
            // Array of lines.
            while (scannerOfFile.hasNextLine())
            {
                String data = scannerOfFile.nextLine();
                lines.add(data);
            }
            scannerOfFile.close();

            return lines;
        }
        // Catch the error that indicates the file was not found.
        catch (Exception e)
        {
            System.err.println("An error occurred, the file cannot be opened.");
            e.printStackTrace();
            return new ArrayList<String>();
        }
    }
}
