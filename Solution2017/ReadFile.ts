import * as fs from 'fs';

export class ReadFile
{
    /**
     * Function used to get the path of the input file. Input files should be in a subfolder "textfiles", and named
     * x.txt where is x is the number of the day. if 10 > x, write 0x (for example 03.txt for day 3).
     *
     * @param day Day when the problem was published.
     * @return String representing the path of the textfile.
     */
    private static getNameOfFile(day: number) : string
    {
        return `./textfiles/${day.toString().padStart(2, '0')}.txt`;
    }

    /**
     * Function used to get the string in the input file.
     * Handle error when oppening the file.
     *
     * @param day Day when the problem was published.
     * @return A string that contains the input of the problem.
     */
    public static getLine(day: number) : string
    {
        try
        {
            const line: string = fs.readFileSync(ReadFile.getNameOfFile(day), 'utf-8');
            return line;
        }
        catch (error)
        {
            console.error("An error occurred, the file cannot be opened.");
            return "";
        }
    }

    /**
     * Function used to get the strings in the input file that contains multiple lines.
     * Handle error when oppening the file.
     *
     * @param day Day when the problem was published.
     * @return A list of strings that contains the input of the problem.
     */
    public static getLines(day: number) : string[]
    {
        try
        {
            const lines: string[] = fs.readFileSync(ReadFile.getNameOfFile(day), 'utf-8').split('\n');
            return lines;
        }
        catch (error)
        {
            console.error("An error occurred, the file cannot be opened.");
            return [];
        }
    }
}