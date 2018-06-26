import string
exclude = set(string.punctuation)
iliad_text =[]
top = {}
final_top = {}
counter = 0
with open("iliad.txt", "r", encoding="utf-8") as f:
        iliad_text = f.read().split()
for i in iliad_text:
    iliad_text[counter] = i.lower().rstrip(string.punctuation)
    counter += 1
for i in iliad_text:
    if i in top:
        top[i] += 1
    else:
        top[i] = 1
top_list = top.items()
for i in top_list:
    final_top[i[1]] = i[0]
counter = 1
print("The Top Ten Words From The Iliad\n")
for i in sorted(final_top)[::-1]:
    print(str(counter)+ ". " + final_top[i])
    counter += 1
    if counter == 11:
        break
