def reverseWordSentence(Sentence):

		words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
	newSentence = " ".join(newWords)

	return newSentence
Sentence = "GeeksforGeeks is good to learn"
print(reverseWordSentence(Sentence))
