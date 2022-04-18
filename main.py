import diskord
from diskord.ext import commands
import os
from replit import db # this used replits database to store the last known number so if the bot did get ratelimited it would pick up from where it last left off
import asyncio

intents = diskord.Intents.all()  
intents.members = True  

bot = commands.Bot(
	command_prefix="-",  # Change to desired prefix
	case_insensitive=True,# Commands aren't case-sensitive
  intents=intents,      #enables intents
)

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    await bot.change_presence(activity=diskord.Activity(type=diskord.ActivityType.competing, name="to 9k"))
    print(bot.user)  # Prints the bot's username and identifier

    # gets the latest db value, if it can't find it assume it's 0 and set it accordingly
    
    value = 0
    try: 
      value = db["key"]
    except:
      db["key"] = 0
      
     # get the channel
      
    channel = bot.get_channel(965577840894550016)
    
    # while it hasn't reached 9000 send the last value, increment it by 1 and sleep 1 second to avoid ratelimitations
    while value != 9001:
      await channel.send(value)
      value = value + 1
      db["key"] = value
      await asyncio.sleep(1)
      
    


bot.run(os.environ.get("token") )  # Starts the bot
