import InvalidNN as inv
from InvalidNN.utill import pretreatment
import csv

training_data = []
result = []

f = open("D:\Programming\Dataset\MNIST\mnist_train.csv")
for line in csv.reader(f):
    training_data.append(line)

for sample in training_data:
    result.append([[int(s) for s in sample[1:]], int(sample[0])])
training_data = result

training_data = pretreatment.one_hot(training_data, (0, 10), value=(0.01, 0.99))
training_data = pretreatment.data_normalization(training_data, rnge=(0.01, 0.09))

print(training_data[0])