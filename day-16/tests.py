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

    def test_get_bits_operator_type_0(self):
        bytes = parser.convert_hex_to_bytes('38006F45291200')

        bit_value = parser.get_bits(bytes, 0, 3)
        self.assertEqual(bit_value, 1)

        bit_value = parser.get_bits(bytes, 3, 3)
        self.assertEqual(bit_value, 6)

        bit_value = parser.get_bits(bytes, 6, 1)
        self.assertEqual(bit_value, 0)

        bit_value = parser.get_bits(bytes, 7, 15)
        self.assertEqual(bit_value, 27)

    def test_literal(self):
        bytes = parser.convert_hex_to_bytes('D2FE28')
        (versions, offset, value) = parser.parse_value(bytes)
        self.assertEqual(value, [2021])

    def test_operator_type_0(self):
        bytes = parser.convert_hex_to_bytes('38006F45291200')
        (versions, new_offset, results) = parser.parse_value(bytes)
        self.assertEqual(versions, [1, 6, 2])
        self.assertEqual(results, [10, 20])

    def test_operator_type_1(self):
        bytes = parser.convert_hex_to_bytes('EE00D40C823060')
        (versions, new_offset, results) = parser.parse_value(bytes)
        self.assertEqual(versions, [7, 2, 4, 1])
        self.assertEqual(results, [1, 2, 3])

        bytes = parser.convert_hex_to_bytes('8A004A801A8002F478')
        (versions, new_offset, results) = parser.parse_value(bytes)
        self.assertEqual(versions, [4, 1, 5, 6])
        self.assertEqual(results, [15])

        bytes = parser.convert_hex_to_bytes('620080001611562C8802118E34')
        (versions, new_offset, results) = parser.parse_value(bytes)
        self.assertEqual(versions, [3, 0, 0, 5, 1, 0, 3])
        self.assertEqual(results, [10, 11, 12, 13])

        bytes = parser.convert_hex_to_bytes('C0015000016115A2E0802F182340')
        (versions, new_offset, results) = parser.parse_value(bytes)
        self.assertEqual(sum(versions), 23)

        bytes = parser.convert_hex_to_bytes('A0016C880162017C3686B18A3D4780')
        (versions, new_offset, results) = parser.parse_value(bytes)
        self.assertEqual(sum(versions), 31)

if __name__ == '__main__':
    unittest.main()
