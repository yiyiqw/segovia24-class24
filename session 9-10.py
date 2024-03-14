f = open("x-files.txt", "r")
while True:
    line = input("give me some text to put into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end
f.close()

# class code
with open("secret.txt") as f:
    text = f.read()
text = text.split("\n")
decooded = ""
for line in text:
    num_vow = 0
    for v in "aeiou":
        num_vow += line.count(v)
    decoded = decoded + "abcdefghijklmnopqrstuvxyz"[num_vow]
print(decoded)