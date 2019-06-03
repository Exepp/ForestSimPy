class Vec2:
    def __init__(this, x, y):
        this.x = x
        this.y = y

    def __eq__(this, other):
        if isinstance(other, Vec2):
            return this.x == other.x and this.y == other.y
        return False
