import fuzzy as fz

import matplotlib.pyplot as plt

class temp:

    def run(t):
        temp_file = open("temp.txt", "r")
        temp_lines = temp_file.readlines()

        t_start = -30
        t_finish = 100
        print(t)
        T = []

        for temp in temp_lines:
            #print(temp.split(" "))
            array = temp.split(" ")

            if (array[1].lower() == "rtr"):
                if ("n" in array[3]):
                    array[3] = array[3][:-1]
                # print(array[3])
                m = fz.membership_function.RTr(int(t), array[0], int(array[2]), int(array[3]))
                T.append([array[0], m])
                a = int(array[2])
                b = int(array[3])
                x = [t_start, a, b, t_finish]
                y = [1, 1, 0, 0]
                plt.plot(x, y, label=array[0])
                # print(m)

            elif (array[1].lower() == "ltr"):
                if ("n" in array[3]):
                    array[3] = array[3][:-1]
                m = fz.membership_function.LTr(int(t), array[0], int(array[2]), int(array[3]))
                T.append([array[0], m])

                a = int(array[2])
                b = int(array[3])
                x = [t_start, a, b, t_finish]
                y = [0, 0, 1, 1]
                plt.plot(x, y, label=array[0])

            elif (array[1].lower() == "t"):
                if ("n" in array[4]):
                    array[3] = array[3][:-1]
                m = fz.membership_function.T(int(t), array[0], int(array[2]), int(array[3]), int(array[4]))
                T.append([array[0], m])

                a = int(array[2])
                b = int(array[3])
                c = int(array[4])
                x = [t_start, a, b, c, t_finish]
                y = [0, 0, 1, 0, 0]
                plt.plot(x, y, label=array[0])
            elif(array[1].lower()=="tr"):
                if ("n" in array[4]):
                    array[3] = array[3][:-1]
                m=fz.membership_function.Tr(int(t),array[0],int(array[2]),int(array[3]),int(array[4]),int(array[5]))
                T.append([array[0],m])
                a = int(array[2])
                b = int(array[3])
                c = int(array[4])
                d=int(array[5])
                x = [t_start, a, b, c, d, t_finish]
                y = [0, 0, 1, 1, 0, 0]
                plt.plot(x, y, label=array[0])
        print(T)
        plt.legend()
        plt.show()
        return T

    def interval(l_value):
        temp_file = open("temp.txt", "r")
        temp_lines = temp_file.readlines()

        t_start = -40
        t_finish = 100

        for temp in temp_lines:
            array = temp.split(" ")
            if(array[0].lower()==l_value):
                if (array[1].lower() == "rtr"):
                    t_start=-40
                    t_finish=int(array[3])
                elif (array[1].lower() == "ltr"):
                    t_start=int(array[2])
                    t_finish=100
                elif (array[1].lower() == "t"):
                    t_start=int(array[2])
                    t_finish=int(array[4])
                elif(array[1].lower()=="tr"):
                    t_start=int(array[2])
                    t_finish=int(array[5])
            else:
                continue
        return t_start,t_finish

#t=(temp.interval("normal"))
#print(t[0])