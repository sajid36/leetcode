class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1: return True
        res = {}
        res['#'] = 0
        serial = 1
        for ch in order:
            res[ch] = serial
            serial = serial + 1

        for i in range (len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            diff = abs(len(word1) - len(word2))
            if len(word1) > len(word2):
                word2 = word2 + '#'*diff
                for j in range(len(word1)):
                    if res[word1[j]] > res[word2[j]]:
                        return False
                    else:
                        if res[word1[j]] == res[word2[j]]:
                            continue
                        break
                    
            else:
                word1 = word1 + '#'*diff
                #print(word1, word2)
                for j in range(len(word1)):
                    if res[word1[j]] > res[word2[j]]:
                        return False
                    else:
                        if res[word1[j]] == res[word2[j]]:
                            continue
                        break
            
        return True
        