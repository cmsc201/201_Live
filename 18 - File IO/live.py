# read in a file, and count how many functions are defined there
# def number_functions(filename):
#     file = open(filename, 'r')
#     contents = file.read()
#     file.close()
#
#     function_count = 0
#     for i in range(len(contents)):
#         if i + 4 < len(contents) and contents[i:i + 4] == "def ":
#             function_count += 1
#
#     return function_count
#
#
# def main():
#     print(number_functions("live.py"))


# main()
# read in a file, find each time it says dogs and replace it with cats, write out the file
# def justice(filename, outputFilename):
#     file = open(filename, 'r')
#     contents = file.read()
#     file.close()
#     contents = contents.lower()
#     output = ""
#     i = 0
#     while i < len(contents):
#         if i + 4 < len(contents) and contents[i:i + 4] == "dogs":
#             output += "cats"
#             i += 4
#         else:
#             output += contents[i]
#             i += 1
#
#     # write output to a file
#     out_file = open(outputFilename, 'w')
#     out_file.write(output)
#     out_file.close()
#
# def main():
#     print(justice("dogfest.txt", "catfest.txt"))
#
# main()
# Read in a file of integers and print their average
def main():
    file = open("someints.txt", 'r')
    lines = file.readlines()
    file.close()
    sum = 0
    number = len(lines)
    for i in range(len(lines)):
        sum += int(lines[i])
    print(sum / number)


main()