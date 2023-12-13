#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Davis", "Cadeau", "Bacot"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)
