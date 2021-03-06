import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime


st.set_page_config(page_title='Stockapp',page_icon = "📈")

# App title
st.markdown('''
# Stock Price App
Shown are the stock price data for query companies!

''')
st.write('----------------------------------------------------------------------')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv("symbols.txt")
tickerSymbol = st.sidebar.selectbox('Stock ticker',ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

# Bollinger bands
st.header('**linechart**')
st.write('**Close and Volume**')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


qf=cf.QuantFig(tickerDf[20:100],title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

st.header('**barcharchart**')
st.write('**Close and Volume**')
st.bar_chart(tickerDf.Close)
st.bar_chart(tickerDf.Volume)



st.header('**Areachart**')
st.write('**Close and Volume**')
st.area_chart(tickerDf.Close)
st.area_chart(tickerDf.Volume)
