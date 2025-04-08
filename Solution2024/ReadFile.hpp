#ifndef _READFILE_HPP_
#define _READFILE_HPP_

#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <string>

class ReadFile
{
    private:
        static std::string getNameOfFile(const int day);

    public:
        static std::string getLine(const int day);
        static std::vector<std::string> getLines(const int day);
};
#endif // _READFILE_HPP_
