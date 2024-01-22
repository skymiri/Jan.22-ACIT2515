class Locker:
    def __init__(self, code):
        if not isinstance(code, str) or len(code) < 3:
            raise AttributeError(
                "unlock_code must be a string with more than 3 numbers")

        self.locked = False
        self.code = code
        self.contents = []

    def lock(self):
        self.locked = True

    def unlock_with_code(self, code):
        if self.code == code:
            self.locked = False
            print("unlocked")
            return True

        else:
            return False

    def is_empty(self):
        return len(self.contents) == 0
