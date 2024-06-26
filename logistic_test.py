import numpy as np
from logistic import logistic
from logistic import sigmoid
import matplotlib.pyplot as plt


# set the parameter
train_rate = 0.8
n_samples = 200
n_features = 2

# get X_1
mean_1 = [-5, 0]
covariance_1 = np.eye(n_features)
X_1 = np.random.multivariate_normal(mean_1, covariance_1, n_samples)

# get X_2
mean_2 = [0, 5]
covariance_2 = np.eye(n_features)
X_2 = np.random.multivariate_normal(mean_2, covariance_2, n_samples)

# get y_1 and y_2
y_1 = np.ones(n_samples)
y_2 = -np.ones(n_samples)

# combine X and Y
X = np.concatenate((X_1, X_2), axis=0)
y = np.concatenate((y_1, y_2))

# then disrupt the order
indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
y = y[indices]

# get train and test
split_index = int(train_rate * X.shape[0])
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# get w
w = logistic(X_test, y_test, 500, 0.01)
print(w)

# calculate accuracy
right_num = 0
x = np.ones(X_test.shape[0]).T
X_test_augmented = np.insert(X_test, 0, x, 1)
for i in range(X_test_augmented.shape[0]):
    print("possibility:", sigmoid(np.dot(w, X_test_augmented[i])))
    if np.sign(sigmoid(np.dot(w, X_test_augmented[i])) - 0.5) == np.sign(y_test[i]):
        right_num += 1
print("test accuracy:", right_num / len(X_test) * 100, "%")

# draw the dataset
plt.figure(figsize=(8, 6))
plt.scatter(X_1[:, 0], X_1[:, 1], color='blue', label='+1 class')
plt.scatter(X_2[:, 0], X_2[:, 1], color='red', label='-1 class')

# draw the GeneralizedInverse boundary
x_plot = np.linspace(-10, 10, 100)
y_plot = -(w[1] * x_plot + w[0]) / w[2]
plt.plot(x_plot, y_plot, color='green', linestyle='--', label='boundary')

plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Data set and Boundary')
plt.legend()
plt.grid(True)
plt.show()
