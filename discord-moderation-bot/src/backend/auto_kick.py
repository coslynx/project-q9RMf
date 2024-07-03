import discord

from discord.ext import commands

class AutoKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Implement auto-kick logic here
        if message.content == 'badword':
            await message.author.kick(reason='Auto kick for using inappropriate language')

def setup(bot):
    bot.add_cog(AutoKick(bot))