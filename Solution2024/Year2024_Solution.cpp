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
        nullptr,
    };

    // Table for method of part 2
    static long long (*secondPartTable[])() = {
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
