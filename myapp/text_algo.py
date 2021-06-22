from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def get_word_set(input_text):
    words = word_tokenize(input_text)
    words = [word.lower() for word in words if word.isalpha()]
    print(words)
    clean_words = words[:]
    #sr = stopwords.words('english')
    for token in words:
        if token in stopwords.words('english'):
            clean_words.remove(token)
    return clean_words

def remove_duplicates(words_set):
    words_set = list(dict.fromkeys(words_set))
    return words_set

def get_top_words(words_set):
    #count = Counter(words_set).items()
    x = Counter(words_set)
    #percentages = {x: int(float(y) / len(words_set) * 100) for x, y in count}

    # for name, pct in percentages.iteritems():
    #    print('%s - %s%s' % (name, pct, '%'))
    #print(percentages)
    for w,i in  x.most_common(3):
        print(w)
    return x.most_common(3)

def get_line_from_file(file_path):
    lines_set =list()
    for line in open(file_path, 'r'):
        lines_set.append(line)
    return lines_set

import numpy as np
def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])


def list_to_string(s):
    # initialize an empty string
    str1 = ","
    # return string
    return (str1.join(s))

#Distance = levenshtein_ratio_and_distance('a', 'ab',True)
#print(Distance)
#c_w = get_word_set('this is a, cool sentense sarath. How are you sarath. python, python')
#print(c_w)
#print(remove_duplicates(c_w))
#print(list_to_string(c_w))

#get_top_words(c_w)