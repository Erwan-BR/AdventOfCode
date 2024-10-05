package Solution2016;

import java.lang.reflect.Method;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
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
     *  https://adventofcode.com/2016/day/1
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
     *  https://adventofcode.com/2016/day/1#part2
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
}
