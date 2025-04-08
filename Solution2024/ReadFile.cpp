#include "ReadFile.hpp"

std::string ReadFile::getNameOfFile(const int day)
{
    std::string representationOfDay = "textfiles/";

    representationOfDay += (day < 10) ? "0" + std::to_string(day) : std::to_string(day);

    representationOfDay += ".txt";

    return representationOfDay;
}

std::string ReadFile::getLine(const int day)
{
    // Instantiation of a string that will represent the successive lines.
    std::string currentLine = "";

    // Instantiation of a fstream object which is a file.
    std::fstream readingFile;

    const std::string intputFileName = getNameOfFile(day);

    // Opening the file in reading mode.
    readingFile.open(intputFileName, std::ios::in);

    // Checking if the file is correctly opened.
    if (readingFile.is_open())
    {
        getline(readingFile, currentLine);

        // Closing the file because we do not need it anymore.
        readingFile.close();
    }

    return currentLine;
}

std::vector<std::string> ReadFile::getLines(const int day)
{
    std::vector<std::string> linesOfProblem;


    // Instantiation of a fstream object which is a file.
    std::fstream readingFile;

    const std::string intputFileName = getNameOfFile(day);

    // Opening the file in reading mode.
    readingFile.open(intputFileName, std::ios::in);

    // Checking if the file is correctly opened.
    if (readingFile.is_open())
    {
        // Instantiation of a string that will represent the successive lines.
        std::string currentLine;

        // Looping while we can get the following line (while another exists in fact).
        while(getline(readingFile, currentLine))
        {
            currentLine.erase(currentLine.find_last_not_of(" \t\r\n") + 1);
            linesOfProblem.push_back(currentLine);
        }

        // Closing the file because we do not need it anymore.
        readingFile.close();
    }

    return linesOfProblem;
}
