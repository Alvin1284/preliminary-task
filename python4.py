def search_age():
    infile = open("names.txt", "r")
    age = input("Enter age:")
    for s in infile:
        last_char = s.split()[-1]
        if last_char == age:
            print(s)


search_age()