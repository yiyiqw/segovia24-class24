f = open("x-files.txt", "a")
while True:
    line = input("give me some text to put into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end
f.close()


with open("x-files.txt", "r")
