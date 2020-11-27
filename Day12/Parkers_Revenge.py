
def read_fasta_file(filename: str) -> str:
    with open(filename, 'r') as f:
        temp = [line.strip() for line in f]
    seq = ''.join(temp[1:])
    return seq


def longest_prefix(suf1, suf2, mx=None):
    min_len = min(len(suf1), len(suf2))
    for i in range(min_len):
        if suf1[i] != suf2[i]:
            return (suf1[0:i], len(suf1[0:i]))
    return (suf1[0:i], len(suf1[0:i]))


def longest_repeat(txt):
    lst = sorted([text[i:] for i in range(len(text))])

    mxLen = 0
    mx_string = ""
    for x in range(len(lst) - 1):
        temp = longest_prefix(lst[x], lst[x + 1])
        if temp[1] > mxLen:
            mxLen = temp[1]
            mx_string = temp[0]
    first = txt.find(mx_string)
    last = txt.rfind(mx_string)
    return (first, last, mxLen)


text = read_fasta_file("pACYC184_short.fasta")
print(longest_repeat(text))

