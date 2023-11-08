#!/usr/bin/python3


def multiple_returns(sentence):
  if not sentence:
    first_character = "None"
  
  return ((len(sentence), sentence[0]))