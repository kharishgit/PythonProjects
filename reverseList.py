def reverse_list(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)  # prints [5, 4, 3, 2, 1]