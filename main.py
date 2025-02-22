import argparse
import pathlib

from stats import get_num_words, get_total_char_counts


def main():
    parser = argparse.ArgumentParser("bookbot")
    parser.add_argument("book_file_path", type=pathlib.Path)
    args = parser.parse_args()

    book_file_path: pathlib.Path = args.book_file_path

    with book_file_path.open("r") as fp:
        content = fp.read()
        word_count = get_num_words(content)
        char_counts = get_total_char_counts(content)

    print(f"--- Begin report of {book_file_path} ---")
    print(word_count, "words found in the document")
    print()

    for c, count in sorted(char_counts.items(), key=lambda x: x[0]):
        print(f"{c}: {count}")


if __name__ == "__main__":
    main()
