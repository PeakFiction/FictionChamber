query = int(input())
totalX = 0 

for i in range(query):
    command = input()
    
    if command == "X++" or command =="++X":
        totalX = totalX + 1
    elif command == "--X" or command == "X--":
        totalX = totalX - 1

print(totalX)