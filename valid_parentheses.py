def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    brackets = []
    d = {')': '(', ']': '[', '}': '{'}
    for e in s:
        if e in d.values():
            brackets.append(e)
        elif e in d:
            if not brackets or d[e] != brackets.pop():
                return False
    return not brackets