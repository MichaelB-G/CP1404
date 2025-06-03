"""Guess game with files and exceptions"""

#FILENAME = "secret.txt"

#def main():
    #secret = load_number(FILENAME)
    #guess = get_valid_number()
    #while guess != secret:
        #print("Guess again! ")
        #guess = get_valid_number()
    #print("You guessed correctly!")


#d#ef get_valid_number():
    #is_valid_input = False
    #while not is_valid_input:
        #try:
            #guess = int(("Please guess a number: "))
            #is_valid_input = True
        #except ValueError:
            #print("Invalid input")
    #return guess


#def load_number(filename):

    #try:
        #infile = open(filename, "r")
        #number = int(infile.read())
    #except ValueError:
        #print(f"{filename} is not a valid number")
        #number = 6

    #except FileNotFoundError:
        #print(f"{filename} is not a valid file")
        #number= 4

    #else:
        #infile.close()
    #return number


  #main()


with open("data.txt", "r") as in_file:
    in_file.readline()  # Ignore header of data
    for line in in_file:
        parts = line.strip().split(',')

        name = parts[0]
        length = int(parts[1])
        print(name, "is", length, "metres long")