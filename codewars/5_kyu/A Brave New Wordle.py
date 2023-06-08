"""
https://www.codewars.com/kata/62013b174c72240016600e60

Wordle is a game where users try to guess a hidden 5 letter word. Feedback is given for each guess, in the form of colored tiles, indicating when letters match or occupy the correct position.

see: https://www.nytimes.com/games/wordle/index.html

The Brief
Make a function that takes in a 5 letter guess and, comparing to a known solution, returns clues for the user to solve the wordle puzzle.

Requirements
The function takes in two strings of 5 letters each, a guess and a solution.
The function returns a string of 5 letters.
The returned string is composed of letters each corresponding to a letter of the guess: 'b' (black) when the letter is not present in the answer; 'y' (yellow) when the letter is present but in a different location; and 'g' (green) when the letter is present and in the right location.
Duplicates
A letter appearing in the correct place is always green, including if it appears elsewhere in the word.
A letter can only be green or yellow as many times as it appears in the correct answer. Extra occurences of that letter are marked as 'b'.
Below are some examples, see example tests for more:
letters are evaluated left to right.
Guess: xxxxx
Answer: yxxxx
Expected Output: bgggg
Explanation: extra letters marked as 'b'

guess: xxxxz
answer:aaaax
expected output: ybbbb
first x marked as 'y',  and each one as 'b' after
"""

def resolver(guess, solution):
    tmp_sol = list(solution)
    clue = ["b", "b", "b", "b", "b"]

    for index in range(5):
        if guess[index] == solution[index]:
            clue[index] = "g"
            tmp_sol.pop(tmp_sol.index(guess[index]))

    for index in range(5):
            if clue[index] == "b" and guess[index] in tmp_sol:
                clue[index] = "y"
                tmp_sol.pop(tmp_sol.index(guess[index]))

    return ''.join(clue)


print(resolver('woooo', 'world'))
print(resolver('wooer', 'ivory'))  # 'bbgby'