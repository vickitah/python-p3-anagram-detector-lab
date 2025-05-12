# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            if candidate.lower() != self.word:
                if sorted(candidate.lower()) == self.sorted_word:
                    matches.append(candidate)
        return matches
