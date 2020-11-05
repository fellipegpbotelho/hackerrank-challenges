def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


def main() -> None:
    year = int(input())
    print(is_leap(year))


if __name__ == '__main__':
    main()
