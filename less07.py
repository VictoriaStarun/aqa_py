import unittest

#import functions to test
import less6

class my_unittests(unittest.TestCase):

    def test_smoke_adding_function(self):
        "Test adding function"
        actual_result = less6.sum_of_two(2,3)
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def test_zero_adding_function(self):
        "Test adding function with zero"
        actual_result = less6.sum_of_two(0,1)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test_negative_nums_adding_function(self):
        "Test adding function wit negative numbers"
        actual_result = less6.sum_of_two(-5,1)
        expected_result = -4
        self.assertEqual(actual_result, expected_result)

    def test_smoke_longest_word(self):
        "Test finding the longest word of list"
        actual_result = less6.the_longest_word_of_list(["Luke", "Anakin", "Leia"])
        expected_result = "Anakin"
        self.assertEqual(actual_result, expected_result)

    def test_longest_word_empty(self):
        "Test finding the longest word of list, one of the items is empty"
        actual_result = less6.the_longest_word_of_list(["", "Anakin", "Leia"])
        expected_result = "Anakin"
        self.assertEqual(actual_result, expected_result)

    def test_sentences_divider(self):
        "Test devision of text to a list sentences by a dot"
        actual_result = less6.sentences_devider("Test. sentence. to. divide")
        expected_result = ["Test", "sentence", "to", "divide"]
        self.assertEqual(actual_result, expected_result)

    def test_sentences_divider_no_dots(self):
        "Test devision of text to a list sentences by a dot if there are no dots"
        actual_result = less6.sentences_devider("Test sentence to divide")
        expected_result = ["Test sentence to divide"]
        self.assertEqual(actual_result, expected_result)

    def test_words_counter(self):
        "Test count of words in a text"
        actual_result = less6.amount_of_words("Test sentence to count words")
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def test_words_counter_empty(self):
        "Test count of words in empty string"
        actual_result = less6.amount_of_words("")
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_capitalized_words_counter(self):
        "Test count of capitalized words"
        actual_result = less6.count_words("Test of capitals Counter Lalala")
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def test_capitalized_words_counter_no_capitals(self):
        "Test count of capitalized words if there is no such words"
        actual_result = less6.count_words("test of capitals no capitals")
        expected_result = 0
        self.assertEqual(actual_result, expected_result)




if __name__ == '__main__':
    unittest.main(verbosity=2)



