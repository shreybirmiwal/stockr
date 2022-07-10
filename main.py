import discord
import datetime

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

        #time
        hour = int(input[2])
        minute = int(input[3])
        if(hour < 7):
            hour += 12
            
        messageDict['hour'] = hour
        messageDict['minute'] = minute


        #strat
        messageDict['strat'] = str(input[4])

        #rule
        messageDict['rule'] = str(input[5])

        today = str(datetime.date.today())
        waitTill = datetime.datetime(int(today[:4]), int(today[5:7]), int(today[8:10]), messageDict['hour'], messageDict['minute'],tzinfo=datetime.timezone.utc)
        print(waitTill)

        await discord.utils.sleep_until(waitTill)
        await message.channel.send(messageDict)


client.run('OTk1NTY3MzM3MzEyODk5MDgz.GZszpS.a8kEXCT2G-a4l6Q4TeIND7Zg8_7l5CDp27HrfQ')
s
