from matplotlib import pyplot
import slot





if __name__ == '__main__':

    ddd = []
    fff = [0]
    ggg = []

    num = 500

    count = 0
    while (True):
        bbb = slot.aaa_slot_class()
        ccc = bbb.aaa_slot(count)
        print(ccc)  # ベルヌーイ
        ddd.append(ccc) # 0 or 1 を配列に入れていく
        eee = sum(ddd) / len(ddd)   # 現時点での、ddd の平均値
        fff.append(eee)     # ddd を配列に格納

        if(num < count):
            # print(str(len(fff)-num) + "@" + str(len(fff)))
            pyplot.cla()
            pyplot.ylim([0,1])
            pyplot.plot(range(len(fff)-num, len(fff)), fff[len(fff)-num:len(fff)+1], color='blue')
        else:
            pyplot.cla()
            pyplot.ylim([0,1])
            pyplot.plot(range(len(fff)), fff, color='blue')

        pyplot.savefig('image.png')

        count += 1
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # pyplot.show()
