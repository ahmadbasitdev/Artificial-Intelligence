# By using class

"""Lab 4 - Task 1: Implement a stack using Python."""


class Stack:
    """Represent a last-in, first-out (LIFO) stack."""

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

def main() -> None:
    """Run a stack demonstration."""
    print("=== Lab 4 - Task 1: Stack ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped:", stack.pop())
    print("Top element:", stack.peek())
    stack.display()


if __name__ == "__main__":
    main()
