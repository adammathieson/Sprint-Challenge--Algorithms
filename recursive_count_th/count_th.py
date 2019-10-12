'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if len(word) < 2:
        return 0
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else: 
        split_word = word[1:]
        return count_th(split_word)


# print(count_th('')) #None
# print(count_th('abcthxyz')) #1
# print(count_th("abcthefthghith")) #3
# print(count_th("THtHThth")) #1