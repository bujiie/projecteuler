#!/usr/bin/env python

def parse_names(raw):
  separator = ','
  return map(lambda x: x.strip()[1:-1], raw.split(separator))

def calculate_letter_score(letter):
  offset = 64
  return ord(letter) - offset

def calculate_name_score(name):
  letter_scores = map(lambda x: calculate_letter_score(x), name)
  return reduce(lambda acc, num: acc + num, letter_scores)


with open('names.txt') as file_handler:
  for line in file_handler:
    total_score = 0
    unsorted_names = parse_names(line)
    sorted_names = sorted(unsorted_names)
    for index, name in enumerate(sorted_names):
      score = calculate_name_score(name)
      row_score = (index+1) * score
      total_score += row_score

print total_score