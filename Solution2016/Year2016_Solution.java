package Solution2016;

import java.lang.reflect.Method;

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
}
