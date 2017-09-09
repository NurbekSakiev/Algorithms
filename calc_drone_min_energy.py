def calc_drone_min_energy(route):
  diff = 0
  current = route[0][2]
  maxEnergyNeeded = 0
  for i in range(1, len(route)):
    current = (route[i-1][2] - route[i][2])
    if current < diff and abs(current) > diff:
      maxEnergyNeeded = max(maxEnergyNeeded, abs(current) - diff)
    elif current < diff:
      diff -= abs(current)
    else:
      diff += current
  return maxEnergyNeeded