# 比較版本 #比較 #list比較

# versions = ['3.2.1', '3.2.12', '3.12.0',
#             '3.2', '3.1', '3.2.0', '3.2.20', '3.1.3']


def compareall():
    for i in range(len(versions)):
        for j in range(i, len(versions)):
            compare2(versions[i], versions[j])


def compare1(s1, s2):
    '''
    l1, l2 長度不一定一樣 比如 3.2 必須大於 3.1.100
    l1, l2 內容必須是數字比較，不能用文字比較
    '''
    l1 = [int(i) for i in s1.split('.')]
    l2 = [int(i) for i in s2.split('.')]
    if l1 > l2:
        return '>'
    elif l1 < l2:
        return '<'
    else:
        return '='


def compare2(s1, s2):
    '''
    傳統的比較方式，適用於其他語言 C/C++
    '''
    l1 = [int(i) for i in s1.split('.')]
    l2 = [int(i) for i in s2.split('.')]

    minlen = min(len(l1), len(l2))
    for i in range(minlen):
        if l1[i] > l2[i]:
            return '>'
        elif l1[i] < l2[i]:
            return '<'
    else:
        if len(l1) == len(l2):
            return '='
        elif len(l1) > minlen:
            return '>'
        else:
            return '<'


versions = ['3.0.9', '3.0.10', '3.1.9', '3.1.10',
            '3.2', '3.1', '3.2.0', '3.2.20', '3.3']

maxlist = None
for version in versions:
    versionlist = [int(i) for i in version.split('.')]

    if maxlist == None or versionlist > maxlist:
        maxlist = versionlist

print('maxlist=', maxlist)


compareall()

# versions = sorted(versions)

# print(versions)


assert '>' == compare1('3.2.1', '3.2')
assert '<' == compare1('3.1', '3.2')
assert '=' == compare1('3.2.1', '3.2.1')
assert '<' == compare1('3.1.1', '3.2')
assert '<' == compare1('3.9', '3.10')
assert '<' == compare1('3.2', '3.2.1')
assert '<' == compare1('3.2.1', '3.2.1_beta')
