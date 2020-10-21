from matplotlib import pyplot as plt

X = list(range(1, 66))
y = [2*x - 1 for x in X]

num = 0
den = 0
y_mean = sum(y) / len(y)
x_mean = sum(X) / len(X)
for i in range(len(X)):
    num += (X[i]*y[i] - y_mean * X[i])
    den += (X[i]*X[i] - x_mean * X[i])
# trained model
m = num / den
c = y_mean - m * x_mean

print("Slope", m, ", Intercept", c)
plt.scatter(X, y, s=5)

y_pred = [m*x + c for x in X]
plt.plot(X, y_pred, c="r")
plt.title("Linear Regression")
plt.show()
