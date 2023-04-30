# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
import copy
import random

# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for color in range(value):
                self.contents.append(key)

    def draw(self, balls_number):
        drawed_balls = []
        if balls_number >= len(self.contents):
            return self.contents
        else:
            for _ in range(balls_number):
                drawed_ball_index = random.choice(range(len(self.contents)))
                drawed_balls.append(self.contents.pop(drawed_ball_index))
            return drawed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    as_expected_count = 0
    for _ in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        as_expected = True
        exp_draw = hatcopy.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            as_expected = True if exp_draw.count(key) >= value and as_expected else False
        if as_expected:
            as_expected_count += 1
    probability = as_expected_count / num_experiments
    print(probability)
    return probability


if __name__ == "__main__":
    pass

hat = Hat(blue=3, red=2, green=6)
probabil = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
