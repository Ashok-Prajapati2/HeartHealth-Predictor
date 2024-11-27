import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
data = {
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'feature3': np.random.rand(100),
    'feature4': np.random.rand(100),
    'target': np.random.choice([0, 1], size=100)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('testdata.csv', index=False)
print("testdata.csv created with synthetic data.")
