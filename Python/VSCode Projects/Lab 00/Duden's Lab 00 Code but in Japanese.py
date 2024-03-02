print("\n")
print("こんにちは! ラボ 00 プログラミング基礎へようこそ！", "\n")
print("下で、あなたの名前、あだ名、学生ID、とメールをき記録してください!" "\n")
# Python prints words

名前 = input("名前: ")
あだ名 = input("あだ名: ")
カタカナで名前 = input("カタカナ書く方名前: ")
何歳 = input("歳: ")
学生_ID = input("学生ID: ")
メール= input("メール: ")
# We give variables that is unknown to python so that the command will ask the user for what the variables mean

print()
#page break

print("一つ言葉で、あなたによると”プログラミング”を写してください")
答え = input("")
#We tell python to print another line as context for the user on what to type next as the "answer" variable input.

print("\n")
#page break

print("学生", 名前, "またの名を", あだ名, "カタカナで", カタカナで名前, 何歳, "歳", "とメールは", メール, "出席を写しました。", "\n")
print("そうして",カタカナで名前, "によると、", 答え, "は”プログラミング”を写した一つ言葉です。")
print("\n")
print("今日のラボ会議が来てくれてありがとうございました！また来週ねぇ！")
print("\n")

#python prints the texts from the variables with context and it ends the process
