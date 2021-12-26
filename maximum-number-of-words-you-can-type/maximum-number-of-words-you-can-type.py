class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word = 0
        counter = 0
        for char in text.split():
            word = word + 1
            for c in brokenLetters:
                if c in char:
                    counter = counter + 1
                    break

        return (word - counter)