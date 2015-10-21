import random
import re


def getWordListFromData(filelocs):
	words = []
	for fileloc in filelocs:
		f = open(fileloc, 'r')
		for line in f:
			words.extend((line.rstrip()).split())

	return words


def trainMarkovChain(words):
	word_dict = dict()
	for i in range(len(words)):
		if(word_dict.has_key(words[i])):
			(word_dict.get(words[i])).append(words[i+1])
		else:
			word_dict[words[i]] = [words[i+1]]

	return word_dict


def getStartWords(words):
	start_words = []
	for word in words:
		if(re.match('^[A-Z].*', word)):
			start_words.append(word)

	return start_words


def isEndWord(word):
	if(re.search('[!.?]', word)):
		return True
	else:
		False


def makeRandomSentence(word_dict, start_words):
	random.seed(0)
	start_words_count = len(start_words)
	rand_start_word_index = random.randrange(start_words_count)

	word = start_words[rand_start_word_index]
	sentence = [word]
	while(isEndWord(word) is False):
		nextWords = word_dict.get(word)
		rand_index = random.randrange(len(nextWords))
		word = nextWords[rand_index]
		sentence.append(word)

	return " ".join(sentence)



filelocs = ['alice_tiny.txt', 'alice_test.txt']
words = getWordListFromData(filelocs)
word_dict = trainMarkovChain(words)
start_words = getStartWords(words)
sentence = makeRandomSentence(word_dict, start_words)
print(sentence)

