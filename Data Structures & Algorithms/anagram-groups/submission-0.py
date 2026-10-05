class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_anagrams = []
        for i in range(len(strs)):
            anagrams = []
            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    anagrams.append(strs[j])
            if anagrams and not anagrams in total_anagrams:
                total_anagrams.append(anagrams)
        return total_anagrams
                