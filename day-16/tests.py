import unittest
import parser

class TestParse(unittest.TestCase):

    def test_convert_hex_to_bytes(self):
        bytes = parser.convert_hex_to_bytes('D2FE28')
        self.assertEqual(bytes, [210, 254, 40])

    def test_get_bits_simple(self):
        bytes = parser.convert_hex_to_bytes('D2FE28')
        bit_value = parser.get_bits(bytes, 0, 3)
        self.assertEqual(bit_value, 6)

        bit_value = parser.get_bits(bytes, 3, 3)
        self.assertEqual(bit_value, 4)

        bit_value = parser.get_bits(bytes, 6, 1)
        self.assertEqual(bit_value, 1)

        bit_value = parser.get_bits(bytes, 7, 4)
        self.assertEqual(bit_value, 7)

        bit_value = parser.get_bits(bytes, 11, 1)
        self.assertEqual(bit_value, 1)

        bit_value = parser.get_bits(bytes, 12, 4)
        self.assertEqual(bit_value, 14)

        bit_value = parser.get_bits(bytes, 16, 1)
        self.assertEqual(bit_value, 0)

        bit_value = parser.get_bits(bytes, 17, 4)
        self.assertEqual(bit_value, 5)

    def test_value(self):
        parser.parse_value('D2FE28')

if __name__ == '__main__':
    unittest.main()
