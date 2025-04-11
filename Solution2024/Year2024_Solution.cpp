#include "Year2024_Solution.hpp"

/*
* Function called outside the class to obtain the solution for any day, for the first or second part.
* @param day: Day for which we want to retrieve the solution.
* @param isFirstPart: Boolean indicating whether we want to retrieve the solution for day 1 or day 2.
*        - True:  Returns the solution for the first part of the problem.
*        - False: Returns the solution for the second part of the problem.
*
* @returns: Answer of the given problem.
*/
long long Year2024_Solution::getSolution(const unsigned int day, const bool isFirstPart)
{
    // Table for method of part 1
    static long long (*firstPartTable[])() = {
        nullptr,
        &day_01_Part_1,
        &day_02_Part_1,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
    };

    // Table for method of part 2
    static long long (*secondPartTable[])() = {
        nullptr,
        &day_01_Part_2,
        &day_02_Part_2,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
    };

    // Checking index
    if (0 == day || 25 < day)
    {
        std::cout << "The day should be between 1 and 25" << std::endl;
        return 0LL;
    }

    // Checking if solution exist for the first part of the given day
    if (isFirstPart)
    {
        if (nullptr == firstPartTable[day])
        {
            std::cout << "Solution for year 2024, day " << day << ", part one has not yet been developed." << std::endl;

            return 0LL;
        }
        // Call the method for the first part
        return (*firstPartTable[day])();
    }
    // Checking if solution exist for the second part of the given day
    if (nullptr == firstPartTable[day])
    {
        std::cout << "Solution for year 2024, day " << day << ", part two has not yet been developed." << std::endl;

        return 0LL;
    }

    // Call the method for the second part
    return (*secondPartTable[day])();
}

/*
* Get solution for day 1, Part 1.
* https://adventofcode.com/2015/day/1
*
* @returns: Total distance the two given lists.
*/
long long Year2024_Solution::day_01_Part_1()
{
    // Retrieve puzzle input
    const std::vector<std::string> linesOfInput = ReadFile::getLines(1);

    // Regex used to find both numbers.
    const std::regex numberRegex(R"(\d+)");

    // Create two priority queue that will store value in the order so we don't have to sort them at the end.
    std::priority_queue<int> valueCol1;
    std::priority_queue<int> valueCol2;

    // Creating iterators to use regex
    std::sregex_iterator words_begin;

    const std::sregex_iterator words_end = std::sregex_iterator();

    // Iterating among all lines.
    for (const std::string line: linesOfInput)
    {
        // Search for the start of the regex.
        words_begin = std::sregex_iterator(line.begin(), line.end(), numberRegex);

        std::sregex_iterator indexIterator = words_begin;
        
        // Add the first value converted as an integer.
        valueCol1.push(std::stoi((*indexIterator).str()));

        ++ indexIterator;

        // Add the second value converted as an integer.
        valueCol2.push(std::stoi((*indexIterator).str()));
    }

    long long result = 0;

    // Compute the difference between each biggest value and delete them from the total result.
    while (! valueCol1.empty())
    {
        result += abs(valueCol1.top() - valueCol2.top());

        valueCol1.pop();
        valueCol2.pop();
    }

    return result;
}

/*
* Get solution for day 1, Part 2.
* https://adventofcode.com/2015/day/1#part2
*
* @returns: Similarity score of the two given lists.
*/
long long Year2024_Solution::day_01_Part_2()
{
    // Retrieve puzzle input
    const std::vector<std::string> linesOfInput = ReadFile::getLines(1);

    // Regex used to find both numbers.
    const std::regex numberRegex(R"(\d+)");

    // Create two unordered map that will store values and their occurences.
    std::unordered_map<unsigned int, unsigned int> valueCol1;
    std::unordered_map<unsigned int, unsigned int> valueCol2;

    std::sregex_iterator words_begin;

    const std::sregex_iterator words_end = std::sregex_iterator();

    // Iterating among all lines.
    for (const std::string line: linesOfInput)
    {
        // Search for the start of the regex.
        words_begin = std::sregex_iterator(line.begin(), line.end(), numberRegex);

        std::sregex_iterator indexIterator = words_begin;
        
        // Increment the number of time the value has been found in the first list.
        ++ valueCol1[std::stoi((*indexIterator).str())];

        ++ indexIterator;

        // Increment the number of time the value has been found in the second list.
        ++ valueCol2[std::stoi((*indexIterator).str())];
    }

    long long result = 0;

    // Compute the similarty of the given lists.
    for (const std::pair<unsigned int, unsigned int>& pairOfVal: valueCol1)
    {
        result += pairOfVal.first * valueCol2[pairOfVal.first];
    }

    return result;
}

/*
* Helper for the solution to day 2.
* https://adventofcode.com/2015/day/2
* 
* @param values: Check if the values are considered 'safe' when increasing.
* @param indexToSkip: Used for part 2. We want to 'skip' some value to avoid delete them for real.
*
* @returns: true if the values sequence is safe by increasing, false otherwise.
*/
bool Year2024_Solution::day_02_helper_isSafeIncreasing(const std::vector<int>& values, const unsigned int& indexToSkip)
{
    bool shouldBeAdded = true;

    for (size_t index = 1; values.size() > index; ++index)
    {
        // If the index has to be skipped, we check a bigger window
        if (index == indexToSkip)
        {
            // If the index to skip is the last one, no bigger window is available
            if ((values.size() - 1) == index)
            {
                continue;
            }
            // Checking previous value with NEXT value.
            if (((values[index + 1] - values[index - 1]) <= 0) || ((values[index + 1] - values[index - 1]) >= 4))
            {
                shouldBeAdded = false;
                break;
            }
        }
        // No need to make some check once again on the value to skip.
        else if (index == (indexToSkip + 1))
        {
            continue;
        }
        // Check if values are increasing and if they are not increasing more than 4.
        else if (((values[index] - values[index - 1]) <= 0) || ((values[index] - values[index - 1]) >= 4))
        {
            shouldBeAdded = false;
            break;
        }
    }

    return shouldBeAdded;
}

/*
* Helper for the solution to day 2.
* https://adventofcode.com/2015/day/2

* @param values: Check if the values are considered 'safe' when decreasing.
* @param indexToSkip: Used for part 2. We want to 'skip' some value to avoid delete them for real.
*
* @returns: true if the values sequence is safe by decreasing, false otherwise.
*/
bool Year2024_Solution::day_02_helper_isSafeDecreasing(const std::vector<int>& values, const unsigned int& indexToSkip)
{
    bool shouldBeAdded = true;
    
    for (size_t index = 1; values.size() > index; ++index)
    {
        // If the index has to be skipped, we check a bigger window
        if (index == indexToSkip)
        {
            // If the index to skip is the last one, no bigger window is available
            if ((values.size()) - 1 == index)
            {
                continue;
            }
            // Checking previous value with NEXT value.
            if (((values[index - 1] - values[index + 1]) <= 0) || ((values[index - 1] - values[index + 1]) >= 4))
            {
                shouldBeAdded = false;
                break;
            }
        }
        // No need to make some check once again on the value to skip.
        else if (index == (indexToSkip + 1))
        {
            continue;
        }
        // Check if values are decreasing and if they are not decreasing more than 4.
        else if (((values[index - 1] - values[index]) <= 0) || ((values[index - 1] - values[index]) >= 4))
        {
            shouldBeAdded = false;
            break;
        }
    }

    return shouldBeAdded;
}

/*
* Helper for the solution to day 2.
* https://adventofcode.com/2015/day/2

* @param report: Check if the report is safe.
* @param valueToCheckFirst: Used to check if the report is increasing or decreasing. First value of the table.
* @param valueToCheckSecond: Used to check if the report is increasing or decreasing. Second value of the table.
* @param valueToSkip: Used to check if the report safe even if we skip a value.
*
* @returns: true if the values sequence is safe by decreasing, false otherwise.
*/
bool Year2024_Solution::day_02_helper_isSafeReport(const std::vector<int>& report, unsigned int valueToCheckFirst, unsigned int valueToCheckSecond, unsigned int valueToSkip)
{
    // Reports has to be stricly increasing / decreasing.
    if (report[valueToCheckSecond] == report[valueToCheckFirst])
    {
        return false;
    }
    
    // Call the increasing or decreasing method according to the order of the first two values.
    if (report[valueToCheckSecond] > report[valueToCheckFirst])
    {
        return day_02_helper_isSafeIncreasing(report, valueToSkip);
    }
    
    return day_02_helper_isSafeDecreasing(report, valueToSkip);
}

/*
* Get solution for day 2, Part 1.
* https://adventofcode.com/2015/day/2
*
* @returns: Number of safe reports.
*/
long long Year2024_Solution::day_02_Part_1()
{
    // Retrieve puzzle input
    const std::vector<std::string> linesOfInput = ReadFile::getLines(2);

    // Regex used to find the numbers written
    const std::regex numberRegex(R"(\d+)");

    // Vector that will store the values found at each line
    std::vector<int> values;

    // Value to return
    long long numberOfSafeReport = 0;

    std::sregex_iterator words_begin;

    const std::sregex_iterator words_end = std::sregex_iterator();

    // Iterate among all reports
    for (const std::string line: linesOfInput)
    {
        words_begin = std::sregex_iterator(line.begin(), line.end(), numberRegex);

        // write in values the different values that we found on a report
        for (std::sregex_iterator indexIterator = words_begin; words_end != indexIterator; ++indexIterator)
        {
            values.push_back(std::stoi((*indexIterator).str()));
        }

        if (day_02_helper_isSafeReport(values, 0, 1, values.size()))
        {
            ++ numberOfSafeReport;
        }

        // Erase values that are stored on values for the next report.
        values.clear();
    }
    return numberOfSafeReport;
}

/*
* Get solution for day 2, Part 1.
* https://adventofcode.com/2015/day/2
*
* @returns: Number of safe reports when we can delete one value only of the report.
*/
long long Year2024_Solution::day_02_Part_2()
{
    // Retrieve puzzle input
    const std::vector<std::string> linesOfInput = ReadFile::getLines(2);

    // Regex used to find the numbers written
    const std::regex numberRegex(R"(\d+)");

    // Vector that will store the values found at each line
    std::vector<int> values;

    // Value to return
    long long numberOfSafeReport = 0;

    std::sregex_iterator words_begin;

    const std::sregex_iterator words_end = std::sregex_iterator();

    // Iterate among all reports
    for (const std::string line: linesOfInput)
    {
        words_begin = std::sregex_iterator(line.begin(), line.end(), numberRegex);

        for (std::sregex_iterator indexIterator = words_begin; words_end != indexIterator; ++indexIterator)
        {
            values.push_back(std::stoi((*indexIterator).str()));
        }

        // Check if we have to consider the report safe when deleting the first element.
        if (day_02_helper_isSafeReport(values, 1, 2, 0))
        {
            ++ numberOfSafeReport;
            values.clear();
            continue;
        }

        // Check if we have to consider the report safe when deleting the second element.
        if (day_02_helper_isSafeReport(values, 0, 2, 1))
        {
            ++ numberOfSafeReport;
            values.clear();
            continue;
        }

        // We start iterating from at 2 because skipping 0 and 1 are already considered (edge cases).
        for (size_t indexToSkip = 2; values.size() > indexToSkip; ++indexToSkip)
        {
            if (day_02_helper_isSafeReport(values, 0, 1, indexToSkip))
            {
                ++ numberOfSafeReport;
                break;
            }
        }
        values.clear();
    }

    return numberOfSafeReport;
}
