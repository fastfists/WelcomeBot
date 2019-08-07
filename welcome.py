import discord
import dotenv
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        await member.send("this is your DM")


client = MyClient()
client.run(os.getenv("discord-mojo-token"))
