import unittest
from random_password_generator.generator import generate_password


class TestGeneratePassword(unittest.TestCase):

    def test_length(self):
        password = generate_password(upper=2, lower=4, digits=2, symbols=2)
        self.assertEqual(len(password), 10)

    def test_uppercase_count(self):
        password = generate_password(upper=2, lower=4, digits=2, symbols=2)
        self.assertEqual(sum(1 for c in password if c.isupper()), 2)

    def test_lowercase_count(self):
        password = generate_password(upper=2, lower=4, digits=2, symbols=2)
        self.assertEqual(sum(1 for c in password if c.islower()), 4)

    def test_digit_count(self):
        password = generate_password(upper=2, lower=4, digits=2, symbols=2)
        self.assertEqual(sum(1 for c in password if c.isdigit()), 2)

    def test_no_negative_values(self):
        with self.assertRaises(ValueError):
            generate_password(upper=-1, lower=4, digits=2, symbols=2)


if __name__ == '__main__':
    unittest.main()
