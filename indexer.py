import os
import operator
import math
from bisect import bisect_left
import json

# searched = "w"
# N = 14450

#
# def binary_search(a, x, lo=0, hi=None):
#     hi = hi if hi is not None else len(a)
#     pos = bisect_left(a, x, lo, hi)
#     return pos if pos != hi and a[pos] == x else -1

# a = [1, 2, 5, 7, 9, 11]
#
# print(binary_search(a, 2))
#
#
# tf = {}
# ni = 0
# for filename in os.listdir("indexes/terms/"):
#     with open('indexes/terms/' + filename,'r') as file_term:
#         terms = file_term.read().splitlines()
#         id = binary_search(terms, searched)
#         if id != -1:
#             with open('indexes/freqs/' + filename, 'r') as file_freq:
#                 ni += 1
#                 tf[filename] = float(file_freq.read().splitlines()[id])


# idf = math.log(N/ni)
# print(idf)
# sorted_tf = sorted(tf.items(), key=operator.itemgetter(1), reverse=True)[:100]
# tf_json = json.dumps(sorted_tf)
# print(tf_json)

    # for line in f:
    #     if line.split()[0] == searched:
    #         print(line.split()[1])

# generowanie indeksów
for filename in os.listdir("texts"):
    try:
        with open("texts/" + filename, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            word_index = {

            }
            all_terms = 0
            for word in data.split():
                all_terms += 1
                if word in word_index:
                    word_index[word] += 1
                else:
                    word_index[word] = 1
            sorted_index = sorted(word_index.items(), key=operator.itemgetter(0))
            with open('indexes/terms/' + filename, 'w') as term, open('indexes/freqs/' + filename, 'w') as freq:
                for it in sorted_index:
                    term.write(str(it[0]) + "\n")
                    freq.write(str(round(it[1]/all_terms, 6)) + "\n")
    except:
        print("can't open ")



# generator stop slow
# word_index = {
#
# }
# all_terms = 0
#
# for filename in os.listdir("texts"):
#     try:
#         with open("texts/" + filename, 'r') as myfile:
#             data = myfile.read().replace('\n', '')
#             for word in data.split():
#                 all_terms += 1
#                 if word in word_index:
#                     word_index[word] += 1
#                 else:
#                     word_index[word] = 1
#     except:
#         print("can't open ")
#
#
# sorted_index = sorted(word_index.items(), key=operator.itemgetter(1), reverse=True)
# with open('stop_words.txt', 'w') as sw:
#     for it in sorted_index:
#         sw.write(str(it[0]) + "\n")

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1

ter_dict = {}
# with open('lemmas/words.txt', 'r') as words, open('lemmas/lemmas.txt', 'r') as lemmas:#żyźnie
#     terms_w = words.read().splitlines()
#     terms_l = lemmas.read().splitlines()
#     for i,t in terms_w:
#         ter_dict[terms_w] = terms_l[i]

with open('lematy-02-UTF-8.txt', 'r') as words:
    for w in words:
        ter_dict[w.split("|")[0]] = w.split("|")[1]

# print(ter_dict["żyźniejszymi"])

for filename in os.listdir("texts"):
    # try:
        with open("texts/" + filename, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            word_index = {

            }
            all_terms = 0
            for word in data.split():
                all_terms += 1
                # print(ter_dict)
                if word in ter_dict.keys():
                    word = ter_dict[word]

                if word in word_index:
                    word_index[word] += 1
                else:
                    word_index[word] = 1

            sorted_index = sorted(word_index.items(), key=operator.itemgetter(0))
            with open('lemmas/terms/' + filename, 'w') as term, open('lemmas/freqs/' + filename, 'w') as freq:
                for it in sorted_index:
                    term.write(str(it[0]) + "\n")
                    freq.write(str(round(it[1]/all_terms, 6)) + "\n")
    # except:
    #     print("can't open " + filename)


