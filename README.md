# Advent Of Code

## Description

The aim of this project is to strengthen my Python skills by solving problems proposed by the Advent Of Code for different years. It is an excellent opportunity to improve my skills in algorithms, reading text files and regular expressions (REGEX). Each solution is designed to be efficient and well-structured, with readability and performance in mind.

The Advent Of Code problems are published daily in December, and cover a variety of challenges ranging from string manipulation to more complex algorithms.

## Structure of the project

The project is structured into several directories, each corresponding to a year of the Advent Of Code. Within each directory, the challenges are organised by day, with a dedicated Python file for each problem.

```
AdventOfCode/
│
├── Global/
│ ├── globals.py
│ ├── __init__.py
│
├── Solution_2015/
│ ├── textfiles
│ │   ├── 01.txt
│ │   ├── 01.txt
│ │   ├── 01.txt
│ ├── Year2015_Solution.py
│ ├── __init__.py
│
├── .../
│
├── Solution_2023/
│ ├── textfiles
│ │   ├── 01.txt
│ │   ├── 01.txt
│ │   ├── 01.txt
│ ├── Year2023_Solution.py
│ ├── __init__.py
│
└── main.py
```

## Setting up the project

### Prerequisites

To run this project, you must have Python 3.12.4 installed on your machine. You can check the version of Python by running the following command:

```bash
python --version
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

3. Launch the file main.py:

```bash
python3 main.py
```

4. Customize the output displayed (optionnal): In main.py, you can choose to display the answer you want. Let's imagine you want the solution for year 20XX, day Y. You have to modify the main.py file to have this:

```python
if "__main__" == __name__:
    print(Sol_20XX.getSolution(Y, True)) # True for Part One, False for Part Two
```

### Compilation

As these are Python scripts, no compilation is necessary. Just make sure that Python is correctly installed on your machine.

## Tickets and Solutions

These tickets contain the list of solutions to be implemented for each year, and for each ticket an associated branch is created, allowing the work on each year to be dissociated:

- [Ticket 02: Year 2015](https://github.com/Erwan-Br/AdventofCode/issues/2)
- [Ticket 03: Year 2016](https://github.com/Erwan-Br/AdventofCode/issues/3)
- [Ticket 04: Year 2017](https://github.com/Erwan-Br/AdventofCode/issues/4)
- ...
- [Ticket 10: Year 2023](https://github.com/Erwan-Br/AdventofCode/issues/10)

## Contribute

Contributions are welcome! If you would like to suggest improvements or correct errors, don't hesitate to submit a pull request or open an issue.

## Authors

- **[Erwan BROUDIN](https://github.com/Erwan-Br)** - *Principal author*

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for more details.
