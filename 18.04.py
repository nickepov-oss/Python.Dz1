import re
from re import fullmatch

minyons_1 = "Minyon minYon Mineyon mInyoN mInYon MINYON mOnYoN ManyoN"
minyons_2 = "minyon miNYon mIneYon MinYou Minyon Bob Manyon minYON MiNyon MinyoN Monyon"
Bob = re.compile("Bob")#
match_1 = Bob.search(minyons_1)# search - шукає перший збіг
print(match_1)
match_2 = Bob.search(minyons_2)
print(match_2)

match_3 = Bob.finditer(minyons_1)# finditer - шукає всі збіги
for item in match_3:
    print(f"match_1: {item}")
match_4 = Bob.finditer(minyons_2)
for item in match_4:
    print(f"match_2: {item}")

match_5 = Bob.findall(minyons_1)# findall - створює список з усіма входженнями
match_6 = Bob.findall(minyons_2)
print(match_5)
print(match_6)

minyons_with_Kevin_1 = Bob.sub("Kevin", minyons_1)# sub -  зміна чогось на щось
print(minyons_with_Kevin_1)
minyons_with_Kevin_2 = Bob.sub("Kevin", minyons_2)
print(minyons_with_Kevin_2)

splitty = Bob.split(minyons_1)# Метод аналогічний до Split String
print(splitty)
fullmatch_1 = Bob.fullmatch(minyons_1)# Повний збіг з рядком
fullmatch_2 = Bob.fullmatch(minyons_2)
print(fullmatch_1)
print(fullmatch_2)

login_patter = re.compile(r"^/w{3,20}")