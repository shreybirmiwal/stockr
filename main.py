import discord
import datetime
import pandas as pd
import yfinance as yf

def lowVol(ticker):
    tick = yf.Ticker(ticker.lower())
    gotData = tick.history(start="2022-6-10", interval="1d")
    avgVol = gotData["Volume"].mean()
    print(avgVol)
    curVol = gotData.iloc[gotData.shape[0]-1].Volume
    print(curVol)
    
    if(curVol < avgVol):
        return True
    else:
        return False

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith("!"):
        input = message.content.split()
        messageDict ={}

        #long/short
        messageDict['position'] = str(input[0])[1:]

        #ticker
        messageDict['ticker'] = str(input[1])

        #date
        messageDict['date'] = str(input[2])

        #time in UTC
        hour = int(input[3])
        minute = int(input[4])

        hour+=12
            
        messageDict['hour'] = hour
        messageDict['minute'] = minute

        #strat
        messageDict['strat'] = str(input[5])

        #rule
        messageDict['rule'] = str(input[6])

        day = int(messageDict['date'][0:1])
        month = int(messageDict['date'][2:4])
        year = int(messageDict['date'][5:9])
        hour = messageDict['hour']
        minute = messageDict['minute']

        #print(day)
        #print(month)
        #print(year)
        #print(str(datetime.date.today()))

        waitTill = datetime.datetime(year, day, month, hour , minute)
        print(waitTill)
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)

        await discord.utils.sleep_until(waitTill)

        output = ""
        for value in messageDict.values():
            if(not type(value) == int):
                output = output + " " + str(value)
                
        channel1 = client.get_channel(995804795195621416)
        await channel1.send("@everyone " + output)
        if(lowVol(messageDict['ticker'].lower())):
                await channel1.send("@everyone Previous day LOW VOLUME!")
        else:
                await channel1.send("@everyone Proceed with caution - high volume day previous")



client.run('')
s
