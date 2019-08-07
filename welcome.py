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
        await member.send("""Hey! Welcome to our Discord server!
This is Cayde's Cache - Our VIP Carries and Account recoveries hangout.
Here you'll find all the help you could ever need; from casual tips, to raid carries, competitive boosts, pinnacle weapon runs and even raffles and giveaways for all our customers! :slot_machine: :eyes:

Before you continue, we only ask that you read these simple rules and abide by them while you're among us in our server.

1. Under no circumstances are users to PM one another within the discord. We want you all to make friends, but under NO circumstances are we liable if you are scammed. We are a 100% friendly, legit service - see our #reviews. Feel free to contact any of our review-leavers to confirm that they are in fact a real person and not a bot or a fake account. If you are caught PM'ing members of the discord you WILL be BANNED. Use the #general-chat for any and all conversations you might have here. Again, this is to prevent scamming - we are not liable if you do not follow this rule.
2. Please be kind and courteous to all discord employees and members at all times. We also will not tolerate harassment of any kind and anyone found to be breaking this rule will be subject to a 1 month mute and then a secondary offence will result in a lifetime ban.

3. Last but not least, please respect the time it takes to complete some of these tasks. Some of us have been working for upwards of 24 hours. Please do not be rude if we don't respond immediately. Sometimes we're even just playing a match of PvP! If you message an agent here on the Discord (who's names are in Green, Blue, Purple and Red to be clear!!) you WILL be responded to. Please be patient, we're listening :)


That's it! On the discord you'll find a few handy things: A general chat, for all general enquiries and chit chat, dedicated pages for each service. If you would like to get a quote, please copy&paste this 'form' below into the relevant channel and a discord Mod will be in contact with you!
COPY AND PASTE THIS FORM:


- - - - - - - - - - - - -
TIMEZONE:
I WOULD LIKE A:     CARRY   (Y/N)   //  ACCOUNT RECOVERY   (Y/N)
QUEST:
QUEST PROGRESS:
GLORY*:
- - - - - - - - - - - - -



*only if applicable to a competitive pinnacle quest
                """)


client = MyClient()
client.run(os.getenv("discord-mojo-token"))
