class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        out = []
        for item in words:
            s = ""
            for x in range (len(item)):
                s = s + letter [ord(item[x])-96-1]
            out.append(s)
        
        return (len(set(out)))
        