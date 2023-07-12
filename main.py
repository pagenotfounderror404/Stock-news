import datetime
from twilio.rest import Client
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


apikey_news='074ecae060bb4b3b9bd861e837b99903'
apikey_stock=" C4924NH33DLOYTHC"

params_stock={
"apikey":apikey_stock,
"function":"TIME_SERIES_DAILY",
"symbol":STOCK,
"interval":"1day"
}

params_news={
    "apikey":apikey_news,
    "q":COMPANY_NAME,
    "language":"en",
    "sortBy":"popularity"
}
stock=requests.get(url=STOCK_ENDPOINT,params=params_stock)
news=requests.get(url=NEWS_ENDPOINT,params=params_news)
company_news=news.json()
yesterday=datetime.datetime.today()-datetime.timedelta(days=1)
day_before_yesterday=datetime.datetime.today()-datetime.timedelta(days=2)
price_on_yesterday=stock.json()["Time Series (Daily)"][f"{yesterday.date()}"]['4. close']
price_on_day_before_yesterday=stock.json()["Time Series (Daily)"][f"{day_before_yesterday.date()}"]['4. close']
difference_in_price=float(price_on_yesterday)-float(price_on_day_before_yesterday)
bignews=[]
bignewsdict={}
if difference_in_price/float(price_on_day_before_yesterday)*100>=5:
    for i in range (3):
       bignewsdict["title"]= company_news['articles'][i]['title']
       bignewsdict["description"]=company_news['articles'][i]['description']
       bignews.append(bignewsdict)


for i in range(3):
    bignewsdict["title"] = company_news['articles'][i]['title']
    bignewsdict["description"] = company_news['articles'][i]['description']
    bignews.append(bignewsdict)

account_sid = "AC602e5f1e63f5c7b7f26cf1c4de6475a1"
auth_token = "8d9da16a40a17028d8c7a162c9f3af05"
API_KEY="e722ca56f5d45806a4b72891544817af"
phone_number="+14787724404"

if bignews!=[]:
    client = Client(account_sid, auth_token)
    s=""
    for i in bignews:
        if s=="":
            s = s + i["title"] + "\n" + i["description"]
        else:
            s=s+"\n"+i["title"]+"\n"+i["description"]
    message = client.messages \
        .create(
        body=f"{s}",
        from_=phone_number,
        to='+919749595387'
    )