class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        entries = sorted(roman.items(), key=lambda x: -x[1])
        answer = ""

        rest = num
        for i in range(len(entries)):
            (letter, value) = entries[i]
            answer += letter * (rest // value)
            rest -= value * (rest // value)

        return answer


s = Solution()
print(s.intToRoman(3))  # III
print(s.intToRoman(58))  # LVIII
print(s.intToRoman(1994))  # MCMXCIV
