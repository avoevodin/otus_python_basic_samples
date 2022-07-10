from pprint import pprint
import sys


def parths():
    n = int(sys.stdin().readline().strip())
    start_num = 0

    for i in range(1, 2 * n, 2):
        start_num += 2 ** (i)

    end_num = 2 ** (2 * n) - 2**n + 1
    result = []

    for num in range(start_num, end_num, 2):
        b_num = "{0:b}".format(num)
        b_sum = 0

        for b_sym in b_num:
            b_sum += 1 if b_sym == "1" else -1
            if b_sum < 0 or b_sum > n:
                break

        if b_sum == 0:
            par_str = ""
            for b in b_num:
                par_str += "(" if b == "1" else ")"
            result.append(par_str)

    pprint(result)


def parths_bin():
    n = int(sys.stdin.readline().strip())
    start_num = 0

    for i in range(1, 2 * n, 2):
        start_num += 2**i

    start_num = get_bin_list(start_num)
    end_num = get_bin_list(2 ** (2 * n) - 2**n)
    result = []

    while True:
        b_sum = 0

        for b_sym in start_num:
            b_sum += 1 if b_sym == 1 else -1
            if b_sum < 0 or b_sum > n:
                break

        if b_sum == 0:
            par_str = ""
            for b in start_num:
                par_str += "(" if b == 1 else ")"
            result.append(par_str)

        if start_num == end_num:
            break

        start_num = increase_bin_num(start_num)
    print("\n".join(result))


def get_bin_list(bin_num):
    return [int(b) for b in "{0:b}".format(bin_num)]


def decrease_bin_num(b_num):
    i = len(b_num) - 2
    tail = 1
    while i > -1 and tail > 0:
        b = b_num[i]
        if b == 1:
            b_num[i] = 0
            tail = 1
        else:
            b_num[i] = 1
            tail -= 1

        if i == 0 and tail == 1:
            b_num.insert(0, 1)

        i -= 1
    return b_num


def increase_bin_num(b_num):
    i = len(b_num) - 2
    tail = 1
    while i > -1 and tail > 0:
        b = b_num[i]
        if b == 1:
            b_num[i] = 0
            tail = 1
        else:
            b_num[i] = 1
            tail -= 1

        if i == 0 and tail == 1:
            b_num.insert(0, 1)

        i -= 1
    return b_num


def main():
    parths_bin()


if __name__ == "__main__":
    main()
