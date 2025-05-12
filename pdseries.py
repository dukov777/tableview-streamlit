import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Method 1: Create from a dictionary
data = {
    'timestamp': [datetime(2025, 4, 1) + timedelta(days=i) for i in range(10)],
    'value': np.random.randn(10)
}
df1 = pd.DataFrame(data)
df1.set_index('timestamp', inplace=True)

# Method 2: Create with DatetimeIndex directly
dates = pd.date_range(start='2025-04-01', periods=10, freq='D')
df2 = pd.DataFrame({'value': np.random.randn(10)}, index=dates)

# Method 3: From existing data with pd.to_datetime()
timestamps = ['2025-04-01', '2025-04-02', '2025-04-03', '2025-04-04']
values = [10.2, 15.1, 13.5, 14.7]
df3 = pd.DataFrame({'timestamp': timestamps, 'value': values})
df3['timestamp'] = pd.to_datetime(df3['timestamp'])
df3.set_index('timestamp', inplace=True)


print(df1)
print(df2)
print(df3)

