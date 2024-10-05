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
     * https://adventofcode.com/2016/day/2#part2
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
     * https://adventofcode.com/2016/day/3
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
     * https://adventofcode.com/2016/day/3#part2
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
     * https://adventofcode.com/2016/day/5
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
     * https://adventofcode.com/2016/day/5#part2
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
            System.err.println("An error occurred.");
            e.printStackTrace();
            return "";
        }
    }

    /*
     * Helper for the solution to day 6.
     * Get the frequencie by column of each character.
     * 
     * https://adventofcode.com/2016/day/6
     * 
     * @param numberOfCols: Number of columns in the problem.
     * @returns: A matrix with 26 lines for all letters, and numberOfCols columns to reprensent the frequencie of all letter
     *           in each column.
     */
    private static int[][] day_06_helper_getFrequenciesByColumn(final int numberOfCols)
    {
        // Get the puzzle input.
        final ArrayList<String> lines = ReadFile.getLines(6);

        // Create the matrix that will contains the number of each each letter for each column.
        int[][] letterFrequencies = new int[26][numberOfCols];

        // Initialize the table.
        for (int indexLetter = 0; 26 > indexLetter; ++indexLetter)
        {
            for (int indexColumn = 0; numberOfCols > indexColumn; ++indexColumn)
            {
                letterFrequencies[indexLetter][indexColumn] = 0;
            }
        }

        //  Iterate among all lines to change the frequencies of the different columns.
        for (String line : lines)
        {
            // Iterate among the letters of the current string.
            for (int charIndex = 0; numberOfCols > charIndex; ++charIndex)
            {
                // Retrieve the char frequencie that needs to be incremented on the current column.
                final char currentChar = line.charAt(charIndex);
                ++ letterFrequencies[currentChar - 'a'][charIndex];
            }
        }
        
        // Return the frequencie of each letter in each column.
        return letterFrequencies;
    }

    /*
     * Get solution for day 6 "Signals and Noise", Part 1.
     * https://adventofcode.com/2016/day/6
     *
     * @returns: Error-corrected password sent to Santa.
     */
    @SuppressWarnings("unused")
    private static String day_06_Part_1()
    {
        // Number of column of the problem.
        final int numberOfCols = 8;

        // Retrieve the frequencies of each letter, for all the column.
        final int[][] lettersFrequenciePerColumn = day_06_helper_getFrequenciesByColumn(numberOfCols);

        // Initialisation of the corrected password.
        String correctedPassword = "";
        
        // Iterating among all columns.
        for (int indexColumn = 0; numberOfCols > indexColumn; ++indexColumn)
        {
            int currentIndexLetterMax = 0;

            // Iterating among all letters to find which one is the most used.
            for(int indexLetter = 0; 26 > indexLetter; ++indexLetter)
            {
                // If the frequencie is strictly bigger, we update which 'letter' (by index) is the most used.
                if (lettersFrequenciePerColumn[indexLetter][indexColumn] > lettersFrequenciePerColumn[currentIndexLetterMax][indexColumn])
                {
                    currentIndexLetterMax = indexLetter;
                }
            }
            // Add to the password the corresponding character to the index with the biggest frequencie found.
            correctedPassword += (char)('a' + currentIndexLetterMax);
        }

        // Return the error-corrected password.
        return correctedPassword;
    }

    /*
     * Get solution for day 6 "Signals and Noise", Part 2.
     * https://adventofcode.com/2016/day/6#part2
     *
     * @returns: Error-corrected password sent to Santa when the less present element is the one sent.
     */
    @SuppressWarnings("unused")
    private static String day_06_Part_2()
    {
        // Number of column of the problem.
        final int numberOfCols = 8;

        // Retrieve the frequencies of each letter, for all the column.
        final int[][] lettersFrequenciePerColumn = day_06_helper_getFrequenciesByColumn(numberOfCols);

        // Initialisation of the corrected password.
        String correctedPassword = "";
        
        // Iterating among all columns.
        for (int indexColumn = 0; numberOfCols > indexColumn; ++indexColumn)
        {
            int currentIndexLetterMax = 0;

            // Iterating among all letters to find which one is the most used.
            for(int indexLetter = 0; 26 > indexLetter; ++indexLetter)
            {
                // If the frequencie is strictly smaller, we update which 'letter' (by index) is the most used.
                if (lettersFrequenciePerColumn[indexLetter][indexColumn] < lettersFrequenciePerColumn[currentIndexLetterMax][indexColumn])
                {
                    currentIndexLetterMax = indexLetter;
                }
            }
            // Add to the password the corresponding character to the index with the smallest frequencie found.
            correctedPassword += (char)('a' + currentIndexLetterMax);
        }

        // Return the error-corrected password.
        return correctedPassword;
    }

    /*
     * Helper for the solution to day 7.
     * Check if a given string respect the condition of the TLS IP element (having a ABBA form).
     * 
     * https://adventofcode.com/2016/day/7
     * 
     * @param elementOfIP: Element of the IP that we want to check if it contains ABBA.
     * @returns: A boolean athat states if the ABBA pattern is found.
     */
    private static Boolean day_07_helper_checkIfRespectConditionTLS(String elementOfIP)
    {
        // Boolean that check if the condition is respected.
        Boolean isRespectingConditionTLS = false;

        // Iterating among all possible 4 elements to check if the ABBA pattern is found.
        for (int charIndex = 3; elementOfIP.length() > charIndex; ++charIndex)
        {
            // If the ABBA pattern is found, place the return value to TRUE and stop looping for something already checked.
            if (elementOfIP.charAt(charIndex) == elementOfIP.charAt(charIndex - 3)
            && elementOfIP.charAt(charIndex - 1) == elementOfIP.charAt(charIndex - 2)
            && elementOfIP.charAt(charIndex) != elementOfIP.charAt(charIndex - 1))
            {
                isRespectingConditionTLS = true;
                break;
            }
        }

        // Return the boolean that states if the condition is respected.
        return isRespectingConditionTLS;
    }

    /*
     * Helper for the solution to day 7.
     * Add to a set the two first letters of the elements that may respect the SSL condition (having a ABA form).
     * 
     * https://adventofcode.com/2016/day/7
     * 
     * @param elementOfIP: Element of the IP that we want to check if it contains ABBA.
     * @param lettersThatRespectSSL: A set containing all the AB from the ABA form that are already found.
     */
    private static void day_07_helper_checkIfRespectConditionSSL(String elementOfIP, HashSet<String> lettersThatRespectSSL)
    {
        // Iterating among all three consecutive elements possible.
        for (int charIndex = 2; elementOfIP.length() > charIndex; ++charIndex)
        {
            // If the ABA pattern is found, we have something to add to the set.
            if (elementOfIP.charAt(charIndex) == elementOfIP.charAt(charIndex - 2)
            && (elementOfIP.charAt(charIndex) != elementOfIP.charAt(charIndex - 1)))
            {
                // Add to the set AB from the ABA form (to avoid redondancy).
                lettersThatRespectSSL.add("" + elementOfIP.charAt(charIndex) + elementOfIP.charAt(charIndex - 1));
            }
        }
    }

    /*
     * Get solution for day 7 "Internet Protocol Version 7", Part 1.
     * https://adventofcode.com/2016/day/7
     *
     * @returns: Number of IP that supports TLS.
     */
    @SuppressWarnings("unused")
    private static int day_07_Part_1()
    {
        // Get the puzzle input.
        ArrayList<String> lines = ReadFile.getLines(7);

        // Initialize the number of IP that supports TLS.
        int nbIPSupportingTLS = 0;

        // Pattern to search for with a regex (consecutive letters)
        final Pattern patternToSearch = Pattern.compile("[a-z]+");
        
        // Matcher that will contains the information the part of the IP adresses.
        Matcher matcherOfIP; 
        
        // Iterating among all IP adresses
        for (String line : lines)
        {
            // Boolean that states if the match is in the hypernet (inside the brackets)
            Boolean isCurrentStringInHypernet = false;
            
            // Intialize the matcher with the line to look at
            matcherOfIP = patternToSearch.matcher(line);

            // Boolean that states if a ABBA pattern is found outside the brackets
            Boolean isPatternFoundOutsideHypernet = false;
            
            // Looping while some sequence of the IP is found.
            while (matcherOfIP.find())
            {
                // If the position is odd, we are inside hypernet.
                if (isCurrentStringInHypernet)
                {
                    // If a ABBA pattern is found inside the hypernet, we know that this IP is not correct.
                    if (day_07_helper_checkIfRespectConditionTLS(line.substring(matcherOfIP.start(), matcherOfIP.end())))
                    {
                        // Stop looping and state that nothing is found.
                        isPatternFoundOutsideHypernet = false;
                        break;
                    }
                }
                // If the position is even, we are outside hypernet.
                else
                {
                    // The boolean is updated if it was not already true by checking the new part.
                    isPatternFoundOutsideHypernet |= day_07_helper_checkIfRespectConditionTLS(line.substring(matcherOfIP.start(), matcherOfIP.end()));
                }
                
                // Changing the value of if we are in the hypernet or not.
                isCurrentStringInHypernet = (! isCurrentStringInHypernet);
            }
            
            // If a pattern is found outside the hypernet (and not inside, in this case the boolean would be false)
            // Then we can increment the number of IP that respect our condition.
            if (isPatternFoundOutsideHypernet)
            {
                ++ nbIPSupportingTLS;
            }
        }

        // Return the total number of IP adress that support TLS.
        return nbIPSupportingTLS;
    }

    /*
     * Get solution for day 7 "Internet Protocol Version 7", Part 2.
     * https://adventofcode.com/2016/day/7#part2
     *
     * @returns: Number of IP that supports SSL.
     */
    @SuppressWarnings("unused")
    private static int day_07_Part_2()
    {
        // Get the puzzle input.
        final ArrayList<String> lines = ReadFile.getLines(7);
        
        // Initialize the number of IP that supports SSL.
        int nbIPSupportingSSL = 0;

        // Pattern to search for with a regex (consecutive letters)
        final Pattern patternToSearch = Pattern.compile("[a-z]+");
        
        // Matcher that will contains the information the part of the IP adresses.
        Matcher matcherOfIP; 
        
        // Iterating among all IP adresses
        for (String line : lines)
        {
            // Iterating two hashset to find if one ABA is found inside the hypernet and BAB outside the hypernet.
            HashSet<String> outsideElements = new HashSet<>();
            HashSet<String> insideElements = new HashSet<>();

            // Boolean that states if the match is in the hypernet (inside the brackets)
            Boolean isCurrentStringInHypernet = false;
            
            // Intialize the matcher with the line to look at
            matcherOfIP = patternToSearch.matcher(line);

            // While some elements of the IP are found, we continue iterating.
            while (matcherOfIP.find())
            {
                // If we are inside the hypernet, fill the other set with the values that looks like ABA.
                if (isCurrentStringInHypernet)
                {
                    day_07_helper_checkIfRespectConditionSSL(line.substring(matcherOfIP.start(), matcherOfIP.end()), insideElements);
                }
                // If we are outside the hypernet, fill the hypernet set with the values that looks like ABA.
                else
                {
                    day_07_helper_checkIfRespectConditionSSL(line.substring(matcherOfIP.start(), matcherOfIP.end()), outsideElements);
                }

                // Changing the value of if we are in the hypernet or not.
                isCurrentStringInHypernet = ! isCurrentStringInHypernet;
            }
            
            // Iterating among all ABA pattern found on the hypernet.
            for (String element: insideElements)
            {
                // If outside the hypernet BAB is found, we can count this line as a IP that support SSL and stop looping.
                if (outsideElements.contains("" + element.charAt(1) + element.charAt(0)))
                {
                    ++ nbIPSupportingSSL;
                    break;
                }
            }
        }

        // Return the number of IP that supports SSL.
        return nbIPSupportingSSL;
    }

    
    /*
     * Helper for the solution to day 8.
     * Find the matrix of 0 / 1 according to what should be on the screen.
     * 
     * https://adventofcode.com/2016/day/8
     * 
     * @returns: Matrix containing all elements after all the operation of the puzzle.
     */
    private static int[][] day_08_helper_getMatrixAfterOperations()
    {
        // Dimension of the matrix and creation of the matrix.
        final int nbLines = 6;
        final int nbCols = 50;
        int matrix[][] = new int[nbLines][nbCols];

        // Get the puzzle input.
        final ArrayList<String> lines = ReadFile.getLines(8);

        // Pattern to search for with a regex
        final Pattern patternToSearch = Pattern.compile("[0-9]+");
        
        // Matcher that will contains the information about how to turn and the distance to walk.
        Matcher matcherNumber; 

        // Iterating among all instructions
        for (String line: lines)
        {
            // Make the matcher find the elements on the current instruction.
            matcherNumber = patternToSearch.matcher(line);
            if (! matcherNumber.find())
            {
                return null;
            }
            // Find the first integer written on the line.
            final int firstInteger = Integer.valueOf(line.substring(matcherNumber.start(), matcherNumber.end()));
            
            if (! matcherNumber.find())
            {
                return null;
            }

            // Find the second integer written on the line.
            final int secondInteger = Integer.valueOf(line.substring(matcherNumber.start(), matcherNumber.end()));
            
            // If the rect instruction is written, all values on the rectangle should be .
            if (line.startsWith("rect"))
            {
                for (int indexLine = 0; firstInteger > indexLine; ++indexLine)
                {
                    for (int indexCol = 0; secondInteger > indexCol; ++indexCol)
                    {
                        matrix[indexCol][indexLine] = 1;
                    }
                }
            }

            // If the row instruction is written, all values on the row firstInteger should be moved secondInteger time.
            else if (line.contains("row"))
            {

                int [] lineFromMatrix = new int[nbCols];
                for (int index = 0; nbCols > index; ++index)
                {
                    lineFromMatrix[index] = matrix[firstInteger][index];
                }
                
                for (int columnIndex = 0; nbCols > columnIndex; ++columnIndex)
                {
                    matrix[firstInteger][columnIndex] = lineFromMatrix[(columnIndex + nbCols - secondInteger) % nbCols];
                }
            }
            // If the column instruction is written, all values on the column firstInteger should be moved secondInteger time.
            else if (line.contains("column"))
            {
                int [] columnFromMatrix = new int[nbLines];

                for (int index = 0; nbLines > index; ++index)
                {
                    columnFromMatrix[index] = matrix[index][firstInteger];
                }
                
                for (int rowIndex = 0; nbLines > rowIndex; ++rowIndex)
                {
                    matrix[rowIndex][firstInteger] = columnFromMatrix[(rowIndex + nbLines - secondInteger) % nbLines];
                }
            }
        }
        
        // Return the matrix of the state after all operations are made.
        return matrix;
    }

    /*
     * Get solution for day 8 "Two-Factor Authentication", Part 1.
     * https://adventofcode.com/2016/day/8
     *
     * @returns: Number of pixels that should be lit.
     */
    @SuppressWarnings("unused")
    private static int day_08_Part_1()
    {
        // Retrieve the matrix after all operations on the instructions.
        int[][] matrix = day_08_helper_getMatrixAfterOperations();

        // Initialize the variable that count the nummber of pixels that should be lit.
        int nbPixelsThatLit = 0;

        // Iterating among all lines
        for (int lineFromMatrix[]: matrix)
        {
            // Iterating among all pixels from the line
            for (int elementOfMatrix: lineFromMatrix)
            {
                // Sum with the new value (1 if it's on, 0 if it's off)
                nbPixelsThatLit += elementOfMatrix;
            }
        }

        // Return the number of pixels that should be lite on the screen.
        return nbPixelsThatLit;
    }

    /*
     * Get solution for day 8 "Two-Factor Authentication", Part 2.
     * https://adventofcode.com/2016/day/9#part2
     *
     * @returns: void. The answer is visual.
     */
    @SuppressWarnings("unused")
    private static void day_08_Part_2()
    {
        // Retrieve the matrix after all operations on the instructions.
        int[][] matrix = day_08_helper_getMatrixAfterOperations();

        // Display a new line
        System.out.println("");

        // Iterating among all lines
        for (int lineFromMatrix[]: matrix)
        {
            // Iterating among all pixels from the line
            for (int elementOfMatrix: lineFromMatrix)
            {
                // Display a square if it should be lit, and a space if it should not.
                System.out.print((1 == elementOfMatrix ? "#" : " "));
            }
            // Display a new line
            System.out.println("");
        }
    }
}
