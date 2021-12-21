positions = [2,7]
scores = [0,0]

turn = 0
dice_value = 1
someone_won = False
while True:
  advance = dice_value + dice_value + 1 + dice_value + 2
  positions[turn] = (positions[turn] + advance) % 10
  scores[turn] += (positions[turn] - 1) % 10 + 1
  dice_value += 3
  print(turn, advance, positions[turn], scores[turn])
  if (scores[turn] >= 1000):
    print(scores)
    print(dice_value)
    print((dice_value - 1) * scores[(turn + 1) % 2])
    break
  turn = (turn + 1) % 2
