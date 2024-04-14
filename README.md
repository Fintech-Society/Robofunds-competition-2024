LIBF Fintech Society Robofunds Competition 2024
-----------------------------------------------
 
This is the readme file for the Robofund competition 2024, the objective of this competition is to build a model in python to predict market movements. This competition aims to improve skills in python, statistical knowledge and research. 

This file contains information you need for the competition and some resources to help research. 

This file is `README.md` and is plain text so you can open it locally with word, notepad, vscode etc.

# Tradable assets

Can trade both the asset and components

1.	S&P 500 (^GSPC)
2.	Nasdaq Composite (^IXIC)
3.	Bitcoin to USD (BTC-USD)
4.	Ethereum to USD (ETH-USD)

May trade index but not components:

1.	VIX index (^VIX)

# Rules

1. All code and data for submission should be within `/src` directory. All data must be pre-downloaded as well as the program being capable of finding and locating the data it requires.

2. The program must be compatable with backtesting.py

3. The file `example.py` is an example on how to use backtesting.py and will not be tested as a part of your submission.

4. Other reputable third party libaries can be used, however the program should not rely on them for all indicator generation and risk management purposes.

5. No intraday trading, minimum time period of data and trade is 1 day.

6. If your submission raises errors and does not work after a reasonable attempt to fix, you will be contacted and given 2 more chances to fix the errors within a total of 15 days.

7. Participants must be LIBF students.

# Winning criteria

Algorithic traders are measured by many metrics to acertain if they are viable.

The three main categories your algorithm will be evaluated in for this competition is:

1. Maximum drawdown
 - Zero is best

2. Excess returns and Risk adjusted returns
 - Higher is better

3. Exposure to market
 - Lower is better

There will be only one prize for the overall winner. Winning prize is the total for the team.

The winner will be revealed near the start of the next academic year (date TBD). 

The winning group and selected other groups will be asked to do a presentation. Refusual to do the presentation also means forfeiting the prize, if you have won.

The presentation will be on your research and the process of building your algorithm. It should be around 5 slides.

# Questions

## What is backtesting?

Backtesting is testing a predictive model on past data.

Data is revealed, one at a time, from the start of the time period to the end of the data period.

## What is algorithmic trading?

Algorithmic trading employs the use of computers to develop a set of rules to automate trading. 

Algorithmic traders are rewarded with the liquidity they provide to markets by finding pricing inefficiencies and then buying and selling to correct those prices. This inefficiency what a model aims to find and correct.

A model can be anything such as linear regression (auto regression) from CAPM to asking GPT-4 (neural networks) to make decisions. What matters most is that there is a set of rules to decide when to trade based of the model. 

## Aren't markets efficient?

According to EMH markets are, however the markets are still able to become irrational either over time or when faced with an event. Markets do not switch from being perfectly rational to completely irrational and they can take on a range of efficiency.

## What is the VIX index?

VIX is based on the options traded for the S&P500, specifically it is the market's expectation on volatility.

For first years, options will be covered in 5DRM, putting some research into options now will significantly help your understanding later. 

Trading the options themselves is disallowed for the competition.

# Resources

## Backtesting.py

One hour video covering backtesting.py

https://www.youtube.com/watch?v=e4ytbIm2Xg0

## LIBF

Enrique has made a course for learning python, use that as you get a badge for completing it.

https://brightspace.libf.ac.uk/d2l/home/44564

## Getting fundamentals of specific US companies. 

The SEC's api, EDGAR, allows for access to company information found in the quarterly and annual reports in an easier method for programs to access.

EDGAR returns information in a json format and is rate limited so **dont make more than 10 requests/second or you will be banned**.

https://www.sec.gov/edgar/sec-api-documentation

Example on getting the fundamental information for microsoft.

```python
import requests
import json

# You need to get the CIK number manually or have a lookup table for it.
URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json"

# For individuals use: Name email@<sample email domain>
headers = {"User-Agent": Sample Company Name AdminContact@<sample company domain>.com}

# Requests libary handles everything related to connecting to the internet for you.
response = requests.get(URL,headers=headers)

# Content is in json format, json.loads() turns it into a python dictionary
data = json.loads(response.content)

# Optional: Save file locally for futher use later
with open("MSFT.json","w") as f:
    f.write(json.dumps(data))
```

Explore the data to find what you need. But with the line `data["facts"]["us-gaap"]["RevenueFromContractWithCustomerExcludingAssessedTax"]["units"]["USD"]` you can get the reveneus starting from 2015, at least for microsoft.

## Price data

Yahoo finance is able to meet your price data requirements by using the yfinance library.

https://pypi.org/project/yfinance/

## Web scraping

Web scraping is programactially downloading data from sites. You should first find any API that is provided and use that before downloading the site. If a site has API access you can typically find somewhere at the bottom of the site.

Web scraping is an incredibly useful skill for gathering large amounts of data.

Some sites are harder to scrape than others and have been built to resist web scraping. There is also a lot of trial and error in web scraping.

Please be respectful to the site owners and make as few requests as possible.

https://www.youtube.com/watch?v=8dTpNajxaH0

### Beautiful soup

Used to read the HTML information from a site then beautiful soup converts the data from requests into a more accessible format to manipulate.

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

### Playwright

Automates web browsers and can also be used for webscraping.

https://playwright.dev/python/docs/intro

## Github

Github has a lot of resources and you can view working examples by just searching and browsing. This repository has a massive list of libaries to use for finance, even for different languages.

https://github.com/wilsonfreitas/awesome-quant?tab=readme-ov-file#python

### Git?

Git is what's used for keeping track of your code and sharing. It can be used for colabrative work but can be tricky to get working. Stick to google colab and juypter for colaborating and quickly iterating on your work then copy and paste the code when and where needed.

There is a difference between git and Github as Github is the site where the code is hosted while Git is the software.

## Corey Schafer

Has tutorials on a range of python topics, was inactive for a while but came back. Has a really good series on object orientated programming / python classes (which backtesting.py uses).

https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

## Quantpy

Youtuber that covers topics for quant finance using python.

https://www.youtube.com/@QuantPy

## 3blue1brown

The one of the best youtube channels relating to math and has videos on the fundamentals of neural networks and machine learning.

https://www.youtube.com/@3blue1brown

## Sebastian Lague

A channel which uploads infrequently but has very high quality videos. This video on neural networks is outstanding.

https://www.youtube.com/watch?v=hfMk-kjRv4c

## w3schools

Online and free site for learning programming, well organised and useful for referencing commands with examples.

https://www.w3schools.com/python/default.asp

## Gregory Gundersen

An online blog that covers a range of areas in quantitative finance and is short and well written to be understandable.

https://gregorygundersen.com/

## Python libaries and documentation

This list is not extensive and is only meant to get you started with what to use.

Each libary has documentation on their functions and uses, typically they will also have a introductry guide to help you or some examples.

If you get stuck you can copy and paste errors into google or search what you want to do and add "stackoverflow" or "quantoverflow" to the end. These sites are where people ask questions and the community answers them.

### backtesting.py

backtesting.py is an easy to use backtesting libary, others are available and it is possible to code your own. So that submissions are consistent use backtesting.py.

https://kernc.github.io/backtesting.py/doc/backtesting/#gsc.tab=0

### Numpy

Provides matricies and useful math functions. matricies can be used in a variety of situations such as modern portfolio theory.

https://numpy.org/doc/stable/

### pandas

Data frames are incredibly useful for data handling and makes life a lot easier.

https://pandas.pydata.org/docs/

### scipy

Excellent for statistics and time series analysis.

https://docs.scipy.org/doc/scipy/

### scikit-learn / statsmodels

Machine learning for python. Contains lots of tools for predictive analysis. 

https://scikit-learn.org/stable/

statsmodels is similar and also worth using

https://www.statsmodels.org/stable/index.html

also see [related projects](https://scikit-learn.org/stable/related_projects.html).

### Matplotlib and seaborn

https://matplotlib.org/

Seaborn uses matplotlib but seaborn is more often easier to use

https://seaborn.pydata.org/

# Non exhaustive list of topics to investigate

and base your model of in no particular order:

- Auto regressive models and ARIMA models
- Hidden markov models
- Support vector machines
- Neural networks
- Auto correlation
- Exponential moving average
- Stationarity
- Vector autoregression
- Normal distributions
- Hypothesis testing
- Dynamic linear models
- GARCH
- Brownian motion