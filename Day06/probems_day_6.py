# """
# Name    : probems_day_6
# Author  : S. Urista
# HUID    : 81484503
# Date    : 03-Oct-2020
# Desc    :
# """
#
# # Takes a string and returns a list
# def parse_email_address(s):
#     "split a mail address into recipient and list of hops"
#     split_email = s.split("@")
#     steps_list = split_email[1].split(".")
#     split_email[1] = steps_list[::-1]
#     return split_email
#
# parse_email_address('jdp@world.std.com')
#
#
# def is_valid_parens_count(s):
#     "Is this a well-nested set of parentheses?"
#     count = 0
#     open_pars = "{[("
#     close_pars = "}])"
#     for par in s:
#         if par in open_pars:
#             count += 1
#         elif par in close_pars:
#             count -= 1
#
#     return count == 0
#
# is_valid_parens_count("{[)][]}")
#
# def is_valid_parens(s):
#     "Is this a well-nested set of parentheses?"
#     stack = []
#     parans_dict = {"(":")", "[":"]", "{":"}"}
#
#     for parens in s:
#         if parens in parans_dict:
#             stack.append(parens)
#         elif len(stack) == 0 or parans_dict[stack.pop()] != parans_dict:
#             return False
#
#     return len(stack) == 0
#
#
# def solitary(word):
#     solitary_dict = {}
#     for char in word:
#         if char.lower() in solitary_dict:
#             return False
#         else:
#             solitary_dict[char.lower()] = 1
#
#     return True
#
# solitary('subdermatoglyphic')
#
#
# import os
#
# #get current workind directory
# cwd = os.getcwd()
# print(os.listdir(cwd))
#
# #get everything split
# for roots, dirs, files in os.walk(cwd):
#     for file in files:
#         file_size = os.path.getsize(file)
#         print(file_size)

# #only the roots
# roots = next(os.walk(cwd))[0]
# # print("Roots = %s"% roots)
#
# #only the dirs
# dirs = next(os.walk(cwd))[1]
# print("Dirs = %s" % dirs)

# #only the files
# files = next(os.walk(cwd))[2]
# print("Files = %s" % files)



# def find_large_files(dirname, filesize):
#     "Return a list of large files below this point"
#     results = []
#     for root, dir, files in os.walk(dirname):
#         if os.stat(dirname).st_size < filesize:
#             results.append(name)
#
#     return results
#
# lst = find_large_files('..', 1048576)
# print(len(lst))

# d = {'one': 1, 'two': 2, 'three':3}
# for v in d:
#     if d[v] % 2 == 0:
#         print(v)

def compare (lst):
    for i in range(1,len(lst)):
        if lst[i-1] > lst[i]:
            return i
    return -1

print(compare([1,4,1,5,3]))
