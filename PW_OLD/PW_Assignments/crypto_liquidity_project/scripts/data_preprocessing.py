# Drop nulls
df = df.dropna()

# Convert date column to datetime if exists
df['date'] = pd.to_datetime(df['date'])

# Select important numeric columns for scaling
from sklearn.preprocessing import MinMaxScaler

numeric_cols = ['price', 'volume_24h', 'market_cap']  # Adjust names to your dataset
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print(df.describe())
