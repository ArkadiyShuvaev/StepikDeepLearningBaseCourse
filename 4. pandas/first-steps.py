import numpy as np
import pandas as pd


list = [1, 3, 5, np.nan, 6, 8]
series = pd.Series(list)
print(series)
print(series[2])
# 5.0

index = ["1st day", "2nd day", "3rd day", "4th day", "5th day", "6th day"]
series2 = pd.Series(list, index=index)
print(series2)
# 1st day    1.0
# 2nd day    3.0
# 3rd day    5.0
# 4th day    NaN
# 5th day    6.0
# 6th day    8.0

print(series2["3rd day"])
# 5.0

series3 = pd.Series(list, index=index, name="Temperature")
print(series3)
print(series3["3rd day"])
# 1st day    1.0
# ..............
# 6th day    8.0
# Name: Temperature, dtype: float6

print(series3[0:3])
# 1st day    1.0
# 2nd day    3.0
# 3rd day    5.0
# Name: Temperature, dtype: float64

print(series3[::-1])
# 6th day    8.0
# 5th day    6.0
# 4th day    NaN
# 3rd day    5.0
# 2nd day    3.0
# 1st day    1.0
# Name: Temperature, dtype: float64

date_range = pd.date_range("20230228", periods=10)
series4 = pd.Series(np.random.rand(10), index=date_range)
print(series4)
# 2023-02-28    0.594822
# 2023-03-01    0.826546
# 2023-03-02    0.073800
# 2023-03-03    0.383293
# 2023-03-04    0.407613
# 2023-03-05    0.048568
# 2023-03-06    0.137802
# 2023-03-07    0.890421
# 2023-03-08    0.112342
# 2023-03-09    0.396057
# Freq: D, dtype: float64

# Check if the values are greater than .5
values = series4 > .5
print(values)
# 2023-02-28    False
# 2023-03-01     True
# 2023-03-02    False
# 2023-03-03    False
# 2023-03-04    False
# 2023-03-05     True
# 2023-03-06    False
# 2023-03-07    False
# 2023-03-08     True
# 2023-03-09    False

# series4[series4 > .5]
print(series4[values])
# 2023-03-01    0.506672 (True)
# 2023-03-05    0.957485
# 2023-03-08    0.661586
# dtype: float64