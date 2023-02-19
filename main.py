# 221RDB249 Jānis Kārlis Zāģeris 2. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":                                        # Pārbauda atverošās iekavas
            opening_brackets_stack.append(Bracket(next_char, i))

        elif next_char in ")]}":                                      # Pārbauda aizverošās iekavas
            if not opening_brackets_stack:                            # Ja nav atverošās iekavas
                return i+1
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top.char, next_char):             # Ja atverošā iekava nesakrīt
                    return i+1

    if opening_brackets_stack:                                        # Ja joprojām ir palikušas atverošās iekavas un nav tām attiecīgās aizverošās iekavas
        return opening_brackets_stack[0].position+1

    return "Success"                                                  # Ja viss sakrīt


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()