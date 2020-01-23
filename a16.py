import numpy as np
from matplotlib import pyplot as plt


def volume(resp):
    x = resp['time']
    y = resp['volume']
    plt.title("Volume Varying scatter diagram")
    plt.xlabel("time")
    plt.ylabel("volume")
    plt.plot(x, y, "ob")
    plt.show()

def avgPrice(resp):

    x = [9.30,10.30 ,11.30]
    y = [resp['time==9.30'],resp['time==10.30'],resp['time'==11.30]]
    x2 = [13.00, 14.00, 15.00]
    y2 = [resp['time==13.00'],resp['time==14.00'],resp['time'==15.00]]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('avgPrice Average value histogram')
    plt.ylabel('avgPrice')
    plt.xlabel('time')
    plt.show()

def ccl(resp):
    x = resp['time']
    y = resp['ccl']
    plt.title("ccl line chart")
    plt.xlabel("time")
    plt.ylabel("ccl")
    plt.plot(x, y)
    plt.show()

def netChangeRatio(resp):
    x = resp['time']
    y = resp['netChangeRatio']
    plt.title("netChangeRatio Varying scatter diagram")
    plt.xlabel("time")
    plt.ylabel("netChangeRatio")
    plt.plot(x, y, "ob")
    plt.show()

def amount(resp):
    x = resp['time']
    y = resp['amount']
    plt.title("amout line chart")
    plt.xlabel("time")
    plt.ylabel("amount")
    plt.plot(x, y)
    plt.show()

def Price(resp):
    x = resp['time']
    y = resp['Price Varying scatter diagram']
    plt.title("Price ")
    plt.xlabel("time")
    plt.ylabel("Price")
    plt.plot(x, y, "ob")
    plt.show()