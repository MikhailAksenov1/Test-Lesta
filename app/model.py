import glob
import math
import re
import os

def tfidf(path_to_samles):
    top_50 = []
    words = {}
    words_in_all_docs = {}
    text_files = glob.glob(os.path.join(path_to_samles, "*.txt"))
    for i in text_files:
        lines = (line for line in open(i))
        words[i] = {}
        for k in lines:
            k = re.split(r'[.,; \s]+', k.lower())
            for d in k:
                if d != '':
                    if d not in words_in_all_docs.keys():
                        words_in_all_docs[d] = [i]
                    if i not in words_in_all_docs[d]:
                        words_in_all_docs[d].append(i)
                    if d not in words[i].keys():
                        words[i][d] = [1]
                    else:
                        words[i][d][0] += 1

    for docs in words:
        count = 0
        for word in words[docs]:
            count += words[docs][word][0]
        for word in words[docs]:
            words[docs][word][0] /= count

    for i in words:
        for k in words[i]:
            tf = words[i][k][0]
            idf = abs(math.log10(len(text_files) / (len(words_in_all_docs[k]))))
            top_50.append((idf, tf, i, k))

    top_50 = sorted(top_50, reverse=True)
    return top_50[0:50]
