import fuzzy as fz
import matplotlib.pyplot as plt

class hum:
    def run(h):
        hum_file = open("humidity.txt", "r")
        hum_lines = hum_file.readlines()
        hum_file.close()
        h_start = 0
        h_finish = 100
        print(h)
        H = []

        for line in hum_lines:
            #print(line.split(" "))
            row = line.split(" ")

            if (row[1].lower() == "rtr"):
                if ("n" in row[3]):
                    row[3] = row[3][:-1]
                # print(array[3])
                m = fz.membership_function.RTr(int(h), row[0], int(row[2]), int(row[3]))
                H.append([row[0], m])
                a = int(row[2])
                b = int(row[3])
                x = [h_start, a, b, h_finish]
                y = [1, 1, 0, 0]
                plt.plot(x, y, label=row[0])
                # print(m)

            elif (row[1].lower() == "ltr"):
                if ("n" in row[3]):
                    row[3] = row[3][:-1]
                m = fz.membership_function.LTr(int(h), row[0], int(row[2]), int(row[3]))
                H.append([row[0], m])

                a = int(row[2])
                b = int(row[3])
                x = [h_start, a, b, h_finish]
                y = [0, 0, 1, 1]
                plt.plot(x, y, label=row[0])

            elif (row[1].lower() == "t"):
                if ("n" in row[4]):
                    row[3] = row[3][:-1]
                m = fz.membership_function.T(int(h), row[0], int(row[2]), int(row[3]), int(row[4]))
                H.append([row[0], m])

                a = int(row[2])
                b = int(row[3])
                c = int(row[4])
                x = [h_start, a, b, c, h_finish]
                y = [0, 0, 1, 0, 0]
                plt.plot(x, y, label=row[0])
            elif (row[1].lower() == "tr"):
                if ("n" in row[4]):
                    row[3] = row[3][:-1]
                m = fz.membership_function.Tr(int(h), row[0], int(row[2]), int(row[3]), int(row[4]),
                                              int(row[5]))
                H.append([row[0], m])
                a = int(row[2])
                b = int(row[3])
                c = int(row[4])
                d = int(row[5])
                x = [h_start, a, b, c, d, h_finish]
                y = [0, 0, 1, 1, 0, 0]
                plt.plot(x, y, label=row[0])

        print(H)
        plt.legend()
        plt.show()
        return H


    def interval(l_value):
        hum_file = open("humidity.txt", "r")
        hum_lines = hum_file.readlines()
        hum_file.close()

        h_start = 0
        h_finish = 100

        for hum in hum_lines:
            array = hum.split(" ")
            if(array[0].lower()==l_value):
                if (array[1].lower() == "rtr"):
                    h_start=0
                    h_finish=int(array[3])
                    break
                elif (array[1].lower() == "ltr"):
                    h_start=int(array[2])
                    h_finish=100
                    break
                elif (array[1].lower() == "t"):
                    h_start=int(array[2])
                    h_finish=int(array[4])
                    break
                elif(array[1].lower()=="tr"):
                    h_start=int(array[2])
                    h_finish=int(array[5])
            else:
                continue
        return h_start,h_finish

#h=(hum.interval("kop"))

#print(type(h))