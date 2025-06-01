import pandas as pd

# Series is like single column 
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s.loc['a'])
print(s['a'])
print(s[0])

#loc selects rows by label while iloc thorugh position (starting from 0)

