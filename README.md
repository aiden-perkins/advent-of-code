# Advent of Code

This repository contains my solutions for the [Advent of Code](https://adventofcode.com/) programming challenges.
My goal is the eventually earn all 50 stars for every year, but I am far from that (50/50 for 2023, 22/50 for 2022, 41/50 for 2021, 5/50 for 2020, & 4/50 for 2015).
I also want to try and use a different language for the previous years, some I want to try are golang, c++, zig, & rust.

___Input:___

- To get an input you first need to get your session token from [the Advent of Code website](https://adventofcode.com/) and put it in a file called `.session` in the root folder.
- To run do `python3 in.py [day] (year)`, if you don't put a year it will default to 2024.
- You may need to make a folder called `puzzle-inputs` if it errors, this is where the inputs are cached.

___Running:___

- All the days require the input.txt to be in the root folder and will not work otherwise, in.py automatically puts it in the correct place so if you used that you can ignore where input.txt is.
- To run any specific day all you need to do is `python3 -m [year].[day]` and just replace `year` and `day` with whatever year/day you want.
- Most days will print out the answers for both part 1 & 2 but this varies depending on what the answer actually is (2021/13 for example).

___Other:___

- [t.py](t.py) is just what I use as a template for starting new days.
- [BinaryTree.py](2021/BinaryTree.py) Just a data structure I used for 2021 day 18, it's from one of my classes in college, so I easily understood how to use it without having to lookup stuff online.
- The 2024-betterer folder was added because often when I finish puzzles, I like going back and use a different approach that might be better, more efficient, or cleaner, etc., but I also want to preserve the code that I used to get an answer. So the 2024 folder holds the code I wrote under time pressure and the 2024-betterer folder holds code I wrote after that I like more, not all days/parts have a betterer solution.

___Time:___

This is how fast each one is in ms on average running it 100 times.
Running on my laptop.

| Day | 2015 | 2020 | 2021        | 2022   | 2023        | 2024        | 2024-betterer                                      |
|:----|:-----|:-----|:------------|:-------|:------------|:------------|:---------------------------------------------------|
| 1   |      |      | 11.92       | 11.80  | 13.83       | 15.99       | simplified - 11.30*                                |
| 2   |      |      | 12.20       | 12.26  | 13.73       | 18.28       |                                                    |
| 3   |      |      | 11.65       | 11.43  | 27.07       | 19.46       | simplified with regex - 18.23                      |
| 4   |      |      | 279.74      | 12.53  | 12.19       | 24.42       | loop instead of 8 ifs (more readable) - 328.33*    |
| 5   |      |      | 84.59       | 11.62  | 13.83       | 21.43       |                                                    |
| 6   |      |      | 11.21       | 11.49  | 107.04      | 9020.19     | speed - TODO                                       |
| 7   |      |      | ~15 seconds | 12.25  | 16.41       | 2562.82     | speed - TODO                                       |
| 8   |      |      | 13.66       | 211.69 | 40.01       | 15.29       |                                                    |
| 9   |      |      | 547.38      | 314.86 | 14.21       | ~50 seconds | speed - TODO                                       |
| 10  |      |      | 14.09       | 11.52  | 45.03       | 37.9        |                                                    |
| 11  |      |      | 17.60       | 204.10 | 354.86      | 310.17      |                                                    |
| 12  |      |      | 1217.83     |        | 1460.42     | 234.46      |                                                    |
| 13  |      |      | 21.53       |        | 234.77      | 1394.66     | speed & no library - 20.58                         |
| 14  |      |      | 11.93       |        | 506.90      | 1475.25     | speed - TODO                                       |
| 15  |      |      | 892.94      |        | 15.58       | 37.62       |                                                    |
| 16  |      |      | 13.31       |        | 1546.16     | TODO        |                                                    |
| 17  |      |      | 65.85       |        | 1164.86     | TODO        |                                                    |
| 18  |      |      | 1762.92     |        | 124.92      | 481.79      | binary search - TODO                               |
| 19  |      |      | 462.55      |        | 20.50       | 557.68      |                                                    |
| 20  |      |      | 953.36      |        | 91.43       | ~22 minutes | speed - improve, currently ~4 1/2 mins             |
| 21  |      |      |             |        | 2989.46     | 17.88       |                                                    |
| 22  |      |      |             |        | 2004.95     | 6055.64     | use bit shifting and simplify - improve speed more |
| 23  |      |      |             |        | ~25 seconds | 53.35       |                                                    |
| 24  |      |      |             |        | 404.26      | 12.87^      | Write general solution - TODO                      |
| 25  |      |      |             |        | ~7 seconds  | 98.45       |                                                    |

\* = only part 1

^ = not a general solution (hardcoded parts)

~ = Is not an average, takes too long
