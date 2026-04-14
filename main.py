class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def check_balance(brackets):
    stack = Stack()
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in brackets:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return 'Несбалансированно'
            if stack.pop() != pairs[char]:
                return 'Несбалансированно'

    return 'Сбалансированно' if stack.is_empty() else 'Несбалансированно'


s = input()
print(check_balance(s))
