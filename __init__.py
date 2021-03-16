import pandas as pd
from io import StringIO
data = "col1,col2,col3\na,b,1\na,2\nc,d,3"
print(pd.read_csv(StringIO(data)))