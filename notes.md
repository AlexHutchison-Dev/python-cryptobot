# Crypto Trading Bot

# Project aims and overview

This project aims to produce a simple crypto trading bot, that follows a simple trend following
trading algorithm to manage a small pot of real money. It will need to access the api of a tradeing
platform every second or so to get pricing information, analyse said information and decide on what
trading actions are appropriate as a result.

## MVP requirements

  * Connect to trading platform api
  * Aquire pricing information on which ever currencies chosen
  * Clean and store data for analysis
  * Analyze data according to trading strategy and move as necessary
  * Log and report results of trading activity 

##  Trading strategy research

Some research on suitable, simple trading algorithm's inorder to decide which strategy's to consider
for implementation.  I think some for m of simple trend following or moving average analysis will be
the simplest to start with.

### Api choice

I think i am going to go with kraken.com  as they seem to be a big and well respected player in the
market with a well documented API.  Binance is probably the main alternative but I feel that there
seems to be a lot more scepticism about there authenticity and reliability, not what you want when
the business necessitates trusting them with your money.

### Algorithmic trading stratergies

#### Mean reversion 

Mean reversion assumes that asset price will revert to the average price over time. If the market 
has a huge rally one week, this strategy assumes that the market will dip the following week.  There
are a couple of strategies designed to exploit mean reversion. 
  * Pairs Traiding  - This works by correlating two securities that tend to follow the same trends,
  however as they sometime diverge, trading oportunies appear as they will likely close to a similar
  level.

  * 

## Crypto trading api's

### Binance 
  Binance api 
## Sources

#### Trading algrothms
https://medium.com/swlh/a-step-by-step-guide-towards-a-trend-following-trading-strategy-814b198b815

### Mistakes to avoid

* When back testing avoid overfitting to the data, use only 60% to design rulesand test on 100%
* When back testing don't use future data.
