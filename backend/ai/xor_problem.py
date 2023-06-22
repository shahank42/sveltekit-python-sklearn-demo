import numpy as np
import sklearn.neural_network
import pickle


model_file_path = "ai/xor_model"

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 0])

model = sklearn.neural_network.MLPClassifier(
    activation="logistic", 
    max_iter=100, 
    hidden_layer_sizes=(2,), 
    solver="lbfgs"
)

model.fit(X, y)

print(model.predict(np.array([[0, 1]])))

pickle.dump(model, open(model_file_path, "wb"))