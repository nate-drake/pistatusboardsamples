from gpiozero import StatusBoard
from yahoo_finance import Share, Currency
from time import sleep

sb = StatusBoard('google', 'device', 'shares', 'xr')
share = Share('AAPL') # Change the ticker symbol to your chosen share here.
share_price = 150.53 # Enter the price you paid for your shares here
currency_pair = Currency('BTCUSD') # Enter your currency pair here.
currency_price = 4087.45 #Enter the price you paid for your currency here. 

while True:
    current_price = share.get_price() # Call the get_price method to get stock price
    cu_price = float(current_price) # Declare variable cu_price to convert stock price to floating point value.
    float(share_price) # Convert the price you paid to a floating value too.
    if cu_price >= share_price: # If share price is more than or equal to what you paid, switch on green led on third strip. 
        sb.shares.lights.red.off()
    else: # Otherwise switch on the red led:
        sb.shares.lights.red.on()
        sb.shares.lights.green.off()
    share.refresh()
    
    exchange_price = currency_pair.get_rate() # Call the get_rate method to get current exchange rate.
    xr_price = float(exchange_price) # Declare variable xr_price to convert exchange rate to floating point value.
    float(currency_price) # Convert the price you paid for the currency to a floating value too.
    if xr_price >= currency_price: # If exchange rate is more than or equal to what you paid, switch on green led on fourth strip. 
        sb.xr.lights.green.on()
        sb.xr.lights.red.off()
    else: # Otherwise switch on the red led:
        sb.xr.lights.red.on()
        sb.xr.lights.green.off()
    share.refresh()
    
    sleep(3)
