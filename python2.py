def search_name():
    infile = open("names.txt", "r")
    for s in infile:
        if s.startswith("A"):
            print(s)


search_name()
