from matplotlib import pyplot as plt
import numpy as np

X = np.array(list(range(1, 66)))
y = 2*X - 1

m = sum(X*y - np.mean(X)*y) / sum(X*X - np.mean(X)*X)
c = np.mean(y) - m * np.mean(X)

print("Slope", m, ", Intercept", c)
plt.scatter(X, y, s=5)

y_pred = [m*x + c for x in X]
plt.plot(X, y_pred, c="r")
plt.title("Linear Regression")
plt.show()
