class Card:
    def __init__(self, value, color):

        if isinstance(value, str):  # value 가 str 인지 확인  T or F 로 반환
            if value.isdigit():  # 숫자로만 이루어져있는지 확인
                value = int(value)
            else:
                raise AttributeError("Invalid value")

        if not isinstance(value, int) or not 1 <= value <= 10:
            raise AttributeError("Invalid value must between 1 to 10")

        if color not in ["red", "black"]:
            raise AttributeError("Invalid color")

        self.value = value
        self.color = color

    def is_stronger_than(self, other):
        if not isinstance(other, Card):
            return False

        return self.value > other.value
