
print()
print("FAREL'S SALARY CALCULATOR へようこそ")
print("-------------------------------------")
print()
showtime = int (input("How many hours did Farel show? "))
staytime = int (input("How many days did Farel stay? "))
revenueshowraw = (showtime*300)
stayprice = (staytime*50)
revenueshowtaxacc = ((revenueshowraw - stayprice)*(1/10))
disposableincome = revenueshowraw - revenueshowtaxacc

idrconv = (disposableincome * 14888)

print()
print("Salary before Tax:", revenueshowraw)
print("Accomodation:", stayprice)
print()
print("Farel has performed for", showtime, "hours and stayed for", staytime, " days, he has generated", \
    disposableincome, "USD after tax and staying fees. Or, Rp.", idrconv)

