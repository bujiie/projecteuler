#!/usr/bin/env python
import unittest
from name_score import calculate_letter_score, parse_names, calculate_name_score

class TestNameScore(unittest.TestCase):

    def setUp(self):
      pass

    def tearDown(self):
      pass

    def test_parse_names(self):
      name1 = 'name1'
      name2 = 'name2'
      name3 = 'name3'
      raw = "\"%s\", \"%s\",\"%s\"" % (name1, name2, name3)
      names = parse_names(raw)
      self.assertTrue(name2 in names)


    def test_calculated_letter_score(self):
      scores_correct = True
      letters_n_scores = [
        ('C', 3), ('O', 15), ('L', 12), ('I', 9), ('N', 14)
      ]
      for lns in letters_n_scores:
        if lns[1] != calculate_letter_score(lns[0]):
          scores_correct = False
          break
      self.assertTrue(scores_correct)


    def test_name_score(self):
      name = 'COLIN'
      score = calculate_name_score(name)
      self.assertEqual(score, 53)


if __name__ == '__main__':
    unittest.main()
