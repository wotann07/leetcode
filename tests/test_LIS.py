from unittest import TestCase

from longest_increasing_sequence import LIS


class TestLIS(TestCase):
    def test_get_longest_increasing_sequence(self):
        self.assertEqual(6, len(LIS.get_longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 80])))
        sample = '184 3 51 154 199 132 60 76 168 139 12 26 186 94 139 195 170 34 178 67 1 97 102 117 92 52 156 101 80' \
                 ' 86 41 65 89 44 19 40 129 31 117 97 171 81 75 109 127 167 56 97 153 186 165 106 83 19 24 128 71 132' \
                 ' 29 103 19 70 168 108 115 140 149 196 123 18 45 46 51 121 155 179 88 164 28 41 150 193 100 34 164' \
                 ' 124 114 187'
        print(sample)
        self.assertEqual(18, len(LIS.get_longest_increasing_sequence(list(map(int, sample.split(' '))))))
