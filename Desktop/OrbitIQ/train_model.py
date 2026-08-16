import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import r2_score
import joblib

# 1. Data Load
df = pd.read_csv("train.csv") 
print("Columns in dataset:", df.columns.tolist())

# 2. X, y
X = df.drop(['id', 'FloodProbability'], axis=1)
y = df['FloodProbability'] 

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model - Linear Regression = Lightening fast
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Check
pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, pred) * 100, "%")

# 6. Save
joblib.dump(model, 'flood_model.pkl')
print("Model saved as flood_model.pkl!")