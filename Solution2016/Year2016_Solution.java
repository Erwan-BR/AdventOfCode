package Solution2016;

import java.lang.reflect.Method;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashSet;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Year2016_Solution
{
    /*
     * Function called outside the class to obtain the solution for any day, for the first or second part.
     * @param day (int): Day for which we want to retrieve the solution.
     * @param isFirstPart (bool): Boolean indicating whether we want to retrieve the solution for day 1 or day 2.
     *        - True:  Returns the solution for the first part of the problem.
     *        - False: Returns the solution for the second part of the problem.
     *
     * @returns: Answer of the given problem.
     */
    public static Object getSolution(int day, Boolean isFirstPart)
    {
        try
        {
            // Construction of the name of the method
            final String methodName = String.format("day_%02d_Part_%s", day, isFirstPart ? "1" : "2");

            // Retrieve the method that has to be called.
            final Method method = Year2016_Solution.class.getDeclaredMethod(methodName);

            // Call the method 
            return method.invoke(null);
        }
        // If the method is not developped yet, display it to the user.
        catch (NoSuchMethodException e)
        {
            System.err.println("Solution for year 2016, day " + day + " part " + (isFirstPart ? "one" : "two") + " has not yet been developed.");
            return null;
        }

        // If an error occurs during the call of the method, display the reason of the error.
        catch (Exception e)
        {
            System.err.println("An error occured on the method called.");
            e.printStackTrace();
            return null;
        }
    }

    /*
     * Get solution for day 1 "No Time for a Taxicab", Part 1.
     * https://adventofcode.com/2016/day/1
     *
     * @returns: Manhattan distance between Santa and the Easter Bunny HQ.
     */
    @SuppressWarnings("unused")
    private static int day_01_Part_1()
    {
        // Get the puzzle input.
        final String line = ReadFile.getLine(1);

        // Current coordinates
        int currentCoordinates[] = {0, 0};
        
        // All the direction Santa can follow: N, E, S, W
        final int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        // At the beginning, Santa is looking north.
        int currentDirectionIndex = 0;

        // Pattern to search for with a regex
        final Pattern patternToSearch = Pattern.compile("[RL][0-9]+");
        
        // Matcher that will contains the information about how to turn and the distance to walk.
        Matcher m = patternToSearch.matcher(line);

        // Finding the next instruction
        while (m.find())
        {
            // Change the direction according to the new instruction.
            if (line.substring(m.start(), m.start() + 1).equals("R"))
            {
                currentDirectionIndex += 1;
                // If we go north, we update it to the first index of the table.
                if (4 == currentDirectionIndex)
                {
                    currentDirectionIndex = 0;
                }
            }
            else if (line.substring(m.start(), m.start() + 1).equals("L"))
            {
                currentDirectionIndex -= 1;
                // If we go west, we update it to the last index of the table.
                if (-1 == currentDirectionIndex)
                {
                    currentDirectionIndex = 3;
                }
            }
            
            // Update the current coordinates
            currentCoordinates[0] += directions[currentDirectionIndex][0] * Integer.valueOf(line.substring(m.start() + 1, m.end()));
            currentCoordinates[1] += directions[currentDirectionIndex][1] * Integer.valueOf(line.substring(m.start() + 1, m.end()));
        }

        // Return the distance that should be walked to go to the Easter Bunny HQ.
        return Math.abs(currentCoordinates[0]) + Math.abs(currentCoordinates[1]);
    }

    /*
     * Get solution for day 1 "No Time for a Taxicab", Part 2.
     * https://adventofcode.com/2016/day/1#part2
     *
     * @returns: First place visited 2 times.
     */
    @SuppressWarnings("unused")
    private static int day_01_Part_2()
    {
        // Get the puzzle input.
        final String line = ReadFile.getLine(1);

        // Current coordinates
        List<Integer> currentCoordinates = Arrays.asList(0, 0);

        // Coordinates already visited:
        HashSet<List<Integer>> coordinatesAlreadyVisited = new HashSet<>();

        // Add to the list of visited places the initial position.
        coordinatesAlreadyVisited.add(new ArrayList<>(currentCoordinates));

        // All the direction Santa can follow: N, E, S, W
        final int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        // At the beginning, Santa is looking north.
        int currentDirectionIndex = 0;

        // Pattern to search for with a regex
        final Pattern patternToSearch = Pattern.compile("[RL][0-9]+");
        
        // Matcher that will contains the information about how to turn and the distance to walk.
        Matcher m = patternToSearch.matcher(line);

        // Finding the next instruction
        while (m.find())
        {
            // Change the direction according to the new instruction.
            if (line.substring(m.start(), m.start() + 1).equals("R"))
            {
                currentDirectionIndex += 1;
                // If we go north, we update it to the first index of the table.
                if (4 == currentDirectionIndex)
                {
                    currentDirectionIndex = 0;
                }
            }
            else if (line.substring(m.start(), m.start() + 1).equals("L"))
            {
                currentDirectionIndex -= 1;
                // If we go west, we update it to the last index of the table.
                if (-1 == currentDirectionIndex)
                {
                    currentDirectionIndex = 3;
                }
            }
            
            // Compute the number of steps Santa do at this instruction.
            final int numberOfMoves = Integer.valueOf(line.substring(m.start() + 1, m.end()));
            
            // Walking on all coordinate from his starting point to the end of this instruction.
            for (int move = 0; numberOfMoves > move; ++move)
            {
                // Update the current coordinates
                currentCoordinates.set(0, currentCoordinates.get(0) + directions[currentDirectionIndex][0]);
                currentCoordinates.set(1, currentCoordinates.get(1) + directions[currentDirectionIndex][1]);
                
                // If Santa already went here, it means it is Easter Bunny HQ.
                if (coordinatesAlreadyVisited.contains(currentCoordinates))
                {
                    // Return the distance that should be walked to go to the Easter Bunny HQ.
                    return Math.abs(currentCoordinates.get(0)) + Math.abs(currentCoordinates.get(1));
                }

                // If this is the first time, memoize the localisation for latter.
                coordinatesAlreadyVisited.add(new ArrayList<>(currentCoordinates));
            }
        }

        // Return -1 if the input is not making Santa going 2 times on the same coordinate.
        return -1;
    }

    /*
     * Helper for the solution to day 2.
     * Returns the keypad that is used to find the code. The keypad is surrounded by "0" to help finding if mooving
     * the finger is possible or not.
     * 
     * https://adventofcode.com/2016/day/2
     * 
     * @param isPartOne: Boolean that indicate if we should take the keypad from the first part or the second part.
     * @returns: Keypad used to solve the problem.
     */
    private static String[][] day_02_helper_getKeypadToSolve(boolean isPartOne)
    {
        // For the first part, the keypad is a regular keypad.
        if (isPartOne)
        {
            final String[][] keypad = {{"0", "0", "0", "0", "0"},
                                   {"0", "1", "2", "3", "0"},
                                   {"0", "4", "5", "6", "0"},
                                   {"0", "7", "8", "9", "0"},
                                   {"0", "0", "0", "0", "0"}};
            
            return keypad;
        }
        
        // For the second part, the keypad has a weird shape.
        final String[][] keypad = {{"0", "0", "0", "0", "0", "0", "0"},
                                   {"0", "0", "0", "1", "0", "0", "0"},
                                   {"0", "0", "2", "3", "4", "0", "0"},
                                   {"0", "5", "6", "7", "8", "9", "0"},
                                   {"0", "0", "A", "B", "C", "0", "0"},
                                   {"0", "0", "0", "D", "0", "0", "0"},
                                   {"0", "0", "0", "0", "0", "0", "0"}};
        
        return keypad;
    }

    /*
     * Helper for the solution to day 2.
     * Returns the code of the bathroom according to the keypad that should be taken.
     * 
     * https://adventofcode.com/2016/day/2
     * 
     * @param isPartOne: Boolean that indicate if we should take the keypad from the first part or the second part.
     * @returns: Code to access inside the bathroom.
     */
    private static String day_02_getSolutionFromProblem(boolean isPartOne)
    {
        // Get the puzzle input.
        final ArrayList<String> lines = ReadFile.getLines(2);

        // Code pannel shape.
        final String[][] matrixVal = Year2016_Solution.day_02_helper_getKeypadToSolve(isPartOne);
        
        // Code that should be found when following instructions.
        String codeFinal = "";

        // Coordinates where Santa should have his finger now.
        int[] currentCoordinates = {3, 3};

        // Iterate among all instructions to find each elements of the code
        for (String line: lines)
        {
            // Iterate among all instruction for one element of the code
            for (int charIndex = 0; line.length() > charIndex; ++charIndex)
            {
                // Put the finger up means decreasing the number of line by one (if possible)
                if ('U' == line.charAt(charIndex) && "0" != matrixVal[currentCoordinates[0] - 1][currentCoordinates[1]])
                {
                    -- currentCoordinates[0];
                }
                // Put the finger down means increasing the number of line by one (if possible)
                if ('D' == line.charAt(charIndex) && "0" != matrixVal[currentCoordinates[0] + 1][currentCoordinates[1]])
                {
                    ++ currentCoordinates[0];
                }
                // Put the finger right means increasing the number of column by one (if possible)
                if ('R' == line.charAt(charIndex) && "0" != matrixVal[currentCoordinates[0]][currentCoordinates[1] + 1])
                {
                    ++ currentCoordinates[1];
                }
                // Put the finger left means decreasing the number of column by one (if possible)
                if ('L' == line.charAt(charIndex) && "0" != matrixVal[currentCoordinates[0]][currentCoordinates[1] - 1])
                {
                    -- currentCoordinates[1];
                }
            }
            // Concatenate the new part of code to the code already found.
            codeFinal += matrixVal[currentCoordinates[0]][currentCoordinates[1]];
        }

        // Return the code that Santa found.
        return codeFinal;
    }

    /*
     * Get solution for day 2 "Bathroom Security".
     * https://adventofcode.com/2016/day/2
     *
     * @returns: Code to open the bathroom.
     */
    @SuppressWarnings("unused")
    private static String day_02_Part_1()
    {
        // Retrieve the solution for the first part and return it.
        return Year2016_Solution.day_02_getSolutionFromProblem(true);
    }

    /*
     * Get solution for day 2 "Bathroom Security", Part 2.
     *  https://adventofcode.com/2016/day/2#part2
     *
     * @returns: Code to open the bathroom with a weird keypad shape.
     */
    @SuppressWarnings("unused")
    private static String day_02_Part_2()
    {
        // Retrieve the solution for the second part and return it.
        return Year2016_Solution.day_02_getSolutionFromProblem(false);
    }

    /*
     * Helper for the solution to day 3.
     * Check if coordinates corresponds to triangles coordinates.
     * 
     * https://adventofcode.com/2016/day/3
     * 
     * @param dimensions: 3 length that may be the dimensions of a triangle.
     * @returns: Boolean that states if the dimensions are valid for a triangle or not.
     */
    private static Boolean day_03_helper_checkIfTriangleIsValid(int[] dimensions)
    {
        // Compute the sum of all sides, and the max side.
        final int sum = dimensions[0] + dimensions[1] + dimensions[2];
        final int maxVal = Math.max(Math.max(dimensions[0], dimensions[1]), dimensions[2]);
        
        // This is a valid triangle if the max side is smaller than the sum of the two others.
        return (maxVal < (sum - maxVal));
    }

    /*
     * Get solution for day 3 "Squares With Three Sides", Part 1.
     *  https://adventofcode.com/2016/day/3
     *
     * @returns: Number of possible triangles.
     */
    @SuppressWarnings("unused")
    private static int day_03_Part_1()
    {
        // Get the puzzle input.
        final ArrayList<String> lines = ReadFile.getLines(3);

        // Pattern to search for with a regex (integers).
        final Pattern patternToSearch = Pattern.compile("[0-9]+");
        
        // Number of valid triangles found on the input.
        int nbTriangles = 0;
        
        // Iterate among all lines.
        for (String line: lines)
        {
            // Retrieve information about the current line in a matcher.
            Matcher m = patternToSearch.matcher(line);
            
            // Dimensions of the current triangle.
            int[] dimensions = {0, 0, 0};

            // Iterate among the 3 dimensions to write them in the dimensions table.
            for (int index = 0; 3 > index; ++index)
            {
                if (! m.find())
                {
                    return -1;
                }
                dimensions[index] = Integer.valueOf(line.substring(m.start(), m.end()));
            }

            // If this is a triangle, increment by 1 the number of valid triangles.
            if (day_03_helper_checkIfTriangleIsValid(dimensions))
            {
                ++ nbTriangles;
            }
        }
        
        // Return the number of triangles that are valid.
        return nbTriangles;
    }

    /*
     * Get solution for day 3 "Squares With Three Sides", Part 2.
     *  https://adventofcode.com/2016/day/3#part2
     *
     * @returns: Number of possible triangles on the input when they are written vertically.
     */
    @SuppressWarnings("unused")
    private static int day_03_Part_2()
    {
        // Get the puzzle input.
        final ArrayList<String> lines = ReadFile.getLines(3);

        // Pattern to search for with a regex (integers)
        final Pattern patternToSearch = Pattern.compile("[0-9]+");
        
        // Number of valid triangles found on the input.
        int nbTriangles = 0;
        
        // Iterate among all lines, 3 by 3 to take triangles vertically.
        for (int indexLine = 2; lines.size() > indexLine; indexLine += 3)
        {
            // Retrieve information about the three lines in a matcher.
            Matcher m1 = patternToSearch.matcher(lines.get(indexLine - 2));
            Matcher m2 = patternToSearch.matcher(lines.get(indexLine - 1));
            Matcher m3 = patternToSearch.matcher(lines.get(indexLine));
            
            // Dimensions of the current triangle.
            int[] dimensions = {0, 0, 0};
            
            // Iterate among the 3 dimensions to write them in the dimensions table.
            for (int index = 0; 3 > index; ++index)
            {
                if (! m1.find() || ! m2.find() || ! m3.find())
                {
                    return -1;
                }
                // Fill the information about the hypotetic triangles.
                dimensions[0] = Integer.valueOf(lines.get(indexLine - 2).substring(m1.start(), m1.end()));
                dimensions[1] = Integer.valueOf(lines.get(indexLine - 1).substring(m2.start(), m2.end()));
                dimensions[2] = Integer.valueOf(lines.get(indexLine).substring(m3.start(), m3.end()));
                
                // If the element is a triangle, increment the number of triangle found.
                if (day_03_helper_checkIfTriangleIsValid(dimensions))
                {
                    ++ nbTriangles;
                }
            }
        }
        
        // Return the number of triangles that are valid.
        return nbTriangles;
    }

    /*
     * Helper for the solution to day 5.
     * Find the MD5 hash in base 16 of the input string.
     * 
     * https://adventofcode.com/2016/day/5
     * 
     * @param inputString: String that needs to be hashed.
     * @returns: Hash of the string given has the parameter.
     */
    private static String day_05_helper_getMd5(final String inputString)
    {
        // Try to get the Md5 hash of the string
        try
        {
            // Static getInstance method is called with hashing MD5
            MessageDigest md = MessageDigest.getInstance("MD5");

            // digest() method is called to calculate message digest
            // of an input digest() return array of byte
            byte[] messageDigest = md.digest(inputString.getBytes());

            // Convert byte array into signum representation
            BigInteger no = new BigInteger(1, messageDigest);

            // Convert message digest into hex value
            String hashtext = no.toString(16);
            
            // Add a padding of zero before returning the hash text.
            while (hashtext.length() < 32)
            {
                hashtext = "0" + hashtext;
            }
            return hashtext;
        }

        // For specifying wrong message digest algorithms
        catch (Exception e)
        {
            throw new RuntimeException(e);
        }
    }

    /*
     * Get solution for day 5 "How About a Nice Game of Chess?", Part 1.
     *  https://adventofcode.com/2016/day/5
     *
     * @returns: Password of the door Santa needs to open.
     */
    @SuppressWarnings("unused")
    private static String day_05_Part_1()
    {
        // Try to find the password.
        try
        {
            // Get the puzzle input.
            final String line = ReadFile.getLine(5);

            // String that contains the password for the door.
            String password = "";
            
            // Value to concatenate at the end of the line to find the hash that helps
            // To get the next password.
            Integer indexToConcatenate = 0;

            // iterating 8 times to find the 8 characters of the password.
            for(int index = 0; 8 > index; ++index)
            {
                // Create a local string and get the hash of the concatenation while the 5 first elements are not 0s.
                String currentString;
                do
                {
                    currentString = day_05_helper_getMd5(line + indexToConcatenate.toString());
                    ++ indexToConcatenate;
                } while (! currentString.substring(0, 5).equals("00000"));
                
                // Concatenate the value obtained at index 5 to the current password.
                password += currentString.charAt(5);
            }

            return password;
        }
        catch (Exception e)
        {
            e.printStackTrace();
            return "";
        }
    }

    /*
     * Get solution for day 5 "How About a Nice Game of Chess?", Part 2.
     *  https://adventofcode.com/2016/day/5#part2
     *
     * @returns: Password of the door Santa needs to open with a new method.
     */
    @SuppressWarnings("unused")
    private static String day_05_Part_2()
    {
        // Try to find the password.
        try
        {
            // Get the puzzle input.
            final String line = ReadFile.getLine(5);

            // String that contains the password for the door.
            // Initialized with z to show that some elements are missing, and z should not be present in
            // an hexadecimal representation.
            String password = "zzzzzzzz";
            
            // Value to concatenate at the end of the line to find the hash that helps
            // To get the next password.
            Integer indexToConcatenate = 0;
            
            // While at least one element of the password is not found, we need to continue searching for new hash.
            while(password.contains("z"))
            {
                // Create a local string and get the hash of the concatenation while the 5 first elements are not 0s.
                String currentString;
                do
                {
                    currentString = day_05_helper_getMd5(line + indexToConcatenate.toString());
                    
                    ++ indexToConcatenate;
                } while (! currentString.substring(0, 5).equals("00000"));
                
                // Retrieve the index where the element should be written.
                final int indexToWrite = Character.getNumericValue(currentString.charAt(5));
                
                // Write in password the element only if it is a correct index, and if nothing was written at this place already.
                if (8 > indexToWrite && 'z' == password.charAt(indexToWrite))
                {
                    password = password.substring(0, Character.getNumericValue(currentString.charAt(5))) + currentString.charAt(6) + password.substring(Character.getNumericValue(currentString.charAt(5)) + 1);
                }
            }

            return password;
        }
        catch (Exception e)
        {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return "";
        }
    }
}
