ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def get_txt(text):
    with open(text, "r") as f:
        book = f.read()
        return book

def character_per_word(text):
    word_list = []
    character_count_list = []
    for word in get_txt(text).split():
        word_list.append(word.strip("."))
    # print(word_list)
    # print()
    for word in word_list:
        character_count_list.append(len(word))
    # print(character_count_list)
    # print(sum(character_count_list)/len(character_count_list))
    return sum(character_count_list)/len(character_count_list)

def words_per_sentence(text):
    init_sentence_list = []
    word_count_list = []
    for sentence in get_txt(text).split("."):
        init_sentence_list.append(sentence.strip())
    sentence_list = init_sentence_list[:-1]
    # print(sentence_list)
    for sentence in sentence_list:
        word_count_list.append(len(sentence.split()))
    # print(word_count_list)
    # print(sum(word_count_list)/len(word_count_list))
    return sum(word_count_list)/len(word_count_list)

def ari(text):
    index = (4.71 * character_per_word(text)) + (0.5 * words_per_sentence(text)) - 21.43
    # print(index)
    mod = index % 1
    end_ari = int(index - mod + 1)
    # print(end_ari)
    return end_ari

def ari_description(text):
    if ari(text) > 14:
        index = 14
    else:
        index = ari(text)
    return f"The ARI for {text} is " + str(ari(text)) + "\nThis corresponds to a " + ari_scale[index]['grade_level'] + " level of difficulty\nthat is suitable for an average person " + ari_scale[index]['ages'] + " years old."


# print(get_txt("5c_w__5w_s.txt"))
print()
# print(character_per_word("5c_w__5w_s.txt"))
# print(words_per_sentence("5c_w__5w_s.txt"))
# ari("5c_w__5w_s.txt")
print(ari_description("5c_w__5w_s.txt"))
print()
# print(character_per_word("iliad.txt"))
# print(words_per_sentence("iliad.txt"))
# ari("iliad.txt")
print(ari_description("iliad.txt"))
print()
