# Task 1

# def multiply_list(number: list[int]) -> int:
#     l = 1
#     for i in number:
#         l *= i
#     return l


# print(multiply_list([1, 2, 3, 4, 5, 7, 8, 9]))


# Task 2


# def minumum_of_list(numbers: list[int]) -> int:
#     if len(numbers) == 0:
#         return None
#     minimum = numbers[0]
#     for i in numbers:
#         if minimum > i:
#             minimum = i
#     return minimum


# print(minumum_of_list([1, 2, 0, -1, 2, -88]))


# Task 3


# def amount_of_prime(listr: list[int]) -> int:
#     amount = 0
#     for i in listr:
#         if i == 2:
#             amount += 1
#             continue
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             amount += 1
#     return amount


# print(amount_of_prime([2, 5, 4, 7, 8, 9, 4]))


# Task 4


# def delete_elements(listr: list[int], delete_it: list[int]) -> int:
#     amount, list_result = 0, listr.copy()
#     for i in listr:
#         if i == delete_it:
#             amount += 1
#             list_result.remove(delete_it)
#     return list_result, amount


# deleting_elemnt = 1
# print(delete_elements([1, 1, 1, 1, 1, 2, 8], deleting_elemnt))


# Task 5


# def unite_of_elements(list1, list2) -> list:
#     result_list = []
#     for i in list1:
#         if i not in result_list:
#             result_list.append(i)
#     for i in list2:
#         if i not in result_list:
#             result_list.append(i)
#     return result_list


# print(unite_of_elements([11, 1, 9], [11, 1, 2, 4, 5]))


# Task 6


# def result_of_something(listr: list[int], e) -> list:
#     result = []
#     for i in listr:
#         result.append(i**e)
#     return result


# print(result_of_something([1, 2, 3], 2))
