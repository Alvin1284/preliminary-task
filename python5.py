def search_name():
    infile = open("names.txt", "r")
    val = input("Enter letter: ").upper()
    
    for s in infile:
        if s.startswith(val):
            print(s)


search_name()