import numpy
import random

#linear regrassion
def hypothesis(theta_list,x_list,sample_idx):#sample_idx : column
    h = 0
    for i in range(0,len(theta_list)):
        h = h + theta_list[i]*x_list[i,sample_idx]
    return h
    
def cost(theta_list,x_list,y_list):
    J = 0
    m = len(y_list)
    for sample_idx in range(0,m):
        J = J + (hypothesis(theta_list,x_list,sample_idx) - y_list[sample_idx])**2
    J = J*0.5*1/m
    return J

def calc(theta_list,x_list,y_list,LR,totalCnt):
    diff = 0
    m = len(y_list)
    for cnt in range(0,totalCnt):   
        for attribute_idx in range(0,len(theta_list)):
            for sample_idx in range(0,m):
                diff = diff + (hypothesis(theta_list,x_list,sample_idx) - y_list[sample_idx])*x_list[attribute_idx,sample_idx]
            diff = diff/m
            theta_list[attribute_idx] = theta_list[attribute_idx] - LR*diff
        print("theta : ",theta_list)
        print("cost :",cost(theta_list,x_list,y_list))

def gen_sample_data():
    theta0 = random.randint(0, 5) + random.random()# for noise random.random[0, 1)
    theta1 = random.randint(0, 10) + random.random()
    theta2 = random.randint(0, 8) + random.random()
    num_samples = 100
    x_list = numpy.zeros([3,100])
    y_list = []
    theta_list = []
    for i in range(num_samples):
        x1 = random.randint(0, 100) * random.random()
        x2 = random.randint(0, 100) * random.random()
        y = theta0 + theta1*x1 + theta2*x2 + random.random() * random.randint(-1, 1)
        x_list[0,i] = 1
        x_list[1,i] = x1
        x_list[2,i] = x2
        y_list.append(y)
    theta_list.append(theta0)
    theta_list.append(theta1)
    theta_list.append(theta2)
    return x_list, y_list,theta_list

def run():
    x_list, y_list, theta_list = gen_sample_data()
    print("sample theta: ",theta_list)
    theta_list_test = []
    theta_list_test.append(random.randint(0, 10))
    theta_list_test.append(random.randint(0, 10))
    theta_list_test.append(random.randint(0, 10))
    LR = 0.001
    totalCnt=10000
    calc(theta_list_test,x_list,y_list,LR,totalCnt)
if __name__ == '__main__':
    run()