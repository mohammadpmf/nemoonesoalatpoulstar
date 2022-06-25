# Q 1
# def get_rank_1(number):
#     if number >= 20:
#         print('A+')
#     if number > 17:
#         print('A')
#     if number > 14:
#         print('B')
#     if number > 12:
#         print('C')
#     if number <= 12:
#         print('F')

# def get_rank_2(number):
#     if number >= 20:
#         print('A+')
#     elif number > 17:
#         print('A')
#     elif number > 14:
#         print('B')
#     elif number > 12:
#         print('C')
#     else:
#         print('F')

# def get_rank_3(number):
#     if number >= 20:
#         print('A+')
#     else:
#         if number > 17:
#             print('A')
#         else:
#             if number > 14:
#                 print('B')
#             else:
#                 if number > 12:
#                     print('C')
#                 else:
#                     if number <= 12:
#                         print('F')
# get_rank_1(15)
# get_rank_2(15)
# get_rank_3(15)


# Q 6
# person = {
#     'name': 'Ali',
#     'family': 'Alavi',
#     'father': {
#         'name': 'Reza',
#         'age': 45
#     },
#     'mother': {
#         'name': 'Narges',
#         'age': 42
#     }
# }

# print(person['father']['age'])


# Q 7
import random
res = random.randint(1, 100) % 6 + 1
print(res)