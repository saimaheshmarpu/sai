# done by sai mahesh
import pandas as pd

ser = pd.Series(['virat','is','very','talented','crickter'])

newseries = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])

print(newseries)