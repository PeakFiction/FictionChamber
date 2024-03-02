import string
from stop_words import get_stop_words

ifile = """
Dering teleponku membuatku tersenyum di pagi hari
Kau bercerita semalam kita bertemu dalam mimpi
Entah mengapa aku merasakan hadirmu di sini
Tawa candamu menghibur saatku sendiri

Aku di sini dan kau di sana
Hanya berjumpa via suara
Namun ku slalu menunggu saat kita akan berjumpa

Meski kau kini jauh di sana
Kita memandang langit yang sama
Jauh di mata namun dekat di hati

Dering teleponku membuatku tersenyum di pagi hari
Tawa candamu menghibur saatku sendiri

Aku di sini dan kau di sana
Hanya berjumpa via suara
Namun ku slalu menunggu saat kita akan berjumpa

Meski kau kini jauh di sana
Kita memandang langit yang sama
Jauh di mata namun dekat di hati

Aku di sini dan kau di sana
Hanya berjumpa via suara
Namun ku slalu menunggu saat kita akan berjumpa

Meski kau kini jauh di sana
Kita memandang langit yang sama
Jauh di mata namun kau dekat di hati

Jarak dan waktu takkan berarti
Karena kau akan selalu di hati
Bagai detak jantung yang kubawa kemanapun kupergi

Meski kau kini jauh di sana
Kita memandang langit yang sama
Jauh di mata namun dekat di hati
Dekat di hati
Dekat di hati

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
    if i in get_stop_words('indonesian'):
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
