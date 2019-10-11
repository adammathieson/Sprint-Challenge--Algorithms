'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

cache = []
def count_th(word):
    if len(word) < 2:
        return
    elif word[0:2] == 'th':
        cache.append(word[0:2])
    split_word = word[1:]
    count_th(split_word)

    return len(cache)

# print(count_th('')) #None
# print(count_th('abcthxyz')) #1
# print(count_th("abcthefthghith")) #3
# print(count_th("THtHThth")) #1