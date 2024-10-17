def main():
    with open(
        "/home/adam_b/workspace/github.com/AdamBtech/bookbot/books/frankenstein.txt"
    ) as f:
        file_contents = f.read()
        count_words(file_contents)
        count_characters(file_contents)
        report(file_contents)


def count_words(file_name):
    with open(
        "/home/adam_b/workspace/github.com/AdamBtech/bookbot/books/frankenstein.txt"
    ) as f:
        file = f.read()
        word_list = file.split()
        word_counts = len(word_list)

    return word_counts


def count_characters(text):
    text = text.lower()

    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def report(file_name):
    char_count = count_characters(file_name)
    char_list = [
        {"char": char, "count": count}
        for char, count in char_count.items()
        if char.isalpha()
    ]
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_name)} words found in the document")
    print("")

    for char_info in char_list:
        print(
            f"The '{char_info['char']}' character was found {char_info['count']} times"
        )

    print("--- End report ---")


def sort_on(dict):
    return dict["count"]


if __name__ == "__main__":
    main()
