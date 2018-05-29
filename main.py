# def f(x):
#     return {
#         'PUSH': 'PUSH',
#         'POP': 'POP',
#     }[x]
#
# action = input('Enter the action : PUSH or POP')
# array = []
#
# numbers = 1
# while numbers != 0 :
#  x = input('Enter numbers to add: press 0 to exit')
#  if (x == '0'):
#      numbers = 0
#  else:
#      array.append(x)
#
# print(array)
# if (action == 'PUSH'):
#     print('PPPPPPPPPPPPPPPPPPPP')
#     print(f(action))
# elif (action == 'POP'):
#     print('POOOOOOOOOOOOOOOP')
#     print(f(action))
# else:
#     print('Wrong cmmand')

import re

new = re.sub('[A-Z]', '', 'HI aslj Jak aslkjP asljda ')
print(new)