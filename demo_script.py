"""Interactive demo for formatted_name function.

Run: python demo_script.py
"""
from name_function import formatted_name


def prompt_and_print():
    print('Interactive demo for formatted_name')
    first = input('First name: ').strip()
    middle = input('Middle name (optional): ').strip()
    last = input('Last name: ').strip()

    try:
        result = formatted_name(first, last, middle if middle else '')
        print('\nFormatted name:', result)
    except ValueError as e:
        print('Error:', e)


if __name__ == '__main__':
    prompt_and_print()
