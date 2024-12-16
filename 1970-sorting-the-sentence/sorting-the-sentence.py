class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split() #  split the shuffled sentence into words
# s = "sentence4 a3 is2 This1"
# The split() function splits the sentence into a list of words. By default, split() splits by spaces, so:
# words = ['sentence4', 'a3', 'is2', 'This1']

        original_sentence = [""] * len(words) # create a list that will hold words in their original order (given in s )

# words = ['sentence4', 'a3', 'is2', 'This1']
# The length of words is 4, so we create a list original_sentence with 4 empty strings:
# original_sentence = ["", "", "", ""]

        for word in words: # now take each word at a time and extract the word 
            index = int(word[-1]) - 1  # Convert 1-indexed to 0-indexed
            actual_word = word[:-1]    # Remove the index from the word
            original_sentence[index] = actual_word # Place the word in its correct position

# First Iteration:
# word = 'sentence4'
# The last character of the word is '4'. We convert it to an integer and subtract 1 to get the 0-indexed position:
# index = int('4') - 1 = 3
# The rest of the word is "sentence", which is the actual word:
# actual_word = 'sentence'
# Now, we place "sentence" in the original_sentence list at index 3:
# original_sentence = ["", "", "", "sentence"]
# Second Iteration:
# word = 'a3'
# The last character is '3'. Convert it to an integer and subtract 1 to get the position:
# index = int('3') - 1 = 2
# The actual word is "a":
# actual_word = 'a'
# Place "a" in the original_sentence list at index 2:
# original_sentence = ["", "", "a", "sentence"]
# Third Iteration:
# word = 'is2'
# The last character is '2'. Convert it to an integer and subtract 1 to get the position:
# index = int('2') - 1 = 1
# The actual word is "is":
# actual_word = 'is'
# Place "is" in the original_sentence list at index 1:
# original_sentence = ["", "is", "a", "sentence"]
# Fourth Iteration:
# word = 'This1'
# The last character is '1'. Convert it to an integer and subtract 1 to get the position:
# index = int('1') - 1 = 0
# The actual word is "This":
# actual_word = 'This'
# Place "This" in the original_sentence list at index 0:
# original_sentence = ["This", "is", "a", "sentence"]


        return " ".join(original_sentence)

# After processing all the words, original_sentence is now ["This", "is", "a", "sentence"].
# The join() method joins the words with a space between them:
# " ".join(["This", "is", "a", "sentence"]) results in "This is a sentence"