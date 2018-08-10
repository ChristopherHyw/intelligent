#encoding:utf-8
import numpy as np
import random

class Network(object):
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]

    def backprop(self,x,y):
        """返回元组"""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        # 存放激活值
        activations = [x]
        # list用来存放z向量
        zs = []
        # 向前传播
        for b,w in zip(self.biases,self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
            #向后传播
            delta =  self.cost_dervitive(activations[-1],y)*self.sigmoid(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta,activations[-2].transpose())

        for l in np.xrange(2,self.num_layers):
            z = zs[-1]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.weights[-l + 1].transpose(),delta) * sp
            nabla_b[-1] = delta
            nabla_w[-1] = np.dot(delta, activations[-l,-1].transpose())

        return (nabla_b,nabla_w)
    def evaluate(self,test_data):
        """返回正确的测试数量"""
        test_results = [(np.argmx(self.feedforward(x)),y) for (x,y) in test_data]
        return sum(int(x==y) for (x,y) in test_results)
    def sigmoid(self,z):
        """sigmoid函数"""
        return 1.0 / (1.0+np.exp(-z))

    def sigmoid_prime(self,z):
        """求导"""
        return self.sigmoid(z) * (1-self.sigmoid(z))

    def cost_derivative(self,output_activations,y):
        return (output_activations - y)

    def feedforward(self,a):
        """返回激活a"""
        for b,w in zip(self.biases,self.weights):
            a = self.sigmoid(np.dot(w,a)+b)
        return a

    def update_mini_batch(self,mini_batch,eta):
        """更新权重w和偏置b,主要使用bp"""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x,y in mini_batch:
            delta_nabla_b,delta_nabla_w = self.bachprop(x,y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(delta_nabla_w)]
        self.weights = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.weights,nabla_w)]
        self.biases = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]
    def SGD(self,training_data, epochs, mini_batch_size, eta, test_data=None):
        """使用SGD训练网络(x,y)输入的x，以及label"""
        if test_data:
            n_test = len(test_data)
            # 50000
            n = len(training_data)
            # epochs迭代
            for j in np.xrange(epochs):
                # 打散
                random.shuffle(training_data)
                # 10个数据一次迭代：mini_batch_size,以mini_batch_size为步长
                mini_batchs = [training_data[k:k + mini_batch_size] for k in np.xrange(0,n,mini_batch_size)]
                for mini_batch in mini_batchs:
                    self.update_mini_batch(mini_batch, eta)
                if test_data:
                    print("Epoch {0}:{1}/{2}".format(j, self.evaluate(test_data),n_test))
                else:
                    print("Epoch {0} complete".format(j))









