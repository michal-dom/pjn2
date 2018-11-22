import os
import operator


ter_dict = {}

with open('lematy-02-UTF-8.txt', 'r') as words:
    for w in words:
        ter_dict[w.split("|")[0]] = w.split("|")[1]

for filename in os.listdir("texts"):
    try:
        with open("texts/" + filename, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            word_index = {}
            all_terms = 0

            for word in data.split():

                all_terms += 1
                if word in ter_dict.keys():
                    word = ter_dict[word]
                if word in word_index:
                    word_index[word] += 1
                else:
                    word_index[word] = 1

            sorted_dict = dict(sorted(word_index.items(), key=operator.itemgetter(0)))
            with open('lemmas/terms/'+filename, 'w') as term, open('lemmas/freqs/'+filename, 'w') as freq:
                for k,v in sorted_dict.items():
                    term.write(str(k) + "\n")
                    freq.write(str(round(int(v) / all_terms, 6)) + "\n")
    except:
        print("can't open " + filename)
