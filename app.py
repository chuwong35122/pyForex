import MetaTrader5 as mt
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def get_pairs(symbol):
    timezone = pytz.timezone('Etc/GMT+7')
    time_frame = mt.TIMEFRAME_H4
    timezone_now = datetime.now(timezone)
    timezone_from = timezone_now - relativedelta(weeks=24)

    rate = mt.copy_rates_range(symbol, time_frame, timezone_from, timezone_now)
    df = pd.DataFrame(rate)
    print(df.head())


authorized = mt.initialize(
    login=54231110, password='ehsg6xft', server='MetaQuotes-Demo')
if not authorized:
    print('Not Authorized.')
else:
    print('Login to 54230707 complete!')
    get_pairs('EURUSD')
