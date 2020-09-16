import sys  # for using command line interface
import spellcheck  # has the pre defined functions in it

value = sys .argv[1]  # take the argument after file location
print(spellcheck.is_this_spelled_right(value))
