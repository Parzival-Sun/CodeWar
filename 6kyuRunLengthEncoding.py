import itertools
def run_length_encoding_v1(s):
    result = []
    prev = ''
    cnt = 0
    if s == '':
        return []

    for c in s:
        if prev == '':
            prev = c
            cnt += 1
        elif c == prev and prev != '':
            cnt += 1
        else:
            result.append([cnt, prev])
            prev = c
            cnt = 1
    result.append([cnt, prev])
    return result


def run_length_encoding(s):
    return [[len(list(v)), k] for k, v in itertools.groupby(s)]


print(run_length_encoding(""))
print(run_length_encoding("abc"))
print(run_length_encoding("aab"))
print(run_length_encoding("Hello, world!"))
print(run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb"))
print(run_length_encoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"))
