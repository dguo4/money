import backtrader as bt
import pandas as pd


# class MyStrategy(bt.Strategy):
#     pass

cerebro = bt.Cerebro()

data_address = '../data/VOO.csv'


def _convert_str_col_to_float(data_address):
    print('Start to convert string column to float ...')
    str_col = ["Open", "High", "Low", "Close", "Volume"]
    data = pd.read_csv(data_address)
    for col in str_col:
        if col == 'Volume':
            data[col]
        else:
            data[col] = data[col].astype(float)

    data.to_csv(data_address, index=False)
    print('finished ...')

_convert_str_col_to_float(data_address)

# daily_data = bt.feeds.GenericCSVData(
#     dataname = data_address,
#     # fromdate = Date.datetime(2000,1,1)
#     # todate = Date.datetime(2000,12,31)
#     nullvalue = 0,
#     dtformat = ('%m/%d/%Y'),
#     datetime = 0,
#     open = 1,
#     high = 2,
#     low = 3,
#     close = 4,
#     volume = 5,
#     openinterest = -1
# )

# cerebro = bt.Cerebro()

# cerebro.adddata(daily_data)

# cerebro.addstrategy(MyStrategy)

# cerebro.run()

# cerebro.plot()