from fibonacci import *
import unittest


class TestFib(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
            fib(-2)
            fib(-3)
            fib(-4)

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            fib("Gun")
            fib(1.0)
            fib(list)

    def test_good_input(self):
        self.assertEqual(fib(1), [0])
        self.assertEqual(fib(6), [0, 1, 1, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()
