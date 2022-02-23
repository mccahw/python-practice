from difflib import SequenceMatcher
import sys

removeSpaces = False
try:
    if len(sys.argv) > 2:
        raise ValueError
    elif len(sys.argv) == 2:
        if not sys.argv[1].isnumeric():
            raise ValueError
        elif int(sys.argv[1]) != 0 and int(sys.argv[1]) != 1:
            raise ValueError
        elif int(sys.argv[1]) == 1:
            removeSpaces = True
except ValueError:
    print("ERROR: Invalid argument(s)")
    print("USAGE: {} <removeSpaces>".format(sys.argv[0]))
    print("USAGE: removeSpaces - 0 (default), 1")
    quit()

print("Text 1:")
string1 = input()
print("Text 2:")
string2 = input()

if removeSpaces:
    string1 = "".join(string1.split(" "))
    string2 = "".join(string2.split(" "))

lmatch = SequenceMatcher(None, string1, string2).find_longest_match(
    0, len(string1), 0, len(string2))
match = SequenceMatcher(None, string1, string2).get_matching_blocks()

print("\n{} total matches".format(len(match)-1))
print("Longest match is {}".format(string1[lmatch.a: lmatch.a + lmatch.size]))

print("Nontrivial matches:\n")
for hit in match:
    if hit.size > 1:
        s1 = (string1[0: hit.a], string1[hit.a: hit.a +
              hit.size], string1[hit.a + hit.size:])
        s2 = (string2[0: hit.b], string2[hit.b: hit.b +
              hit.size], string2[hit.b + hit.size:])
        print(string1[hit.a: hit.a + hit.size])
        print("Text 1: {}".format("*".join(s1)))
        print("Text 2: {}\n".format("*".join(s2)))
