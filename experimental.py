import discord
import datetime
import pandas as pd
import yfinance as yf
import threading
import schedule
import time
import logging
import asyncio
from discord.ext import commands, tasks

client = discord.Client()
firstred = []
firstgreen =[]

@tasks.loop(minutes=1)
async def firststrat():
            
      for tick in firstred[::-1]:
            print(tick)
            
            ticker = yf.Ticker(tick.lower())
            gotData = ticker.history(start="2022-7-5", interval="1d")
            GreenOrRed = gotData.iloc[gotData.shape[0]-1].Close -  gotData.iloc[gotData.shape[0]-1].Open
            if(GreenOrRed < 0): #if it truly is red
                  print(tick + " ALERT! Has hit trigger of FIRST RED! GO LONG!")
                  channel2 = client.get_channel(996218343038140506)
                  await channel2.send(tick + " @everyone Has hit trigger of FIRST RED! GO LONG!")
                  
                  firstred.remove(tick)


      for tick in firstgreen[::-1]:
            print(tick)

            ticker = yf.Ticker(tick.lower())
            gotData = ticker.history(start="2022-7-5", interval="1d")
            GreenOrRed = gotData.iloc[gotData.shape[0]-1].Close -  gotData.iloc[gotData.shape[0]-1].Open
            if(GreenOrRed > 0): #if it truly is green
                  print(tick + " ALERT! Has hit trigger of FIRST GREEN! GO SHORT!")
                  channel2 = client.get_channel(996218343038140506)
                  await channel2.send(tick + " @everyone Has hit trigger of FIRST GREEN! GO SHORT!")
                  firstgreen.remove(tick)

      print(firstred)
     
@client.event
async def on_message(message):
      if message.author == client.user:
          return

      if message.content.startswith("firstred"):
          ticker = str(message.content)[9:]
          firstred.append(ticker)
          print("red")
          print(firstred)

      if message.content.startswith("firstgreen"):
          ticker = str(message.content)[11:]
          firstgreen.append(ticker)
          print("green")
          print(firstgreen)

        
def main():

      firststrat.start()
      client.run('OTk2MTcxMTc1MDM2MTk4OTQz.GyF2V_.Slz6MB8e8VYT6DRmPdqtWGOUgWxcUp7DMyZ8ic')

if __name__ == '__main__':
    main()
