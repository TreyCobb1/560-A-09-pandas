#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Davis", "Cadeau", "Bacot"]
player = {"Last Name": roster,
          "First Name": ["RJ", "Elliot", "Armando"],
          "Height": [72, 73, 83],
          "Weight": [180, 180, 240]}
data = pd.DataFrame(player)
print(data)
