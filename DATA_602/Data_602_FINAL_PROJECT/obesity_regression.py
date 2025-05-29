from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_obesity = pd.read_csv("/Users/alex/SPS_MS_DS/DATA_602/Data_602_FINAL_PROJECT/Obesity_Risk_Factors_CDC.csv")

# Replace with your own loaded data
df_obesity = df_obesity[df_obesity["Class"].str.contains("Obesity", na=False)]

# Group and analyze
obesity_by_year = df_obesity.groupby("YearStart")["Data_Value"].mean().reset_index()
X = obesity_by_year[["YearStart"]].values
y = obesity_by_year["Data_Value"].values


# Fit polynomial regression (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
y_pred = model.predict(X_poly)

# Evaluate
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("RMSE:", round(rmse, 3))
print("R-squared:", round(r2, 3))

# Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X.flatten(), y=y, label="Actual")
plt.plot(X, y_pred, color="red", label="Polynomial Fit")
plt.title("Obesity Rate Over Time (Polynomial Regression)")
plt.xlabel("Year")
plt.ylabel("Obesity Rate (%)")
plt.legend()
plt.tight_layout()
plt.show()
