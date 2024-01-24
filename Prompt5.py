import pandas as pd
import math

data = {
  "x": [],
  "sin(x)": []
}

# Load data into a DataFrame object:
df = pd.DataFrame(data)

for i in range(1001):
    x = i * (2 * math.pi) / 1000
    y = math.sin(x)
    # Round the values to a certain precision (e.g., 10 decimal places)
    df.loc[len(df.index)] = [round(x, 10), round(y, 10)]

print(df)


''' I had to ask chatgpt for help with rounding. My values were very close but not quite accurate for some reason. It explained it was because python was attempting to be too precise with floating point values.
import pandas as pd
import math

data = {
  "x": [],
  "sin(x)": []
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

for i in range (1001):
	x = ((i*(2*math.pi))/1000)
	y = (math.sin(x))
	df.loc[len(df.index)] = [x, y]

print(df)'''
