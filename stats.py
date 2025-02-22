def get_num_words(text: str) -> int:
    return len(text.split())


def get_total_char_counts(text: str) -> dict[str, int]:
    result = {}
    for c in text:
        if not c.isalpha():
            continue
        result.setdefault(c.lower(), 0)
        result[c.lower()] += 1
    return result
