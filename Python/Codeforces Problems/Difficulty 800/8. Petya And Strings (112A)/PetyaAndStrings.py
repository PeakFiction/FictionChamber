string1 = input()
string2 = input()

if string1.lower() < string2.lower():
    print("-1")
elif string1.lower() > string2.lower():
    print("1")
elif string1.lower() == string2.lower():
    print("0")
