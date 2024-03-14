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

