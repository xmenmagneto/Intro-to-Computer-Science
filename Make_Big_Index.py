def make_string(p):
	s = ''
	for e in p:
		s = s + e
	return s

def make_big_index(size):
	index = []
	letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
	while len(index) < size:
		word = make_string(letters)
		add_to_index(index, word, 'fake_url')
		for i in range(len(letters) - 1, 0 ,-1):
			if letters[i] < 'z':
				letters[i] = chr(ord(letters[i] + 1))
				break
			else:
				letters = 'a'
	return index
