#Turkish major vowel harmony following commands
data = input("Enter Your Name")
big = 0
smoll = 0
for i in data:
    if i in "aıou":
        big =+ 1
    elif i in "eiöü":
        smoll =+ 1

print(f"{big} and {smoll} are")

if big > 0 or smoll > 0 :
    if big + smoll == 1:
        sonuc = "Not is a Turkish Grammar"
    elif big * smoll == 0 :
        sonuc = "Turkish grammar is only "
    else:
        sonuc = "Not a Turkish"