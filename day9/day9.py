from collections import deque
import time

num_players = 464
last_marble = 70918

start_time = time.time()
circle = [0]
current_marble = (0, 0)
player = 0
marbles = list(range(last_marble, 0, -1))
scores = [0 for i in range(num_players)]
while len(marbles) > 0:
    marble_value = marbles.pop()

    pos, val = current_marble[0], current_marble[1]

    if marble_value % 23 == 0:
        # add marble to player score
        scores[player] += marble_value
        pos = (pos - 7) % len(circle)
        scores[player] += circle[pos]
        # print(marble_value, circle[pos])
        del circle[pos]
        current_marble = (pos, circle[pos])
    else:
        pos = (pos + 1) % len(circle) + 1
        circle.insert(pos, marble_value)
        current_marble = (pos, marble_value)

    player = (player + 1) % num_players

print(max(scores))
print("Time: %s sec" % (time.time() - start_time) )
# Part 2

num_players = 464
last_marble = 7091800

start_time = time.time()
circle = deque([0])
player = 0
marbles = list(range(last_marble, 0, -1))
scores = [0 for i in range(num_players)]
while len(marbles) > 0:
    marble_value = marbles.pop()
    if marble_value % 23 == 0:
        # add marble to player score
        circle.rotate(7)
        scores[player] += marble_value + circle.pop()
        circle.rotate(-1)
        # print(marble_value, circle[pos])
    else:
        circle.rotate(-1)
        circle.append(marble_value)
    player = (player + 1) % num_players

print(max(scores))
print("Time: %s sec" % (time.time() - start_time) )
