import requests
import yfinance as yahooFinance
import pandas as pd


df = pd.read_excel('path')

headers = {'User-Agent': "hasanallahyarov@address.com"}

# get all companies data
companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
    )

# dictionary to dataframe
companyData = pd.DataFrame.from_dict(companyTickers.json(),
                                     orient='index')


df['cik_str'] = df['cik_str'].astype(str)
companyData['cik_str'] = companyData['cik_str'].astype(str)
df = pd.merge(df, companyData, on='cik_str', how='left')

            

# Convert the 'Filed_At' column to datetime format
df['Filed_At'] = pd.to_datetime(df['Filed_At'], format='%Y%m%d')

# Convert the datetime format back to the desired format "YYYY-MM-DD"
df['Filed_At'] = df['Filed_At'].dt.strftime('%Y-%m-%d')
df['Price'] = None  
df['Price+1'] = None


for i in df.index:
    print(i)
    ticker=df['ticker'].iloc[i]
    
    if pd.notna(ticker):
        GetInformation = yahooFinance.Ticker(ticker)
    else:
        continue

    pd.set_option('display.max_rows', None)

    prices = GetInformation.history(period="max")
    
 
    
    prices.reset_index(inplace=True)
    
    prices['Date'] = pd.to_datetime(prices['Date'])
    
    prices['Date'] = prices['Date'].dt.strftime('%Y-%m-%d')
    
    desired_date = df['Filed_At'].iloc[i]
    
    
    result_df = prices[prices['Date'] == desired_date]
    
    if not result_df.empty:
        index_of_date = result_df.index[0]
    else:
        continue
    
    price_of_day = prices['Close'].iloc[index_of_date]
    
    price_of_next_day = prices['Close'].iloc[index_of_date+1]
    
    df.at[i, 'Price'] = price_of_day
    
    df.at[i, 'Price+1'] = price_of_next_day
    
    
