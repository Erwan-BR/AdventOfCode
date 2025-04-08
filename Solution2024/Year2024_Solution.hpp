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
};

#endif // _YEAR2024_SOLUTION_HPP_
