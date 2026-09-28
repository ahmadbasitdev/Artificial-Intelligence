"""Lab 4 - Task 2: Implement a queue using Python."""


class Queue:
    """Represent a first-in, first-out (FIFO) queue."""

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)

def main() -> None:
    """Run a queue demonstration."""
    print("=== Lab 4 - Task 2: Queue ===")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print("Dequeued:", queue.dequeue())
    queue.display()


if __name__ == "__main__":
    main()