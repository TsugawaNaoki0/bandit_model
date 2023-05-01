import random


class aaa_slot_class():
    def aaa_slot(self, count):
        result = random.random()
        rate = 0.3;



        if (result < rate):
            return 1
        else:
            return 0

class bbb_slot_class():
    def bbb_slot(self):
        result = random.random()
        rate = 0.5;
        if (result < rate):
            return 1
        else:
            return 0
