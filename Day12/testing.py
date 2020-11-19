
seq = "aabcaabdaab"

left_end = 0
right_end = len(seq) - 1

while left_end < right_end:
    midpoint = left_end + (right_end - left_end+1) // 2

if helper(mid):
    left_end = midpoint
else:
    right_end = midpoint - 1








# print(sol, max_length)