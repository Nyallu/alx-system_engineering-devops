#!/usr/bin/python3

"""
importing requests module
"""

import re

def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

    # perform API call here to get titles of hot articles from subreddit
    # use after parameter to get next page of results if available

    # parse titles and count occurrences of words
    title_words = [re.findall(r'\b\w+\b', title.lower()) for title in titles]
    title_words = [word for sublist in title_words for word in sublist] # flatten list of lists
    for word in word_list:
        count = title_words.count(word)
        if count > 0:
            if word in count_dict:
                count_dict[word] += count
            else:
                count_dict[word] = count

    # recursively call function with after parameter to get next page of results
    if after is not None:
        count_words(subreddit, word_list, count_dict, after=after)

    # sort and print results
    sorted_results = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_results:
        print("{}: {}".format(word, count))

