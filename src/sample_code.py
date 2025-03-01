import unittest

def rectangle_properties(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

class TestRectangleProperties(unittest.TestCase):

    def test_positive_values(self):
        length = 5
        width = 3
        expected_area = 15
        expected_perimeter = 16
        area, perimeter = rectangle_properties(length, width)
        self.assertEqual(area, expected_area)
        self.assertEqual(perimeter, expected_perimeter)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            rectangle_properties(0, 5)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            rectangle_properties(-5, 3)

if __name__ == '__main__':
    unittest.main()
