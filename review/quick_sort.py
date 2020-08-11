import random

numbers = [4, 1, 2, 3, 6, 12, 10, 9, 8, 7]


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        q = random.choice(numbers)
        s_nums = []
        m_nums = []
        e_nums = []
        for i in numbers:
            if i < q:
                s_nums.append(i)
            elif i > q:
                m_nums.append(i)
            else:
                e_nums.append(i)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)


print(quick_sort(numbers))
