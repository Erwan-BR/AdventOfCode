import { execPath } from "process";
import { ReadFile } from "./ReadFile.js";

export class Year2017_Solution
{
    /*
     * Function called outside the class to obtain the solution for any day, for the first or second part.
     * @param day: Day for which we want to retrieve the solution.
     * @param isFirstPart: Boolean indicating whether we want to retrieve the solution for day 1 or day 2.
     *        - True:  Returns the solution for the first part of the problem.
     *        - False: Returns the solution for the second part of the problem.
     *
     * @returns: Answer of the given problem.
     */
    public static getSolution(day: number, isFirstPart: boolean) : number | string
    {
        // Create the method name.
        const nameOfFunction = `day_${day.toString().padStart(2, '0')}_Part_${isFirstPart ? "1" : "2"}`;

        // Try to find the method
        const methodToCall = (Year2017_Solution as any)[nameOfFunction] as (() => number | string) | undefined;
        
        // If the method is found, call it
        if (methodToCall)
        {
            try
            {
                return methodToCall();
            }
            catch(error)
            {
                return "An error occured on the method called.";
            }
        }
        // Else, display a message to warn the user that the code is not done yet.
        else
        {
            return `Solution for year 2017, day ${day}, part ${isFirstPart ? "one" : "two"} has not yet been developed.`;
        }
    }
}