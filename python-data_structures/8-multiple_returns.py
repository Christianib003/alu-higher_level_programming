#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        first_character = "None"
    else:
        first_character = sentence[0]
  
    return ((len(sentence), first_character))
