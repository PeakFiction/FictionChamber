originalWord = input() #Input original word (s)

SecondInputWord = input() #Input second word (t)

reversedOriginalWord = originalWord[::-1] #make original word reversed

if SecondInputWord == reversedOriginalWord: #check if reversed original word is the same as t
    print("YES") #if is reversed output yes
else:
    print("NO") #if is not reversed then output NO 


