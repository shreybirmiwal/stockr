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

        #time in UTC
        hour = int(input[2])
        minute = int(input[3])

        hour+=12
            
        messageDict['hour'] = hour
        messageDict['minute'] = minute

        #strat
        messageDict['strat'] = str(input[4])

        #rule
        messageDict['rule'] = str(input[5])

        today = str(datetime.date.today())
        waitTill = datetime.datetime(int(today[:4]), int(today[5:7]), int(today[8:10]), messageDict['hour'], messageDict['minute'])
        #print(datetime.datetime.now())
        #print(waitTill)
        await discord.utils.sleep_until(waitTill)

        output = ""
        for value in messageDict.values():
            if(not type(value) == int):
                output = output + " " + str(value)

        await message.channel.send(output)


client.run('OTk1NTY3MzM3MzEyODk5MDgz.GSXeQ8.R6wu3WokdiF15H-Yh5groQiIZq_z-HnOTXXYNE')
s
