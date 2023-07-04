import disnake
from disnake.ext import commands

import random
import xata


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command(self, inter):
        exists = self.bot.xata.exists("users", {"user_id": 1})
        print(exists)


def setup(bot):
    bot.add_cog(Events(bot))
