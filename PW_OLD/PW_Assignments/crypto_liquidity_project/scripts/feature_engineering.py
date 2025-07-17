# Moving Averages
df['ma_7'] = df['price'].rolling(window=7).mean()
df['ma_30'] = df['price'].rolling(window=30).mean()

# Volatility
df['volatility'] = df['price'].rolling(window=7).std()

# Liquidity Ratio
df['liquidity_ratio'] = df['volume_24h'] / df['price']

df = df.dropna()  # Remove rows with NaNs from rolling calculations

