from Year2015_Solution import Year2015_Solution

if __name__ == "__main__":
    for day in range(1, 26):
        for isFirstPart in (True, False):
            print(f"Solution for year 2015, day {day:02d} part {'1' if isFirstPart else '2'} is: {Year2015_Solution.getSolution(day, isFirstPart)}")
