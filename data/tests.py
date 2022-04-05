import unittest
import data_generator


class TestScoreGenerator(unittest.TestCase):

    def test_simple(self):
        """
         A simple test without duplicate letters
        """
        guess = "angle"
        word = "angel"

        expected = [2, 2, 2, 1, 1]
        actual = data_generator.score(guess, word)

        self.assertEqual(expected, actual)

    def test_duplicate_1(self):
        """
        This test tests the case:
        actual word: contains duplicates
        guess word: does not contain duplicates
        and one of the duplicates is in the correct position
        """
        guess = "ample"
        word = "apple"

        expected = [2, 0, 2, 2, 2]
        actual = data_generator.score(guess, word)

        self.assertEqual(expected, actual)

    def test_duplicate_2(self):
        """
        This test tests the case:
        actual word: contains duplicates
        guess word: does not contain duplicates
        and none of the duplicates is in the correct position
        """
        guess = "amlpe"
        word =  "apple"

        expected = [2, 0, 1, 1, 2]
        actual = data_generator.score(guess, word)

        self.assertEqual(expected, actual)

    def test_duplicate_3(self):
        """
        This test tests the case:
        actual word: does not contain duplicates
        guess word: contains duplicates
        and one of the duplicates is in the correct position
        """
        guess = "apple"
        word = "ample"

        expected = [2, 0, 2, 2, 2]
        actual = data_generator.score(guess, word)

        self.assertEqual(expected, actual)

    def test_duplicate_4(self):
        """
        This test tests the case:
        actual word: does not contain duplicates
        guess word: contains duplicates
        and none of the duplicates are in the correct position
        """
        guess = "pulpy"
        word =  "ample"

        expected = [1, 0, 1, 0, 0]
        actual = data_generator.score(guess, word)

        self.assertEqual(expected, actual)

    def test_duplicate_5(self):
        """
        This test tests the case:
        actual word: contains duplicates
        guess word: contains duplicates
        and none of the duplicates are in the correct position
        """
        guess = "apple"
        word = "pulpy"

        expected = [0, 1, 1, 1, 0]
        actual = data_generator.score(guess, word)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
