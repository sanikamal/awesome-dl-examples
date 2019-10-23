"""
Multilayer Perceptron model for binary classification. 

The model has 10 inputs, 3 hidden layers with 10, 20, and 10 neurons,and an output layer with 1 output.
Rectified linear activation functions are used in each hidden layer 
and a sigmoid activation function is used in the output layer,for binary classification."""

import tensorflow as tf
# from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense

visible = Input(shape=(10,))
hidden1 = Dense(10, activation= 'relu' )(visible)
hidden2 = Dense(20, activation= 'relu' )(hidden1)
hidden3 = Dense(10, activation= 'relu' )(hidden2)
output = Dense(1, activation= 'sigmoid' )(hidden3)

model = Model(inputs=visible, outputs=output)
# summarize layers
model.summary()
# plot graph
# plot_model(model, to_file= 'mlp_graph.png' )
