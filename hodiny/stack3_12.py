

class LimitedStack:
    def __init__(self, size):
        self.__stack = []
        self.__size = size

    def push(self, item):
        if not self.is_full():   #self.__stack < self.__size:
            self.__stack.append(item)
            return True

        return False

    def pop(self):
        try:
            return self.__stack.pop()

        except:
            return None

    def top(self):
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__size

    def get_size(self):
        return self.__size

    def __str__(self):
        return f"{self.__stack}"