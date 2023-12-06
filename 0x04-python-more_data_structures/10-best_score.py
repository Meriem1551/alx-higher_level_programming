#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    if a_dictionary is not None:
        max_score = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == max_score:
                return key
