# lexcheck
A small program to check typographical errors in study lists. Useful for word game players.

Requirements: Python (2.7.13 at the moment.)

Usage: Invoke this program with "python lexcheck.py" followed by two filenames: first, a lexicon of words; second, a word list (typically much smaller) to test.

Function: Checks every word in the word list, to ensure it's either in the lexicon, or a valid anagram of a word in the lexicon. (I wrote the program this way to allow lists of alphagrams to pass.) If the program finds an invalid word (presumably a typo), it prints the line numbers of all such words, so the user can fix them before using the word list.

Purpose: I designed this program to validate manually-entered word lists (whether from paper studying, Aerolith missed words, etc.) before importing said lists into a computer word-studying program. Those will typically either choke on the entire list unhelpfully, or silently pass over typographical errors. I run this program so I can fix those errors myself, prior to importing the word list file. 