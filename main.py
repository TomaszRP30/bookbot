import sys


def get_book_text(filepath):
	with open(filepath) as f:
		contents = f.read()
		return contents

def main():
	if len(sys.argv) != 2:
        	print("Usage: python3 main.py <path_to_book>")
        	sys.exit(1)
	filepath = sys.argv[1]


	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")

	contents = get_book_text(filepath)
	from stats import get_words, count_letters, sorted_letter_counts
	word_count = get_words(contents)
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")

	letters = count_letters(contents)
	sorted_letters = sorted_letter_counts(letters)
	print("--------- Character Count -------")
	
	for entry in sorted_letters:
		char = entry['char']
		num = entry['num']
		print(f"{char}: {num}")
	print("============= END ===============")
if __name__ == "__main__":
	main()
