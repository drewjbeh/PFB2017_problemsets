#!/usr/bin/env python3

# List copying methods

list = ['a','bb','ccc']
list_copy = list
print('List copy method 1', list)
list_copy.append('dddd')
print('Appended list copy', list)

list2 = ['a','bb','ccc']
list2_copy = list2.copy()
print('List copy method 2', list2)
list2_copy.append('dddd')
print('Appended list copy', list2)
