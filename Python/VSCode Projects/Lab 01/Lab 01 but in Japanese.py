print()
print("FARELの給料電卓へようこそ")
print("-------------------------------------")
showtime = int (input("どのくらい時間は彼が演ずりましたか？(時間で）"))
staytime = int (input("ホテルで、幾つ日は彼が住みましたか？"))
revenueshowraw = (showtime*300)
stayprice = (staytime*50)
revenueshowtaxacc = ((revenueshowraw - stayprice)*(1/10))
disposableincome = revenueshowraw - revenueshowtaxacc

idrconv = (disposableincome * 14888)

print()
print("FARELの給料税金抜き:", revenueshowraw)
print("宿泊室料金:", stayprice)
print()

print("Farelが", showtime, "時間で演ずりました. そうして", staytime, "日で住みました。彼の給料は税金と宿泊室の後で", disposableincome, "そうして、ルピアで", idrconv)

