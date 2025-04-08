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
        nullptr,
    };

    // Table for method of part 2
    static long long (*secondPartTable[])() = {
        nullptr,
        &day_01_Part_2,
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
* Search for the distance between first and second list.
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
* Compute the similarity score of the two given lists.
*
* @returns: Similarity score of the two given lists.
*/
long long Year2024_Solution::day_01_Part_2()
{
    // Creating iterators to use regex
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