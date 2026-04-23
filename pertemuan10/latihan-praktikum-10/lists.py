stack = []

stack.append('https://google.com')
stack.append('https://wikipedia.org')
stack.append('https://github.com')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

is_empty = not bool(stack)
print("isEmpty: ", is_empty)

print("Size: ",len(stack))