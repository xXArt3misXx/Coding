import pandas as pd
import numpy as np
import math

data = {
  "x": [],
  "sin(x)": []
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
j = 1
for i in range (1001):
	x = ((i*(2*math.pi))/1000)
	y = (math.sin(x))
	df.loc[len(df.index)] = [x, y]
	j += 1
print(df) 