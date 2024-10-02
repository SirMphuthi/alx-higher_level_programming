#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for a in my_list:
            if a_dictionary[a] > score:
                score = a_dictionary[a]
                leader = a
        return leader
