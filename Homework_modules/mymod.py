def test(file_name):
    print(counting_lines(file_name))
    print(counting_chars(file_name))


def counting_lines(file_name):
    with open(file_name, "r") as f:
        a = len(f.readlines())
        print("Total number of lines is: ", a)


def counting_chars(file_name):
    with open(file_name, "r") as f:
        b = len(f.read().replace(" ", ""))
        print("Total number of chars is: ", b)

#counting_lines("lines_counting")
test("lines_counting")
