import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("Diamonds", 1)
        self.card1 = Card("Hearts", 9)
        self.card2 = Card("Clubs", 3)

    def test_check_for_ace__True(self):
        expected = True
        actual = CardGame.check_for_ace(self, self.card)
        self.assertEqual(expected, actual)

    def test_check_for_ace__False(self):
        expected = False
        actual = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(expected, actual)

    def test_highest_card__1_is_greater_than_card_2(self):
        expected = self.card1
        actual = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(expected, actual)

    def test_highest_card__2_is_less_than_card_1(self):
        self.card1 = Card("Hearts", 3)
        self.card2 = Card("Clubs", 9)
        expected = self.card2
        actual = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        cards = [self.card, self.card1, self.card2]
        expected = "You have a total of 13"
        actual = CardGame.cards_total(self, cards)
        self.assertEqual(expected, actual)
        