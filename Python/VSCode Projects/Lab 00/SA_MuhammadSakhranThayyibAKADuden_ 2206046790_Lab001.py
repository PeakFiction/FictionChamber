print("\n")
print("Hello! Welcome to the Lab 00 for Programming Foundations 1!" "\n")
print("Please record your attendance by entering your name, nickname, student ID, and your UI e-mail down below" "\n")
# Python prints words

name = input("Name: ")
nickname = input("Nickname: ")
katakana_name = input("Name in Katakana: ")
何歳 = input("Age: ")
student_ID = input("Student ID: ")
email = input("E-mail: ")
# We give variables that is unknown to python so that the command will ask the user for what the variables mean

print("\n")
#page break

print("Please write 1 (one) word that describes programming for you!")
answer = input(">")
#We tell python to print another line as context for the user on what to type next as the "answer" variable input.

print("\n")
#page break

print("Attendance recorded for student", name, "AKA", nickname, "or", katakana_name, "who is", 何歳, "years old,", "with student ID", student_ID, "and e-mail", email, "and", answer, "is the word that describes programming for them.")
print("\n")
print("Thank you for coming to today's lab session. See you next week!")
print("\n")

#python prints the texts from the variables with context and it ends the process
