# Advent of Code

This repository contains my solutions for the [Advent of Code](https://adventofcode.com/) programming challenges.
My goal is the eventually earn all 50 stars for every year, but I am far from that (50/50 for 2023, 22/50 for 2022, 41/50 for 2021, 5/50 for 2020, & 4/50 for 2015).
I also want to try and use a different language for the previous years, some I want to try are golang, c++, zig, & rust.

___Input:___

- To get an input you first need to get your session token from [the Advent of Code website](https://adventofcode.com/) and put it in a file called `.session` in the root folder.
- To run do `python3 in.py` and then enter the day/year, if you don't put a year it will default to 2024.
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

| Day | 2015 | 2020 | 2021 | 2022 | 2023 | 2024    | 2024-betterer |
|:----|:-----|:-----|:-----|:-----|:-----|:--------|:--------------|
| 1   |      |      |      |      |      | 15.99   | 11.30*        |
| 2   |      |      |      |      |      | 18.28   |               |
| 3   |      |      |      |      |      | 19.46   | 18.23         |
| 4   |      |      |      |      |      | 24.42   | 328.33*       |
| 5   |      |      |      |      |      | 21.43   |               |
| 6   |      |      |      |      |      | 9020.19 |               |
| 7   |      |      |      |      |      | 2562.82 |               |
| 8   |      |      |      |      |      | 15.29   |               |
| 9   |      |      |      |      |      |         |               |
| 10  |      |      |      |      |      | 37.9    |               |
| 11  |      |      |      |      |      | 310.17  |               |
| 12  |      |      |      |      |      | 234.46  |               |
| 13  |      |      |      |      |      | 1394.66 | 20.58         |
| 14  |      |      |      |      |      | 1475.25 |               |
| 15  |      |      |      |      |      | 37.62   |               |
| 16  |      |      |      |      |      |         |               |
| 17  |      |      |      |      |      |         |               |
| 18  |      |      |      |      |      |         |               |
| 19  |      |      |      |      |      |         |               |
| 20  |      |      |      |      |      |         |               |
| 21  |      |      |      |      |      |         |               |
| 22  |      |      |      |      |      |         |               |
| 23  |      |      |      |      |      |         |               |
| 24  |      |      |      |      |      |         |               |
| 25  |      |      |      |      |      |         |               |

\* = only part 1
