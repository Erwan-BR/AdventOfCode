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

    /*
     * Get solution for day 1 "Inverse Captcha", Part 1.
     *  https://adventofcode.com/2017/day/1
     *
     * @returns: Captcha to proove Santa is not a human.
     */
    private static day_01_Part_1(): number
    {
        // Get puzzle input
        let inputOfExercise: string = ReadFile.getLine(1);

        // Value of the captcha.
        let solutionOfCaptcha: number = 0;
        
        // Iterating among all pairs that are side by side.
        for (let index: number = 1; inputOfExercise.length > index; ++index)
        {
            // If values are equal, then the value should be added to the captcha.
            if (inputOfExercise[index] == inputOfExercise[index - 1])
            {
                solutionOfCaptcha += Number(inputOfExercise[index]);
            }
        }
        
        // It's a circular string, so the first and the last may match.
        if (inputOfExercise[0] == inputOfExercise[inputOfExercise.length - 1])
        {
            solutionOfCaptcha += Number(inputOfExercise[0]);
        }

        // Return the computed captcha.
        return solutionOfCaptcha;
    }

    /*
     * Get solution for day 1 "Inverse Captcha", Part 2.
     *  https://adventofcode.com/2017/day/1#part2
     *
     * @returns: Second captcha to proove Santa is not a human.
     */
    private static day_01_Part_2(): number
    {
        // Get puzzle input
        let inputOfExercise: string = ReadFile.getLine(1);

        // Value of the captcha.
        let solutionOfCaptcha: number = 0;

        // Iterating among all pairs halfway around. No need to iterate two times for checking the same values.
        for (let index: number = 0; (inputOfExercise.length / 2) > index; ++index)
        {
            // If values are equal, then the value should be added 2 times to the captcha:
            // One time for index, the other for the halfwaray around.
            if (inputOfExercise[index] == inputOfExercise[index + (inputOfExercise.length / 2)])
            {
                solutionOfCaptcha += 2 * Number(inputOfExercise[index]);
            }
        }

        // Return the computed captcha.
        return solutionOfCaptcha;
    }
}
