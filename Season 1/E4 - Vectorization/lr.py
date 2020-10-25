from matplotlib import pyplot as plt
import numpy as np

X = np.array(list(range(1, 66)))
y = 2*X - 1

# this was the line in the video, and there's a small mistake in this line
# m = sum(X*y - np.mean(X)*y) / sum(X*X - np.mean(X)*X)
# it is supposed to be
m = m = sum(X*y - np.mean(y)*X) / sum(X*X - np.mean(X)*X)
c = np.mean(y) - m * np.mean(X)

print("Slope", m, ", Intercept", c)
plt.scatter(X, y, s=5)

y_pred = [m*x + c for x in X]
plt.plot(X, y_pred, c="r")
plt.title("Linear Regression")
plt.show()
