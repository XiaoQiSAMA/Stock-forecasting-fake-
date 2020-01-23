'''可视化'''
import matplotlib.pyplot as plt
import seaborn as sns
import tushare as ts
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        super(Figure_Canvas, self).__init__(fig)
        self.axes = fig.add_subplot(111)

    def vision(self, number):

            # 可视化函数
        sns.set_style("whitegrid")

            # 可视化部分
        stock = ts.get_hist_data(number, ktype='60')  # 获取5分钟k线数据
        stock['close'].plot(legend=True, figsize=(10, 4))  # 图形调整 close指昨日收盘价
        plt.savefig('stock_1.jpg')
        # plt.show()


            # 5日 10日 20日均线
        stock[['close', 'ma5', 'ma10', 'ma20']].plot(legend=True, figsize=(10, 4))
        plt.savefig('stock_2.jpg')
        # plt.show()
            # 股票每日涨跌幅
        stock['Daily Return'] = stock['close'].pct_change()
        stock['Daily Return'].plot(legend=True, figsize=(10, 4))
        plt.savefig('stock_3.jpg')
        # plt.show()
            # 核密度估计
        sns.kdeplot(stock['Daily Return'].dropna())
        plt.savefig('stock_4.jpg')
        # plt.show()
            # 核密度估计+统计柱状图
        sns.distplot(stock['Daily Return'].dropna(), bins=100)
        plt.savefig('stock_5.jpg')
        # plt.show()
            # 两支股票的皮尔森相关系数
        sns.jointplot(stock['Daily Return'], stock['Daily Return'], alpha=0.2)
        plt.savefig('stock_6.jpg')
