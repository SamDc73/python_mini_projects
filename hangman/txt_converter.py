a_file = open("sample.txt", "r")


list_of_lists = []

for line in a_file:
    if (' ' in line) == False:
        stripped_line = line.strip()
        # line_list = stripped_line.split()
        list_of_lists.append(stripped_line)

a_file.close()

print(list_of_lists)
