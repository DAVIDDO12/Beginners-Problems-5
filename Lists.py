numList= [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
Biggestnumber = max(numList)
Smallestnumber = min(numList)
Sum = sum(numList)
Numberofnumbers = len(numList)
Average = Sum / Numberofnumbers
index1=numList.index(Biggestnumber)
index2=numList.index(Smallestnumber)
print(Biggestnumber,"The index is", index1)
print(Smallestnumber,"The index is", index2)
print(Average)

stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
count = 0
for stringitem in stringsList:
    if len(stringitem) > 0 and stringitem[0] == stringitem[-1]:
        count += 1
    print(count)

iLikePesto = []
otherFoods = []
for people in range(1,9):
    favouritefood = input("What's your favourite food?")
    if favouritefood.lower() == "pesto":
        iLikePesto.append(favouritefood)
    else:
        otherFoods.append(favouritefood)
print(len(iLikePesto))
for num in range(len(iLikePesto)):
    print("I like pesto")
print("Other foods:")
print(otherFoods)

cerealList = []
while True:
    cereal = input("Enter cereal:")
    if cereal.lower() in ["sultana and bran", "weetbix"]:
        break
    else:
        cerealList.append(cereal)
print("The cereals:")
for cereal in cerealList:
    print(cereal)
