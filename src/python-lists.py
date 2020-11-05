def main():
    quantity_rows = int(input())
    output = []
    for _ in range(quantity_rows):
        args = input().split(' ')
        command_name = args[0]
        if command_name == 'insert':
            output.insert(int(args[1]), int(args[2]))
        elif command_name == 'remove' and int(args[1]) in output:
            output.remove(int(args[1]))
        elif command_name == 'append':
            output.append(int(args[1]))
        elif command_name == 'sort':
            output.sort()
        elif command_name == 'pop':
            output.pop()
        elif command_name == 'reverse':
            output.reverse()
        else:
            print(output)


if __name__ == '__main__':
    main()
