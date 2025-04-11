#ifndef _YEAR2024_SOLUTION_HPP_
#define _YEAR2024_SOLUTION_HPP_

#include <iostream>
#include <regex>
#include <unordered_map>
#include <queue>

#include "ReadFile.hpp"

class Year2024_Solution
{
    public:
        static long long getSolution(const unsigned int day, const bool isFirstPart);
    
    private:
        static long long day_01_Part_1();
        static long long day_01_Part_2();

        static long long day_02_Part_1();
        static long long day_02_Part_2();

        static bool day_02_helper_isSafeReport(const std::vector<int>& report, unsigned int valueToCheckFirst, unsigned int valueToCheckSecond, unsigned int valueToSkip);
        static bool day_02_helper_isSafeIncreasing(const std::vector<int>& values, const unsigned int& indexToSkip);
        static bool day_02_helper_isSafeDecreasing(const std::vector<int>& values, const unsigned int& indexToSkip);
};

#endif // _YEAR2024_SOLUTION_HPP_
