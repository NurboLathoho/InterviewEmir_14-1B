# Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
# def print_zeros_rows():
#     for i in range(1, 6):
#         print(f"{i}. 0")

# print_zeros_rows()

# Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой. Результат: "AAiddialneat” 
# def mix_names(name1, name2):
#     mixed_name = []
    
#     min_length = min(len(name1), len(name2))
#     for i in range(min_length):
#         mixed_name.append(name1[i])
#         mixed_name.append(name2[i])
    
#     mixed_name.extend(name1[min_length:])
#     mixed_name.extend(name2[min_length:])
#     return ''.join(mixed_name)


# result = mix_names("Aidana", "Adilet")
# print(result)
# СУУУУУУ ПОЛУЧИЛОСЬ 4 РАЗА НЕПРАВИЛЬНО ВЫШЛО ХВАВВВАПВП

# Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money,
# it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world
def word_frequency(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


sentence = "money, money, money, it’s always sunny, in the richmen’s world"
print(word_frequency(sentence))

