class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            if digits[index] != 9:
                digits[index] = digits[index] + 1
                break
            else:
                digits[index] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
        