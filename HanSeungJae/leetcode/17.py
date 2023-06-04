class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(case, remainingDigits, map, cases):
            if len(remainingDigits) == 0:
                cases.append(case)
                return

            curDigit = remainingDigits[0]
            letters = map[curDigit]

            for letter in letters:
                backtrack(
                    case + letter,
                    remainingDigits[1:],
                    map,
                    cases,
                )

        cases = []
        backtrack("", digits, map, cases)

        return cases if cases != [""] else []


s = Solution()
print(s.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(s.letterCombinations(""))  # []
print(s.letterCombinations("2"))  # ["a","b","c"]
