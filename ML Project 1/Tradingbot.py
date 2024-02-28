import requests
import pandas as pd
import matplotlib.pyplot as plt
API_KEY = 'JO10JGQDJ0NINUV3'

STOCK_SYMBOL = 'MSFT'
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

def weekly_stock_data(symbol: str):
    '''
    Get weekly stock data from alpha vantage
    '''
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()
    return data

def main():
    '''
    Main Function
    '''
    data = weekly_stock_data(STOCK_SYMBOL)
    df = pd.DataFrame.from_dict(data['Weekly Time Series'], orient = 'index')
    df.index = pd.DataFrame(df.index)
    df = df.astype(float)
    # plot the dataframe
    df['4. close'].plot()
    plt.title('Weekly Stock data')
    plt.show()
    print(df)

if __name__ == '__main__':
    main()