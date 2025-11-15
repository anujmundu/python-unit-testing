from name_function import formatted_name


def interactive_demo():
    print('Enter name parts to format. Leave middle name blank if none.')
    first = input('First name: ').strip()
    middle = input('Middle name (optional): ').strip()
    last = input('Last name: ').strip()

    try:
        # If user leaves middle blank, pass empty string which is handled
        middle_arg = middle if middle else ''
        result = formatted_name(first, last, middle_arg)
        print('\nFormatted name:', result)
    except ValueError as e:
        print('Error:', e)


if __name__ == '__main__':
    interactive_demo()
