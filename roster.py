#https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Davis", "Cadeau", "Bacot", "High", "Ryan", "Trimble", "Wojcik", "Washington", "Lebo", "Withers"],
          "First Name": ["RJ", "Elliot", "Armando", "Zayden", "Cormac", "Seth", "Paxson", "Jalen", "Creighton", "Jae'Lyn"],
          "Height": [72, 73, 83, 81, 77, 75, 77, 82, 73, 81],
          "Weight": [180, 180, 240, 225, 195, 195, 195, 230, 180, 215]}
data = pd.DataFrame(player)

data["BMI"] = round((data["Weight"]/2.205) / ((data["Height"]/39.37)**2), 2)

print(data)

data.to_csv("BMI.csv")
