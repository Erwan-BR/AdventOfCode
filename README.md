# Advent Of Code

## Description

The aim of this project is to strengthen my skills by solving problems proposed by the Advent Of Code for different years. It is an excellent opportunity to improve my skills in algorithms, reading text files and regular expressions (REGEX). Each solution is designed to be efficient and well-structured, with readability and performance in mind.

For each year, I've decided to choose a different language in order to revise languages I know (Python, Java), or to improve my skills in languages I'm less familiar with (JavaScript).

The Advent Of Code problems are published daily in December, and cover a variety of challenges ranging from string manipulation to more complex algorithms.

## Structure of the project

The project is structured into several directories, each corresponding to a year (and therefore a language) of the Advent Of Code. Within each directory, the challenges are organised by day, with a dedicated file for each problem.

```
AdventOfCode/
│
├── Solution_2015/
│ ├── textfiles
│ │   ├── 01.txt
│ │   ├── 01.txt
│ │   ├── 01.txt
│ ├── Year2015_Solution.py
│ ├── ReadFile.py
│ ├── main.py
│
├── Solution_2016/
│ ├── textfiles
│ │   ├── 01.txt
│ │   ├── 01.txt
│ │   ├── 01.txt
│ ├── Year2016_Solution.java
│ ├── ReadFile.java
│ ├── main.java
│
├── Solution_2017/
│ ├── textfiles
│ │   ├── 01.txt
│ │   ├── 01.txt
│ │   ├── 01.txt
│ ├── Year2015_Solution.ts
│ ├── ReadFile.ts
│ ├── main.ts
│
├── .../
│
├── Solution_2023/
│ ├── textfiles
│ │   ├── 01.txt
│ │   ├── 01.txt
│ │   ├── 01.txt
│
└── main.sh
```

## Setting up the project

### Prerequisites

To run this project, you must have:
- For year 2015: Python 3.12.6 installed on your machine. You can check the version of Python by running the following command:

```bash
python --version
```

- For year 2016: Java 21.0.4 installed on your machine. You can check the version of Java by running the following command:

```bash
java --version
```

- For year 2017: Node 20.18.0 installed on your machine. You can check the version of Node by running the following command:

```bash
node --version
```

### Installation

1. Clone this repository on your local machine using the following command:

```bash
git clone https://github.com/Erwan-Br/AdventofCode.git
```

2. Open the repository:

```bash
cd AdventofCode
```

3. Launch the file main.sh:

On Windows:
```bash
sh main.sh -y <yearNumber>
```

On Linux:
```bash
./main.sh -y <yearNumber>
```

4. Customize the output displayed (optionnal): Fo each year, In main.xx, you can choose to display the answer you want. For the year 2015, you might want to display only a few responses so you would have to change main.py to:

```python
if "__main__" == __name__:
    print(Year2015_Solution.getSolution(<dayNumber>, True)) # True for Part One, False for Part Two
```

### Compilation

The file main.sh will do everything for you, just launch it with the correct arguments!

## Tickets and Solutions

These tickets contain the list of solutions to be implemented for each year, and for each ticket an associated branch is created, allowing the work on each year to be dissociated:

- [Ticket 02: Year 2015](https://github.com/Erwan-Br/AdventofCode/issues/2)
- [Ticket 03: Year 2016](https://github.com/Erwan-Br/AdventofCode/issues/3)
- [Ticket 04: Year 2017](https://github.com/Erwan-Br/AdventofCode/issues/4)
- ...
- [Ticket 10: Year 2023](https://github.com/Erwan-Br/AdventofCode/issues/10)

## Use the code to find your answers

All the problems retrieve input from text files, so it is possible to find your answer by using my code and changing the contents of the text files.

I encourage you to try and understand the algorithms involved, and if you have any questions please don't hesitate to ask, I'll be happy to answer them.

## Contribute

Contributions are welcome! If you would like to suggest improvements or correct errors, don't hesitate to submit a pull request or open an issue.

## Authors

- **[Erwan BROUDIN](https://github.com/Erwan-Br)** - *Principal author*

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for more details.
