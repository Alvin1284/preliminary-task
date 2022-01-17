def search_age():
    infile = open("names.txt", "r")
    for s in infile:
        last_char = s.split()[-1]
        if last_char == "5":
            print(s)


search_age()
