import { execPath } from "process";
import { ReadFile } from "./ReadFile.js";

type day_07_elementOfTower = {
    weightOfElement: number;
    weightHolding: number;
    elementsHolding: string[];
    isHolded: boolean
};

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
     * https://adventofcode.com/2017/day/1
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
     * https://adventofcode.com/2017/day/1#part2
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

    /*
     * Get solution for day 2 "Corruption Checksum", Part 1.
     * https://adventofcode.com/2017/day/2
     *
     * @returns: Checksum of the spreadsheet.
     */
    private static day_02_Part_1(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(2);

        // Initialize the number of spreasheet.
        let checksumOfSpreadsheet: number = 0;

        // Regular expression to find numbers on the spreadsheet.
        const regexToFindNumbers: RegExp = /\d+/g;

        // Iterating among all lines.
        for (const line of lines)
        {
            // Retrieve all numbers found on the line.
            const numbersOfLineInString: string[] | null = line.match(regexToFindNumbers);
            
            // if nothing is found, go to next line.
            if (null == numbersOfLineInString)
            {
                continue;
            }

            // Initialize min and max values that are found on these line.
            let minValue: number = Infinity;
            let maxValue: number = -1;
            
            // Iterate among the number of those line of the spreadsheet and compare
            // To get the biggest and the smallest value of the line.
            for (const numberInString of numbersOfLineInString)
            {
                minValue = Math.min(minValue, Number(numberInString));
                maxValue = Math.max(maxValue, Number(numberInString));
            }

            // Add to the checksum the current difference between largest and smallest value.
            checksumOfSpreadsheet += maxValue - minValue;
        }

        // Return the computed checksum.
        return checksumOfSpreadsheet;
    }

    /*
     * Get solution for day 2 "Corruption Checksum", Part 2.
     * https://adventofcode.com/2017/day/2#part2
     *
     * @returns: Sum of each row result. Result for one line is the only whole integer when performing division between 2 values.
     */
    private static day_02_Part_2(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(2);

        // Initialize the number of spreasheet.
        let checksumOfSpreadsheet: number = 0;

        // Regular expression to find numbers on the spreadsheet.
        const regexToFindNumbers: RegExp = /\d+/g;

        // Iterating among all lines.
        for (const line of lines)
        {
            // Retrieve all numbers found on the line.
            const numbersOfLineInString: string[] | null = line.match(regexToFindNumbers);
            
            // if nothing is found, go to next line.
            if (null == numbersOfLineInString)
            {
                continue;
            }

            // Create a table containing all numbers on the current line
            let numbersOfLineInNumber: number[] = [];
            
            // For all number that are on the lines, we repeat the same process
            for (const numberInString of numbersOfLineInString)
            {
                // Get the newValue as an integer
                const newValue: number = Number(numberInString)
                
                // Try to find if it can be divided or if it can divide another value already seen
                for (let index: number = 0; numbersOfLineInNumber.length > index; ++index)
                {
                    // Check if it can be divided by the previous value
                    if (0 == numbersOfLineInNumber[index] % newValue)
                    {
                        // If it's possible, add the quotient to the checksum.
                        checksumOfSpreadsheet += numbersOfLineInNumber[index] / newValue;
                        break;
                    }
                    // Check if it can divide by the previous value
                    if (0 == newValue % numbersOfLineInNumber[index])
                    {
                        // If it's possible, add the quotient to the checksum.
                        checksumOfSpreadsheet += newValue / numbersOfLineInNumber[index];
                        break;
                    }
                }
                // Add the value that is not making the division inside the table of values seen.
                numbersOfLineInNumber.push(newValue);
            }
        }

        // Return the computed checksum.
        return checksumOfSpreadsheet;
    }

    /*
     * Helper for the solution to day 3, part 2.
     * Fill the outside square according to how it should be filled.
     * 
     * https://adventofcode.com/2016/day/3#part2
     * 
     * @param currentSquare: Square that we have. The outside square needs to be filled only.
     * @param target: The minimal value we should have.
     * @returns: -1 if no value written is big enough, and if one returns it.
     */
    private static day_03_helper_fillOutsideSquare(currentSquare: number[][], target: number) : number
    {
        // Computing the size of the current square.
        const size: number = currentSquare.length;
        
        // Filling the right side
        for (let index = size - 2; 0 < index; --index)
        {
            // Sum is made from the previous column and the element bellow
            currentSquare[index][size - 1] = currentSquare[index][size - 2] + currentSquare[index - 1][size - 2] + currentSquare[index + 1][size - 2]
                                             + currentSquare[index + 1][size - 1];
            
            
            // If the target is exceeded, we return the value computed.
            if (target <= currentSquare[index][size - 1])
            {
                return currentSquare[index][size - 1];
            }
        }

        // Filling the top-right corner
        currentSquare[0][size - 1] = currentSquare[1][size - 2] + currentSquare[1][size - 1];
        
        // If the target is exceeded, we return the value computed.
        if (target <= currentSquare[0][size - 1])
        {
            return currentSquare[0][size - 1];
        }

        // Filling the top side
        for (let index = size - 2; 0 < index; --index)
        {
            // Sum is made from the row indexed 1 and the element on the right.
            currentSquare[0][index] = currentSquare[1][index - 1] + currentSquare[1][index] + currentSquare[1][index + 1]
                                                + currentSquare[0][index + 1];
            
            // If the target is exceeded, we return the value computed.
            if (target <= currentSquare[0][index])
            {
                return currentSquare[0][index];
            }
        }

        // Filling the top-left corner
        currentSquare[0][0] = currentSquare[0][1] + currentSquare[1][1];
        
        // If the target is exceeded, we return the value computed.
        if (target <= currentSquare[0][0])
        {
            return currentSquare[0][0];
        }

        // Filling the left side
        for (let index = 1; (size - 1) > index; ++index)
        {
            // Sum is made from the column indexed 1 and the element above.
            currentSquare[index][0] = currentSquare[index - 1][1] + currentSquare[index][1] + currentSquare[index + 1][1]
                                                + currentSquare[index - 1][0];
            
            
            // If the target is exceeded, we return the value computed.
            if (target <= currentSquare[index][0])
            {
                return currentSquare[index][0];
            }
        }

        // Filling the bottom-left corner
        currentSquare[size - 1][0] = currentSquare[size - 2][0] + currentSquare[size - 2][1];
        
        // If the target is exceeded, we return the value computed.
        if (target <= currentSquare[size - 1][0])
        {
            return currentSquare[size - 1][0];
        }

        // Filling the bottom side
        for (let index = 1; (size - 1) > index; ++index)
        {
            // Sum is made from the row above and the element on the left.
            currentSquare[size - 1][index] = currentSquare[size - 2][index - 1] + currentSquare[size - 2][index] + currentSquare[size - 2][index + 1]
                                                + currentSquare[size - 1][index - 1];
            
            
            // If the target is exceeded, we return the value computed.
            if (target <= currentSquare[size - 1][index])
            {
                return currentSquare[size - 1][index];
            }
        }

        // Filling the bottom-right side
        currentSquare[size - 1][size - 1] = currentSquare[size - 1][size - 2] + currentSquare[size - 2][size - 1] + currentSquare[size - 2][size - 2];
        
        // If the target is exceeded, we return the value computed.
        if (target <= currentSquare[size - 1][size - 1])
        {
            return currentSquare[size - 1][size - 1];
        }

        // If nothing has been returned previously, it means that the target is not exceeded.
        // We return -1 and we will have to make the square bigger and re-call this function.
        return -1;
    }

    /*
     * Helper for the solution to day 3, part 2.
     * Create a square bigger than the current one by adding 0 on the outside.
     * 
     * https://adventofcode.com/2016/day/3#part2
     * 
     * @param currentSquare: Square that we already have.
     * @returns: The same square with 0 around it (above, bellow, on the right and the left).
     */
    private static day_03_helper_constructBiggerSquare(currentSquare: number[][]) : number[][]
    {
        // Create the newSquare that has to be created.
        let newSquare: number[][] = [];

        // Add a line filled with 0 at the top of the new square.
        newSquare.push(Array.from({ length: currentSquare.length + 2 }, () => 0))
        
        // For each line of the square we have, add a 0 to the left, the line and then a 0 on the newSquare
        for(let line of currentSquare)
        {
            newSquare.push([0, ...line, 0]);
        }

        // Add a line filled with 0 at the top of the new square.
        newSquare.push(Array.from({ length: currentSquare.length + 2 }, () => 0))

        // Return the new square created.
        return newSquare;
    }

    /*
     * Get solution for day 3 "Spiral Memory", Part 1.
     * https://adventofcode.com/2017/day/3
     *
     * @returns: Manhattan distance between the input and the center of the square.
     */
    private static day_03_Part_1(): number
    {
        // Get the puzzle input.
        const line: string = ReadFile.getLine(3);

        // Convert the puzzle input into a number.
        const target: number = Number(line);

        // Edge case: If the target is one, the distance is 0.
        if (1 == target)
        {
            return 0;
        }
        
        // Initialize the size of the square bellow the one that contains the target.
        let sizeSquareBellow: number = 1;

        // Initialize the distance between the target and the venter of the square.
        let manhattanDistance: number = 1;
        
        
        // Find the size of the biggest square that does not contains the target value.
        while ((sizeSquareBellow + 2) * (sizeSquareBellow + 2) < target)
        {
            // Each iteration, the size of the square increase two times.
            sizeSquareBellow += 2;

            // Increment the distance by one to get through this new element.
            ++ manhattanDistance;
        }
        
        // Now, we now that our target is on the next square.
        // We need to find wich side is it so we can compute the distnce to go to the middle. 
        let middleOfZoneWhereValueIs: number = sizeSquareBellow * sizeSquareBellow + Math.ceil(sizeSquareBellow / 2);

        // The target is on the bottom side
        if (sizeSquareBellow * sizeSquareBellow + (3 * (sizeSquareBellow + 1)) < target)
        {
            middleOfZoneWhereValueIs += 3 * (sizeSquareBellow + 1);
        }
        // The target is on the left side
        else if (sizeSquareBellow * sizeSquareBellow + (2 * (sizeSquareBellow) + 1) < target)
        {
            middleOfZoneWhereValueIs += 2 * (sizeSquareBellow + 1);
        }
        // The target is on the top side
        else if (sizeSquareBellow * sizeSquareBellow + sizeSquareBellow + 1 < target)
        {
            middleOfZoneWhereValueIs += sizeSquareBellow + 1;
        }
        
        // Add the distance to go to the middle of the side.
        // The distance to go from a middle to the center is already computed on the while loop.
        manhattanDistance += Math.abs(middleOfZoneWhereValueIs - target);

        // Return the Manhattan distance between the target and the center of the square.
        return manhattanDistance;
    }

    /*
     * Get solution for day 3 "Spiral Memory", Part 2.
     * https://adventofcode.com/2017/day/3#part2
     *
     * @returns: First value greater than the target value by following the snake to fill the square.
     */
    private static day_03_Part_2(): number
    {
        // Get the puzzle input.
        const line: string = ReadFile.getLine(3);

        // Convert the puzzle input into a number.
        const target: number = Number(line);
        
        // Edge case: If the target is smaller than 1, the first bigger value is 1.
        if (1 >= target)
        {
            return 1;
        }

        // Initialize the square that will contains the number.
        let square: number[][] = [[1]];

        // Initialize the last returned value of the fillind square.
        let lastReturnedValue: number = -1;
        
        // While we did not get a value bigger than the target, we have to make the square bigger and fill it.
        while (-1 == lastReturnedValue)
        {
            // Increase the dimension of the square.
            square = Year2017_Solution.day_03_helper_constructBiggerSquare(square);
            
            // Retrieve the value returned by the filling that may be -1 if nothing is bigger than the target
            // or a value if it exceeds the target.
            lastReturnedValue = Year2017_Solution.day_03_helper_fillOutsideSquare(square, target);
        }

        // Return the first value greater or equal than the target value.
        return lastReturnedValue;
    }

    /*
     * Get solution for day 4 "High-Entropy Passphrases", Part 1.
     * https://adventofcode.com/2017/day/4
     *
     * @returns: Number of valid passphrase.
     */
    private static day_04_Part_1(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(4);
        
        // Initialize the number of valid passphrases.
        let numberOfValidPassPhrase: number = 0;

        // Regular expression to find the words in each line.
        const regexToFindWords: RegExp = /[a-z]+/g;

        // Iterating among all line to check if they are valid passphrase.
        for (const line of lines)
        {
            // Find all words from the line.
            const wordsFromLine: string[] | null = line.match(regexToFindWords);

            // If the line is empty, continue to the next line.
            if (null == wordsFromLine)
            {
                continue;
            }

            // Create a set that contains each words separated.
            const setOfWords: Set<String> = new Set(wordsFromLine);

            // If the size of the set is equal to the size of the table, it means that they are all different.
            // Therefore this is a valid passphrase.
            if (setOfWords.size == wordsFromLine.length)
            {
                ++ numberOfValidPassPhrase;
            }
        }

        // Return the total number of valid passphrase found.
        return numberOfValidPassPhrase;
    }

    /*
     * Get solution for day 4 "High-Entropy Passphrases", Part 2.
     * https://adventofcode.com/2017/day/4#part2
     *
     * @returns: Number of valid passphrase with the new policy.
     */
    private static day_04_Part_2(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(4);
        
        // Initialize the number of valid passphrases.
        let numberOfValidPassPhrase: number = 0;

        // Regular expression to find the words in each line.
        const regexToFindWords: RegExp = /[a-z]+/g;

        // Iterating among all line to check if they are valid passphrase.
        for (const line of lines)
        {
            // Find all words from the line.
            const wordsFromLine: string[] | null = line.match(regexToFindWords);

            // If the line is empty, continue to the next line.
            if (null == wordsFromLine)
            {
                continue;
            }

            // Create a set that contains each words separated.
            const setOfWords: Set<String> = new Set();

            // For each word found, add it but ordered in alphabetical order.
            // Like this, 'abc' and 'cba' are going to be the same on the set.
            for (const word of wordsFromLine)
            {
                setOfWords.add(word.split("").sort().join());
            }

            // If the size of the set is equal to the size of the table, it means that there is no anagrams.
            // Therefore this is a valid passphrase.
            if (setOfWords.size == wordsFromLine.length)
            {
                ++ numberOfValidPassPhrase;
            }
        }

        // Return the total number of valid passphrase found.
        return numberOfValidPassPhrase;
    }

    /*
     * Get solution for day 5 "A Maze of Twisty Trampolines, All Alike", Part 1.
     * https://adventofcode.com/2017/day/5
     *
     * @returns: Number of steps needed to reach the exit.
     */
    private static day_05_Part_1(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(5);
        
        // Puzzle input with numbers. Used to konw how much jump are going to be done.
        let possibleJumps: number[] = [];
        
        // Fill the possibleJumps table with the different jumps.
        for (const line of lines)
        {
            possibleJumps.push(Number(line));
        }
        
        // Initialize a variables to keep track of which jump should be done.
        let currentIndex: number = 0;

        // Initialize a variable to keep track of the number of steps are required to reach the exit.
        let numberOfSteps: number = 0;
        
        // While out index is inside the bounds, we need to jump again.
        while (0 <= currentIndex && possibleJumps.length > currentIndex)
        {
            // Increment the number of steps needed.
            ++ numberOfSteps;

            // Change the index based on the preivous value of the possible jump, and then increment the number of jump
            // on that steps.
            currentIndex += possibleJumps[currentIndex]++;
        }

        // Return the number of steps needed to reach the exit.
        return numberOfSteps;
    }

    /*
     * Get solution for day 5 "A Maze of Twisty Trampolines, All Alike", Part 2.
     * https://adventofcode.com/2017/day/5#part2
     *
     * @returns: Number of steps needed to reach the exit when jump can be decremented.
     */
    private static day_05_Part_2(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(5);
        
        // Puzzle input with numbers. Used to konw how much jump are going to be done.
        let possibleJumps: number[] = [];
        
        // Fill the possibleJumps table with the different jumps.
        for (const line of lines)
        {
            possibleJumps.push(Number(line));
        }
        
        // Initialize a variables to keep track of which jump should be done.
        let currentIndex: number = 0;

        // Initialize a variable to keep track of the number of steps are required to reach the exit.
        let numberOfSteps: number = 0;
        
        // While out index is inside the bounds, we need to jump again.
        while (0 <= currentIndex && possibleJumps.length > currentIndex)
        {
            // Increment the number of steps needed.
            ++ numberOfSteps;

            // If the offet is less than three, increment the value of the jump.
            if (3 > possibleJumps[currentIndex])
            {
                currentIndex += possibleJumps[currentIndex]++;
            }
            // If the offset is greater or equal than 3, decrement the value of the jump. 
            else
            {
                currentIndex += possibleJumps[currentIndex]--;
            }
        }

        // Return the number of steps needed to reach the exit.
        return numberOfSteps;
    }

    /*
     * Helper for the solution to day 6.
     * Find the number of redistribution cycle before having a configuration already seen.
     * 
     * https://adventofcode.com/2016/day/6
     * 
     * @param banks: State of the banks in the first place.
     * @returns: The number of redistributions cycle it took to come to a known state.
     */
    private static day_06_helper_findNumberStepsTwoSameStates(banks: number[]): number
    {
        // Initialize the number of steps needed.
        let numberOfSteps: number = 0;

        // Initialize a set that contains all set already known.
        let setOfSeenStates: Set<string> = new Set();

        // While the current state is not on the set of seen states, we continue to make redistribution cycle.
        // We join with '-' to avoid considering (11, 2) and (1, 12) as the same element.
        while (! setOfSeenStates.has(banks.join('_')))
        {
            // Ad the current state to the states seen and increment the number of steps required.
            setOfSeenStates.add(banks.join('_'));
            ++ numberOfSteps;
            
            // Initialize and find the index of the bank with the maximal value to empty.
            let indexOfBankToEmpty: number = 0;
            for (let index = 1; banks.length > index; ++index)
            {
                if (banks[indexOfBankToEmpty] < banks[index])
                {
                    indexOfBankToEmpty = index;
                }
            }
            
            // Initialize the number of elements that has to be redistributed.
            const numberOfElementsToGive: number = banks[indexOfBankToEmpty];
            // Empty the current bank.
            banks[indexOfBankToEmpty] = 0;

            // Give to the bank the redistribution, one by one.
            for (let nbElementsToGive = numberOfElementsToGive; 0 < nbElementsToGive; --nbElementsToGive)
            {
                // Increment the index of the bank that receives the amound. Re-init if it is equal to the size.
                ++ indexOfBankToEmpty;
                if (banks.length == indexOfBankToEmpty)
                {
                    indexOfBankToEmpty = 0;
                }
                // Increment the value of the current bank.
                ++ banks[indexOfBankToEmpty];
            }
        }

        // Return the number of steps that was needed to find a state already seen.
        return numberOfSteps;
    }

    /*
     * Get solution for day 6 "Memory Reallocation", Part 1.
     * https://adventofcode.com/2017/day/6
     *
     * @returns: Number of steps needed find two times the same bank state after redistribution cycle.
     */
    private static day_06_Part_1(): number
    {
        // Get the puzzle input.
        const line: string = ReadFile.getLine(6);
        
        // Regex to find all the numbers from the input.
        const regexToFindNumbers: RegExp = /\d+/g;

        // Table containing the number as strings.
        const numbersOfLineInString: string[] | null = line.match(regexToFindNumbers);

        // If no number are found, there is an issue and we can return -1 as an error.
        if (null == numbersOfLineInString)
        {
            return -1;
        }

        // Initialize the bank table that contains the number as integers.
        let banks: number[] = [];
        
        // Add the numbers to the bank
        for (const numberString of numbersOfLineInString)
        {
            banks.push(Number(numberString));
        }
        
        // Retrieve the number of steps needed to find 2 times the same state.
        const numberOfSteps: number = Year2017_Solution.day_06_helper_findNumberStepsTwoSameStates(banks);

        // Return the number of steps that was needed.
        return numberOfSteps;
    }

    /*
     * Get solution for day 6 "Memory Reallocation", Part 2.
     * https://adventofcode.com/2017/day/6#part2
     *
     * @returns: Number of steps needed find two times the same bank state after redistribution cycle,
     *           and then we try to find once again two times the same bank state after redistribution cycle.
     */
    private static day_06_Part_2(): number
    {
        // Get the puzzle input.
        const line: string = ReadFile.getLine(6);
        
        // Regex to find all the numbers from the input.
        const regexToFindNumbers: RegExp = /\d+/g;

        // Table containing the number as strings.
        const numbersOfLineInString: string[] | null = line.match(regexToFindNumbers);

        // If no number are found, there is an issue and we can return -1 as an error.
        if (null == numbersOfLineInString)
        {
            return -1;
        }

        // Initialize the bank table that contains the number as integers.
        let banks: number[] = [];
        
        // Add the numbers to the bank
        for (const numberString of numbersOfLineInString)
        {
            banks.push(Number(numberString));
        }
        
        // Get two similar states a first time.
        Year2017_Solution.day_06_helper_findNumberStepsTwoSameStates(banks);

        // Find another time two similar states.
        let numberOfSteps: number = Year2017_Solution.day_06_helper_findNumberStepsTwoSameStates(banks);

        // Return the number of steps that was needed.
        return numberOfSteps;
    }

    /*
     * Helper for the solution to day 7.
     * Construct the information about the tower (exxcept the weight holding by each program).
     * 
     * https://adventofcode.com/2016/day/7
     * 
     * @returns: A mapping that indicates for each program's name, it's weight, the programs it's directly holding,
     *           0 as the weight it's holding and if it's holded if this program is holded or not.
     */
    private static day_07_helper_constructMapWithInfo() : Map<string, day_07_elementOfTower>
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(7);

        // Create a map that will contains all elements, and the information of those elements.
        let allElementsOfTower: Map<string, day_07_elementOfTower> = new Map();

        // Create a regex to find all elements of the tower.
        const regexToFindWords: RegExp = /[a-z]+/g;
        const regexToFindNumbers: RegExp = /[0-9]+/g;

        // Iterate among all holding instructions.
        for (const line of lines)
        {
            // Find the table of elements of the tower in the current line.
            const elementsOfTower: string[] | null = line.match(regexToFindWords);
            const weightOfCurrentElement: number | null = Number(line.match(regexToFindNumbers));

            // If an uncorrect line is found, continue to the next one.
            if (null == elementsOfTower || null == weightOfCurrentElement)
            {
                continue;
            }

            // If the first element is not in the map, we never seen it.
            // State that it exists and it's not holded yet.
            if (! allElementsOfTower.has(elementsOfTower[0]))
            {
                allElementsOfTower.set(elementsOfTower[0], {weightOfElement: weightOfCurrentElement,
                                                            weightHolding: 0,
                                                            elementsHolding: [],
                                                            isHolded: false});
            }
            // If the element was found, we can setup it's weight.
            else
            {
                allElementsOfTower.get(elementsOfTower[0]).weightOfElement = weightOfCurrentElement;
            }

            // For all the other elements, we can for sure say that they are holded.
            for (let index = 1; elementsOfTower.length > index; ++index)
            {
                // Add the element holded to the holder.
                allElementsOfTower.get(elementsOfTower[0]).elementsHolding.push(elementsOfTower[index]);
                
                // If it was never seen, create the element and set that it's holded.
                if (! allElementsOfTower.has(elementsOfTower[index]))
                {
                    allElementsOfTower.set(elementsOfTower[index], {weightOfElement: 0, weightHolding: 0, elementsHolding: [], isHolded: true});
                }
                // Else, just state the element is holded.
                else
                {
                    allElementsOfTower.get(elementsOfTower[index]).isHolded = true;
                }
            }
        }

        // Return the mapping that contains all information about the program.
        return allElementsOfTower;
    }

    /*
     * Helper for the solution to day 7.
     * Fill a maping with the weights of all the program in the branch to avoid computing it multiple times.
     * 
     * https://adventofcode.com/2016/day/7
     * 
     * @param currentProgram: Program we are currently looking, to check for the weight of the branch.
     * @param mapOfTower: Map that contains as the keys the different programs, and the values are the all information of those programs.
     * @returns: Weight of the branch starting from currentProgram.
     */
    private static day_07_helper_fillWeightsOfMap(currentProgram: string, mapOfTower: Map<string, day_07_elementOfTower>) : number
    {
        // Intialize a variable with the weight of the branch starting from the currentProgram.
        let totalWeightHolded: number = mapOfTower.get(currentProgram).weightOfElement;
        
        // Adding the weight of all childrens.
        for (const elementHoldedByThisProgram of mapOfTower.get(currentProgram).elementsHolding)
        {
            totalWeightHolded += Year2017_Solution.day_07_helper_fillWeightsOfMap(elementHoldedByThisProgram, mapOfTower);
        }
        // Store the weight of the program and sub-programs in the map.
        mapOfTower.get(currentProgram).weightHolding = totalWeightHolded;

        // Return the weight of this branch.
        return totalWeightHolded;
    }
    
    /*
     * Helper for the solution to day 7.
     * Find by starting from the bottom the weight that should be adapted to have a balanced tower.
     * 
     * https://adventofcode.com/2016/day/7
     * 
     * @param currentProgram: Program weight we are currently looking, and for it's children too.
     * @param mapOfTower: Map that contains as the keys the different programs, and the values are the all information of those programs.
     * @param weightDiff: Difference of weight that should be applied to an element starting from this program.
     * @returns: The adjusted weight of the element that is not the correct weight. -1 if multiple elements should be changed.
     */
    private static day_07_helper_findRecursivelyWeightToAdapt(currentProgram: string, mapOfTower: Map<string, day_07_elementOfTower>, weightDiff: number) : number
    {
        // Edge case : We don't have children anymore. The weight should be change at a program that does not hold anything.
        if (0 == mapOfTower.get(currentProgram).elementsHolding.length)
        {
            return mapOfTower.get(currentProgram).weightOfElement + weightDiff;
        }

        // Initialize two variables for the weight, and check if all children are the same weight.
        let weightFound1: string = "";
        let weightFound2: string = "";

        // Initialize a boolean that states if weight 1 is found multiple times
        // Usefull if the configuration we have on the children is weightFound1, weightFound1, weightFound1, weightFound2.
        let isWeightFound1MultipleTime: boolean = false;

        // Initialize a variable to check which weight is problematic to continue on this branch.
        let isWeightFound1Problematic: boolean = false;

        // Iterating among all children.
        for (const nameOfElement of mapOfTower.get(currentProgram).elementsHolding)
        {
            // If no weight is written, write in the place 1
            if ("" == weightFound1)
            {
                weightFound1 = nameOfElement;
            }
            // If weightFound1 is written and the new is the same, we may want to stop if it's the second time we see this weight
            // And a different weight is already stored on weightFound2.
            else if (mapOfTower.get(nameOfElement).weightHolding == mapOfTower.get(weightFound1).weightHolding)
            {
                isWeightFound1MultipleTime = true;
                // If another weight was found, weightFound2 was problematic.
                if (""  != weightFound2)
                {
                    isWeightFound1Problematic = false;
                    break;
                }
            }
            // If the weight of the subbranch is different than the weightFound1, we can store the new weight.
            else if ("" == weightFound2)
            {
                weightFound2 = nameOfElement;

                // If we found multiple times the first weight and we have now the second weight, the second weight is the issue.
                if (isWeightFound1MultipleTime)
                {
                    isWeightFound1Problematic = false;
                    break;
                }
            }
            // If the weight found is the same as weight 2, it means that weight 1 is problematic because it's weight is different.
            else if (mapOfTower.get(nameOfElement).weightHolding == mapOfTower.get(weightFound2).weightHolding)
            {
                isWeightFound1Problematic = true;
                break;
            }
            // Here, both values are written and a third value is discovered. Return an invalid value.
            else
            {
                return -1;
            }

        }

        // If all children have the same weight, the problem is coming from this program.
        if ("" == weightFound2)
        {
            return mapOfTower.get(currentProgram).weightOfElement + weightDiff;
        }

        // If the first weight is problematic, we have to search on the corresponding branch.
        // We also re-compute the weight difference because it might be 0 from the first iteration.
        if (isWeightFound1Problematic)
        {
            return Year2017_Solution.day_07_helper_findRecursivelyWeightToAdapt(weightFound1, mapOfTower, mapOfTower.get(weightFound2).weightHolding - mapOfTower.get(weightFound1).weightHolding);
        }

        // If the second weight is problematic, we have to search on the corresponding branch.
        // We also re-compute the weight difference because it might be 0 from the first iteration.
        return Year2017_Solution.day_07_helper_findRecursivelyWeightToAdapt(weightFound1, mapOfTower, mapOfTower.get(weightFound1).weightHolding - mapOfTower.get(weightFound2).weightHolding);
    }    
    
    /*
     * Get solution for day 7 "Recursive Circus", Part 1.
     * https://adventofcode.com/2017/day/7
     *
     * @returns: Name of the program that is at the bottom.
     */
    private static day_07_Part_1(): string
    {
        // Retrieve the map with all informations concerning the program.
        const allElementsOfTower: Map<string, day_07_elementOfTower> = Year2017_Solution.day_07_helper_constructMapWithInfo();

        // Retrieve the only element that is not holded by anyone and return it.
        for (const [nameOfElement, characteristicsOfElement] of allElementsOfTower)
        {
            if (! characteristicsOfElement.isHolded)
            {
                return nameOfElement;
            }
        }

        // Return an empty string if the input is not correctly written.
        return "";
    }

    /*
     * Get solution for day 7 "Recursive Circus", Part 2.
     * https://adventofcode.com/2017/day/7#part2
     *
     * @returns: Adjusted weight of an element of the tower to balance it.
     */
    private static day_07_Part_2(): number
    {
        // Retrieve the map with all informations concerning the program.
        const allElementsOfTower: Map<string, day_07_elementOfTower> = Year2017_Solution.day_07_helper_constructMapWithInfo();

        // Retrieve the name of the program that is at the bottom to start filling the weights.
        const nameOfBottomProgram: string = Year2017_Solution.day_07_Part_1();

        // Fill the weights of each branch.
        Year2017_Solution.day_07_helper_fillWeightsOfMap(nameOfBottomProgram, allElementsOfTower);

        // Retrieve the adpated weight from the tower.
        return Year2017_Solution.day_07_helper_findRecursivelyWeightToAdapt(nameOfBottomProgram, allElementsOfTower, 0);
    }

    /*
     * Get solution for day 8 "I Heard You Like Registers", Part 1.
     * https://adventofcode.com/2017/day/8
     *
     * @returns: Maximal value in registers after all operation are done.
     */
    private static day_08_Part_1(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(8);

        // Create a maping that will contains the name of the registers and their value.
        let mapOfRegisters: Map<string, number> = new Map();

        // Regex to find the different elements of the operation.
        const regexToFindElements: RegExp = /[^ .]+/g;

        // Iterate among all lines that are the isntruction to follow.
        // All lines should be created like this : {Register} inc/dec {integer} if {otherRegister} condition {integer}
        for (const line of lines)
        {
            // Retrieve the elements of the current operation.
            const elementsOfLine: string[] | null = line.match(regexToFindElements);

            // If there is not the correct amount of elements, there is an issue with this line.
            if (null == elementsOfLine || 7 != elementsOfLine.length)
            {
                continue;
            }

            // if one of the two register has not been discovered yet, add them with the initial value 0.
            if (! mapOfRegisters.has(elementsOfLine[0]))
            {
                mapOfRegisters.set(elementsOfLine[0], 0); 
            }
            if (! mapOfRegisters.has(elementsOfLine[4]))
            {
                mapOfRegisters.set(elementsOfLine[4], 0); 
            }

            // Initialize the value that should be added (or retrieved) if the condition is true.
            const valueToIncrOrDecr: number = Number(elementsOfLine[2]) * ("inc" == elementsOfLine[1] ? 1 : -1);
            
            // Retrieve the value to compare with a register.
            const valueToCompare: number = Number(elementsOfLine[6])

            // For all the possible operations, check if the symbol is the same and if the condition is true.
            // If both conditions are true, we can update the register. 
            if (("==" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) == valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
            }
            else if ((">=" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) >= valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
            }
            else if (("<=" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) <= valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
            }
            else if ((">" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) > valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
            }
            else if (("<" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) < valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
            }
            else if (("!=" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) != valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
            }
        }

        // Initialize the maximal value in a register at the end.
        let maximalValueInRegisters: number = - Infinity;

        // Take the max value between both of them.
        for (const [el, valueOfRegister] of mapOfRegisters)
        {
            maximalValueInRegisters = Math.max(maximalValueInRegisters, valueOfRegister);
        }

        // Reurn the maximal value found.
        return maximalValueInRegisters;
    }

    /*
     * Get solution for day 8 "I Heard You Like Registers", Part 2.
     * https://adventofcode.com/2017/day/8#part2
     *
     * @returns: Maximal value in a register ever seen.
     */
    private static day_08_Part_2(): number
    {
        // Get the puzzle input.
        const lines: string[] = ReadFile.getLines(8);

        // Create a maping that will contains the name of the registers and their value.
        let mapOfRegisters: Map<string, number> = new Map();

        // Regex to find the different elements of the operation.
        const regexToFindElements: RegExp = /[^ .]+/g;

        // Maximale value ever found.
        let maximalValueRegistered: number = 0;

        // Iterate among all lines that are the isntruction to follow.
        // All lines should be created like this : {Register} inc/dec {integer} if {otherRegister} condition {integer}
        for (const line of lines)
        {
            // Retrieve the elements of the current operation.
            const elementsOfLine: string[] | null = line.match(regexToFindElements);

            // If there is not the correct amount of elements, there is an issue with this line.
            if (null == elementsOfLine || 7 != elementsOfLine.length)
            {
                continue;
            }

            // if one of the two register has not been discovered yet, add them with the initial value 0.
            if (! mapOfRegisters.has(elementsOfLine[0]))
            {
                mapOfRegisters.set(elementsOfLine[0], 0); 
            }
            if (! mapOfRegisters.has(elementsOfLine[4]))
            {
                mapOfRegisters.set(elementsOfLine[4], 0); 
            }

            // Initialize the value that should be added (or retrieved) if the condition is true.
            const valueToIncrOrDecr: number = Number(elementsOfLine[2]) * ("inc" == elementsOfLine[1] ? 1 : -1);
            
            // Retrieve the value to compare with a register.
            const valueToCompare: number = Number(elementsOfLine[6])

            // For all the possible operations, check if the symbol is the same and if the condition is true.
            // If both conditions are true, we can update the register, and update the max value encoutered.
            if (("==" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) == valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr);
                maximalValueRegistered = Math.max(maximalValueRegistered, mapOfRegisters.get(elementsOfLine[0]));
            }
            else if ((">=" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) >= valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
                maximalValueRegistered = Math.max(maximalValueRegistered, mapOfRegisters.get(elementsOfLine[0]));
            }
            else if (("<=" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) <= valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
                maximalValueRegistered = Math.max(maximalValueRegistered, mapOfRegisters.get(elementsOfLine[0]));
            }
            else if ((">" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) > valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
                maximalValueRegistered = Math.max(maximalValueRegistered, mapOfRegisters.get(elementsOfLine[0]));
            }
            else if (("<" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) < valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
                maximalValueRegistered = Math.max(maximalValueRegistered, mapOfRegisters.get(elementsOfLine[0]));
            }
            else if (("!=" == elementsOfLine[5]) && (mapOfRegisters.get(elementsOfLine[4]) != valueToCompare))
            {
                mapOfRegisters.set(elementsOfLine[0], mapOfRegisters.get(elementsOfLine[0]) + valueToIncrOrDecr); 
                maximalValueRegistered = Math.max(maximalValueRegistered, mapOfRegisters.get(elementsOfLine[0]));
            }
        }

        // Reurn the maximal value ever found.
        return maximalValueRegistered;
    }

    /*
     * Get solution for day 9 "Stream Processing", Part 1.
     * https://adventofcode.com/2017/day/9
     *
     * @returns: Total score of the stream.
     */
    private static day_09_Part_1(): number
    {
        // Get the puzzle input.
        const line: string = ReadFile.getLine(9);
        
        // Initialize a nested level and a score used to keep track of the point that we are making.
        let currentNestedLevel: number = 0;
        let totalScore: number = 0;

        // Initialize a boolean to know if we are in the garbage, and do not mind of { then.
        let isInGarbage: boolean = false;

        // Iterating among everything in the stream.
        for (let index = 0; line.length > index; ++index)
        {
            // If the next element should be cancelled, skip the following one.
            if ('!' == line[index])
            {
                ++ index;
                continue;
            }
            // If we are in the garbage, we should only look if we have a end of garbage as the following character.
            if (isInGarbage)
            {
                if ('>' == line[index])
                {
                    isInGarbage = false;
                }
                continue;
            }
            // Oppening a new group, therefore the nested level increase.
            if ('{' == line[index])
            {
                ++ currentNestedLevel;
            }
            // Closing a group so the score goes up and the nested level decrease.
            else if ('}' == line[index])
            {
                totalScore += currentNestedLevel;
                -- currentNestedLevel;
            }
            // Beginning of the garbage.
            else if ('<' == line[index])
            {
                isInGarbage = true;
            }
        }

        // Return the total score of the stream.
        return totalScore;
    }

    /*
     * Get solution for day 9 "Stream Processing", Part 2.
     * https://adventofcode.com/2017/day/9#part2
     *
     * @returns: Number of elements in the stream that are going in the garbage, except the cancelled ones..
     */
    private static day_09_Part_2(): number
    {
        // Get the puzzle input.
        const line: string = ReadFile.getLine(9);

        // Initialize an integer counting the number of elements that are going in the garbage.
        let nbElementOnGarbageNotCancelled: number = 0;
        
        // Initialize a boolean to know if we are in the garbage, and do not mind of { then.
        let isInGarbage: boolean = false;
        

        // Iterating among everything in the stream.
        for (let index = 0; line.length > index; ++index)
        {
            // If the next element should be cancelled, skip the following one.
            if ('!' == line[index])
            {
                ++ index;
            }
            // If we are in the garbage, we should look if we are exiting, or if we increase the number of elements inside the garbage.
            else if (isInGarbage)
            {
                if ('>' == line[index])
                {
                    isInGarbage = false;
                }
                else
                {
                    ++ nbElementOnGarbageNotCancelled;
                }
            }
            // Beginning of the garbage.
            else if ('<' == line[index])
            {
                isInGarbage = true;
            }
        }

        // Return the number of non-canceled characters that are within the garbage 
        return nbElementOnGarbageNotCancelled;
    }
}
