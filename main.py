import argparse
import pathlib


def get_total_word_count(text: str) -> int:
    return len(text.split())


def get_total_char_counts(text: str) -> dict[str, int]:
    result = {}
    for c in text:
        if not c.isalpha():
            continue
        result.setdefault(c.lower(), 0)
        result[c.lower()] += 1
    return result


def main():
    parser = argparse.ArgumentParser("bookbot")
    parser.add_argument("book_file_path", type=pathlib.Path)
    args = parser.parse_args()

    book_file_path: pathlib.Path = args.book_file_path

    with book_file_path.open("r") as fp:
        content = fp.read()
        word_count = get_total_word_count(content)
        char_counts = get_total_char_counts(content)

    print(f"--- Begin report of {book_file_path} ---")
    print(word_count, "words found in the document")
    print()
    
    for c, count in sorted(char_counts.items(), key=lambda x: x[0]):
        print(f"The '{c}' character was found {count} times")


if __name__ == "__main__":
    main()

