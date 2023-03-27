import collections
test_file = """Here is an input file
I made it multiple lines
let's see if I could properly calculate it
Universe
please 
HELP ME
:)"""
def count_lines(file_name):
    lines = file_name.splitlines()
    print(lines)
    count = 0
    for l in lines:
        count += 1
        print(f"Line {count} : {l}")
#print(count_lines(test_file))

def count_chars(file_name):
    char_dict = collections.Counter(file_name)
    print(sorted(char_dict.items()))

#print(count_chars(test_file))

def test(file_name):
    print(count_lines(file_name))
    return count_chars(file_name)

#print(test(test_file))