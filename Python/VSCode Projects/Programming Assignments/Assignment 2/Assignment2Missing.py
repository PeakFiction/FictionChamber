#################### CANT OPEN???? ######################
try:
    file = open("JokoWidodoSpeech.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("the file's not there you dingus")
    
    
#################### CANT OPEN???? ######################

#put between line 51 and line 53