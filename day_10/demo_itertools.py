from string import ascii_letters, digits
from itertools import (
    combinations, combinations_with_replacement,
    permutations, zip_longest, cycle, chain
)
from pprint import pprint

nums = list(range(10))


def demo_combinations():
    pprint(list(combinations(nums, 2)))
    pprint(list(combinations(nums, 3)))


def demo_combinations_with_replacement():
    pprint(list(combinations_with_replacement(nums, 2)))
    pprint(list(combinations_with_replacement(nums, 3)))


def demo_permutations():
    pprint(list(permutations(nums, 2)))
    pprint(list(permutations(nums, 3)))


def demo_zip():
    for letter, digit in zip(ascii_letters, digits):
        print('- ', letter, digit)


def demo_zip_longest():
    for letter, digit in zip_longest(ascii_letters, digits, fillvalue=0):
        print('- ', letter, digit)


def demo_cycle():
    for letter, digit in zip(ascii_letters, cycle(digits)):
        print('- ', letter, digit)


def demo_chain():
    letters_list = list(ascii_letters)
    digits_list = list(digits)

    print(ascii_letters + digits)
    print(list(chain(ascii_letters, digits)))

    male_names = ['John', 'Jack']
    female_names = ['Ann', 'Sara']
    universal_names = ['Sam', 'Alex']

    first_names = [
        male_names,
        female_names,
        universal_names,
    ]

    color_names = ['Black', 'Brown', 'White']
    prof_names = ['Smith', 'Carpenter', 'Potter']

    last_names = [
        color_names,
        prof_names,
    ]

    all_names_incorrect = first_names + last_names
    print(all_names_incorrect)
    print(list(chain(*first_names, *last_names)))

    all_first_names = list(chain.from_iterable(first_names))
    print(all_first_names)

    all_last_names = list(chain.from_iterable(last_names ))
    print(all_last_names)


def main():
    demo_combinations()
    demo_combinations_with_replacement()
    demo_permutations()
    demo_zip_longest()
    demo_zip()
    demo_cycle()
    demo_chain()


if __name__ == '__main__':
    main()
