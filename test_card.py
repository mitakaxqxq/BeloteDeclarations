import unittest
from card import Card

class TestCardValidationOfValues(unittest.TestCase):

    def test_validation_raises_exception_when_value_is_not_str(self):

        exc = None

        try:
            card = Card(5,'spades')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - value must be of string type!')
    
    def test_validation_raises_exception_when_suit_is_not_str(self):

        exc = None
        spade=6
        try:
            card = Card('7',spade)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - suit must be of string type!')


    def test_validation_raises_assertion_error_when_value_is_not_in_array_values(self):

        exc = None

        try:
            card = Card('3','clubs')
            value=card.value

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect value!')
    
    def test_validation_raises_assertion_error_when_suit_is_not_in_suits(self):

        exc = None

        try:
            card = Card('7','tree')
            value=card.value

        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect suit!')
    

    def test_if_cards_are_equal_with_eq_dunder(self):
        card1=Card('7','clubs')
        card2=Card('7','clubs')

        self.assertEqual(card1,card2,'Not equal!')

    def test_if_card_is_lt_other_one_and_with_same_suits(self):
        card1=Card('7','clubs')
        card2=Card('8','clubs')

        self.assertTrue(card1<card2,'Card1 is bigger than card1')

    def test_if_card_is_lt_other_one_with_different_suits(self):
        card1=Card('7','clubs')
        card2=Card('8','hearts')

        self.assertTrue(card1<card2,'Card1 is bigger than card1')





if __name__ == '__main__':
    unittest.main()