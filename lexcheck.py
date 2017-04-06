import sys
from collections import defaultdict

def alphagramify(word):
    alphagram = ''.join(sorted(list(word)))
    return alphagram

def find_typos(list_of_lists):
    typo_lines = []
    for num, answers in enumerate(list_of_lists,start=1):
        if answers == None:
            typo_lines.append(num)
    return typo_lines

def setup(lexicon, wordfile):
    with open(lexicon, 'r') as f:
        lexlist = [line.rstrip() for line in f]
    
    alphagram_list = [alphagramify(word) for word in lexlist]
    alphagram_dict = dict(zip(lexlist, alphagram_list))

    alphagram_solution_dict = defaultdict(list)
    for key, value in alphagram_dict.iteritems():
        alphagram_solution_dict[value].append(key)

    def find_all_anagrams(stringkey):
        try:
            anagram_list = alphagram_solution_dict[alphagram_dict[stringkey]]
        except KeyError:
            return None
        return anagram_list
        
    with open(wordfile, 'r') as f2:
        wordlist = [find_all_anagrams(line.rstrip().upper()) for line in f2]

    return find_typos(wordlist)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            lexicon = sys.argv[1]
            wordfile = sys.argv[2]
            print(setup(lexicon, wordfile))
        except Exception:
            print("Something went wrong. Sorry.")
            print Exception
    else:
        print("Wrong number of arguments. Call with lexicon file, then word list file.")
