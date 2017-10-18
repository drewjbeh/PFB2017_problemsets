#!/usr/bin/env python3

# List copying methods

my_list = ['a','bb','ccc']
list_copy = my_list
print('List copy method 1', my_list)
list_copy.append('dddd')
print('Appended list copy', my_list)

my_list2 = ['a','bb','ccc']
list2_copy = my_list2.copy()
print('List copy method 2', my_list2)
list2_copy.append('dddd')
print('Appended list copy', my_list2)
