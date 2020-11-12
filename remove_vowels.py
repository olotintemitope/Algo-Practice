class Solution:
    def removeVowels(self, S: str) -> str:
        """ Check if the string is empty """
        if len(S) <= 0:
            return ""
        """ define vowels"""
        vowels = ['a', 'e', 'i', 'o', 'u']
        """ Split the words to hashmap"""
        words = [word for word in S]
        non_vowels = []

        for letter in words: #0(n)
            if letter not in vowels:
                non_vowels.append(letter) #0(1)

        return "".join(non_vowels)


sol = Solution()
print(sol.removeVowels("aeiou"))
