import pandas as pd
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt

def Liner_Regression(t_start,t_finish,h_start,h_finish,oper):

    f = pd.read_csv('data.csv')
    data = f.to_dict()

    new_data = []
    l = len(data['temp'])

    for i in range(l):
        if(oper=="or"):
            if (((int(data['temp'][i]) > t_start) and (int(data['temp'][i]) < t_finish)) or ((
                    int(data['nam'][i]) > h_start) and (
                    int(data['nam'][i]) < h_finish))):
                new_data.append([data['temp'][i], data['nam'][i], data['suv'][i]])
        else:
            if ((int(data['temp'][i]) > t_start) and (int(data['temp'][i]) < t_finish) and (
                    int(data['nam'][i]) > h_start) and (
                    int(data['nam'][i]) < h_finish)):
                new_data.append([data['temp'][i], data['nam'][i], data['suv'][i]])

    # print(new_data)

    df = pd.DataFrame(new_data, columns=['temp', 'nam', 'suv'])
    x = df[['temp', 'nam']]
    y = df['suv']

    print((df))

    reg = sklearn.linear_model.LinearRegression()
    reg.fit(x, y)

    print(reg.coef_)
    print(reg.intercept_)

    # ax = plt.figure().add_subplot(projection='3d')
    # ax.plot(df[['temp']],df[['nam']],df[['suv']])
    # plt.show()
    return round(reg.coef_[0],2), round(reg.coef_[1],2),round(reg.intercept_,2)