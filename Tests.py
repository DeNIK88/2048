import unittest
from logics import get_number_from_index, get_empty_list, get_index_from_number, is_zero_in_mas, move_left


class Tests_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 0), 5)

    def test_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_7(self):
        self.assertEqual(get_index_from_number(2), (0, 1))

    def test_8(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_9(self):
        mas = [
            [1, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_10(self):
        mas = [
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_11(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_12(self):
        mas = [
            [2, 2, 0, 0],
            [0, 0, 4, 4],
            [0, 0, 0, 0],
            [0, 8, 8, 0]
        ]
        rez = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [16, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), rez)

    def test_13(self):
        mas = [
            [8, 2, 4, 8],
            [0, 2, 4, 8],
            [8, 4, 2, 2],
            [2, 4, 8, 0]
        ]
        rez = [
            [8, 2, 4, 8],
            [2, 4, 8, 0],
            [8, 4, 4, 0],
            [2, 4, 8, 0]
        ]
        self.assertEqual(move_left(mas), rez)


if __name__ == "main":
    unittest.main()

