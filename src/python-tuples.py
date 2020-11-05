def grab_inputs():
    n = int(input())
    integer_list = map(int, input().split())
    return n, integer_list


def main():
    n, integer_list = grab_inputs()
    print(hash(tuple(integer_list)))


if __name__ == '__main__':
    main()
