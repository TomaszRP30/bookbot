def get_words(contents):
        return len(contents.split())

def count_letters(contents):
	result = {}
	for l in contents:
		l = l.lower()
		if l.isalpha():

			if l not in result:
				result[l] = 0
			result[l] += 1
	return result

def sort_on(item):
    return item["num"]

def sorted_letter_counts(letter_dict):
    sorted_list = [{"char": k, "num": v} for k, v in letter_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
