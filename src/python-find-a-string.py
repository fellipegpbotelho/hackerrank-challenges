from typing import Tuple


def get_inputs() -> Tuple[str, str]:
    string = input()
    substring = input()
    return string, substring


def found_substring(index: int) -> bool:
    return index != -1


def get_number_of_occurrences(substring: str, string: str) -> int:
    ocurrences: int = 0
    index: int = string.find(substring)
    while found_substring(index):
        ocurrences += 1
        index = string.find(substring, index+1)

    return ocurrences


def main() -> None:
    string, substring = get_inputs()
    occurrences = get_number_of_occurrences(substring, string)
    print(occurrences)


if __name__ == '__main__':
    main()
