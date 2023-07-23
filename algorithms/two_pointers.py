def algo_two_pointers(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list) - 1
    while left_pointer < right_pointer:
        # print(left_pointer, right_pointer)
        if sorted_list[left_pointer] + sorted_list[right_pointer] == target:
            return [left_pointer, right_pointer]
        elif sorted_list[left_pointer] + sorted_list[right_pointer] > target:
            right_pointer = right_pointer - 1
        else:
            left_pointer = left_pointer + 1


if __name__ == "__main__":
    sorted_list = [1, 2, 4, 5, 6, 7, 11, 13, 14]
    target = 9

    result = algo_two_pointers(sorted_list, target)
    print(result)
