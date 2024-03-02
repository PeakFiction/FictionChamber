import string
from stop_words import get_stop_words

ifile = """
        The birds have left their trees
        The light pours onto me
        I can feel you lying there all on your own
        We got here the hard way
        All those words that we exchange
        Is it any wonder things get broke?
        'Cause in my heart and in my head
        I'll never take back the things I said
        So high above, I feel it coming down
        She said, in my heart and in my head
        Tell me why this has to end
        Oh, no, oh, no
        I can't save us, my Atlantis, we fall
        We built this town on shaky ground
        I can't save us, my Atlantis, oh, no
        We built it up to pull it down
        Now all the birds have fled
        The hurt just leaves me scared
        Losing everything I've ever known
        It's all become too much
        Maybe I'm not built for love
        If I knew that I could reach you, I would go
        It's in my heart and in my head
        You can't take back the things you said
        So high above, I feel it coming down
        She said, in my heart and in my head
        Tell me why this has to end
        Oh, no, oh, no
        I can't save us, my Atlantis, we fall
        We built this town on shaky ground
        I can't save us, my Atlantis, oh, no
        We built it up to pull it down
        Yeah, we build it up and we build it up
        Yeah, we build it up to pull it down
        And we build it up and we build it up
        And we build it up to pull it down
        I can't save us, my Atlantis, we fall
        We built this town on shaky ground
        I can't save us, my Atlantis, oh, no
        We built it up to pull it down
"""

#erases punctuation
ifileNoPunc = ifile.translate(str.maketrans('','', string.punctuation))
#makes the all the words in the text lower case
ifileLowerCase = ifileNoPunc.lower()

#splits every bit into a string
ifileSplitted = ifileLowerCase.split()

#sorts the splitted string in accordance to ASCII
ifileSplitted.sort()

word_clean = []
word_repeated = []
# TODO: create for loop to add non stop words to the list and add repeated words to the list
for i in ifileSplitted:
    # strip the word from punctuation and make it lowercase
    if i in get_stop_words('english'):
        continue
    if i not in word_clean:
        word_clean.append(i)
    elif i not in word_repeated:
        word_repeated.append(i)


# PRINT OUTPUT
# TODO: Create a loop to print the list of repeated words in a nicely formatted table
print("") #prints a new line (enter)
print("The sorted (A-Z) repeated words are:") #prints the The sorted (A-Z) repeated words are:
column_counter = 0 #sets the column counter to zero
for y in word_repeated: #for loops every variable in word_repeated
    print(f"{y:20}", end="") #prints said variable with a width of 20
    column_counter = column_counter +1 #adds the +1 counter
    if column_counter == 5: #if column counter is 5, then
        print('')           #prints a new line
        column_counter = 0  #and resets it back to zero

print("") #prints a new line
print("") #prints a new line
column_counter = 0 #sets the column counter to zero
print("The sorted (A-Z) cleaned words are:") 
for x in word_clean: #for loops every variable in word_clean
    print(f"{x:20}", end="") #prints said variable with a width of 20
    column_counter = column_counter + 1 #adds the +1 counter
    if column_counter == 5: #if column counter is 5, then
        print('')           #prints a new line
        column_counter = 0  #and resets it back to zero
