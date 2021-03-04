# Boris Wang
# Exercise 2 - Python String
# Computer Science 20, blk 3
# March 3, 2021

# This program is my own work - BW
#This is a TEST: 6+7=_.

def sum_digits(ogstring):
    total = 0
    for i in ogstring:
        if(i.isdigit() == True):
            total += int(i)
    print("Digit sum: ",total)

def explore_chars(ogstring):
    print("Original:  ",ogstring)
    print("Length:    ",len(ogstring),"chars")
    print("2nd char:  ",ogstring[1])
    print("2nd last:  ",ogstring[-2])
    print("Switched:  ",ogstring[len(ogstring)-3:len(ogstring)]+ogstring[3:len(ogstring)-3]+ogstring[0:3])

def get_input():
    line = input("Enter 10 or more chars ending with a period:\n-> ")
    while len(line) < 10 or line[-1] != ".":
        print("That is an invalid input!")
        line = input("Enter 10 or more chars ending with a period:\n-> ")
    return line

def explore_string():
    string = get_input()
    explore_chars(string)
    sum_digits(string)

def main():
    explore_string()

if __name__ == "__main__":
    main()