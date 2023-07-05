#номер 1
#1 способ
#text = input()
#text2 = text.replace(" ", '-')
#print(text2)

#2 способ
text = str(input())
text2 = text.split(" ")
print('-'.join(text2))
