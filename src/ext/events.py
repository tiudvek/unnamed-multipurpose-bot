import disnake
from disnake.ext import commands

import random
import xata


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command(self, inter):
        if self.bot.db.check_exists(inter.user.id):
            pass
        else:
            self.bot.db.new_user(inter.user.id, random.randint(0, 100))


def setup(bot):
    bot.add_cog(Events(bot))
