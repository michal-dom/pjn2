from flask import Flask
from flask import render_template
from flask import request
import json
from bisect import bisect_left
import os
import operator
import math

app = Flask(__name__)

N = 14450
ni = 0
text_dir = "indexes"


def lemmatize_request(text):
    term_dict = {}
    with open('lematy-02-UTF-8.txt', 'r') as words:
        for w in words:
            term_dict[w.split("|")[0]] = w.split("|")[1]
    result = []
    for t in text:
        if t in term_dict.keys():
            result.append(term_dict[t])
        else:
            result.append(t)

    return list(set(result))


def remove_stop_words(text, n):
    with open('stop_words.txt', 'r') as sw_file:
        stop_words = sw_file.read().splitlines()[:n]
    without_sw = [x for x in text if x not in stop_words]
    return without_sw


def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1


def searcher(searched):
    global ni
    ni = 0
    term_freq_dict = {}
    for filename in os.listdir("indexes/terms/"):
        with open(text_dir + '/terms/' + filename, 'r') as file_term:
            terms = file_term.read().splitlines()
            id = binary_search(terms, searched)
            if id != -1:
                with open(text_dir + '/freqs/' + filename, 'r') as file_freq:
                    ni += 1
                    term_freq_dict[filename] = float(file_freq.read().splitlines()[id])

    sorted_dict = dict(sorted(term_freq_dict.items(), key=operator.itemgetter(1), reverse=True)[:20000])
    idf = math.log(N/ni)
    sorted_dict.update((x, y * idf) for x, y in sorted_dict.items())
    return sorted_dict


def all_file_searcher(words):
    global ni
    prev_dict = searcher(words[0])
    next_dict = {}

    for w in words[1:]:
        next_dict = searcher(w)
        intersection = set(next_dict.keys()) & set(prev_dict.keys())
        result_dict = {}
        for i in intersection:
            result_dict[i] = prev_dict[i] + next_dict[i]
        prev_dict = result_dict

    sorted_dict = dict(sorted(prev_dict.items(), key=operator.itemgetter(1), reverse=True)[:200])
    return sorted_dict



def get_stop_words(n):
    with open('stop_words.txt', 'r') as sw_file:
        stop_words = sw_file.read().splitlines()[:n]
    return stop_words



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/searching', methods=['POST'])
def searching():
    opt =  request.form['opt']
    text = request.form['text']
    sw = int(request.form['stop'])
    lem = int(request.form['lemat'])
    global text_dir

    text_list = str(text).split(" ")

    if lem == 1:
        text_list = lemmatize_request(text_list)
        text_dir = "lemmas"

    if sw > 0:
        text_list = remove_stop_words(text_list, sw)

    print(text_list)

    result = all_file_searcher(text_list)

    print(result)
    return json.dumps(result)



if __name__ == '__main__':
    app.run()
