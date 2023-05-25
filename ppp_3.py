#  Reflecting on coding paradigms

# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        return Podracer(self.max_speed, "repaired", self.price)


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        return AnakinsPod(self.max_speed * 2, self.condition, self.price)


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        return other.repair()


pod = Podracer(100, "good", 1000)
anakin = AnakinsPod(200, "bad", 2000)
sebulba = SebulbasPod(300, "repaired", 3000)

anakin_boosted = anakin.boost()
print(anakin_boosted.max_speed)


# How does this solution ensure data immutability?
# 1) Variables are immutable as there are no modifications made to the existing objects. Instead, new objects are created with updated attributes.

# Is this solution a pure function? Why or why not?
# 2) The functions (repair(), boost(), and flame_jet()) are pure functions as they do not modify any external state and return new instances of the respective classes.

# Is this solution a higher order function? Why or why not?
# 3) No, Higher-order functions involve taking functions as arguments or returning functions as results.

# Would it have been easier to solve this problem using a different programming style?
# 4) No, I think using OOP allows us to encapsulate the data within the classes.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# 5) It's not, The condition from repaired to good, or bad should be managed by a mutable state.
