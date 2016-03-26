"""
Prints length of longest "folding subsequence" as defined by:
https://gist.github.com/whoshuu/6ec6da7ecb50834817a0
"""
def max_folding_subseq(arr):
    length = 1
    compare = None

    for i in range(len(arr)-1):
        curr = arr[i]
        next = arr[i+1]

        if compare:
            if compare == 'more' and next > curr:
                longest += 1
                compare = 'less'
            elif compare == 'less' and next < curr:
                longest += 1
                compare = 'more'
        elif next != curr:
            if next > curr:
                compare = 'less'
            elif next < curr:
                compare = 'more'
            longest += 1
    print(length)

max_folding_subseq([3, 6, 1, 2, 4, 3, 5, 5, 6, 1, 8, 3])