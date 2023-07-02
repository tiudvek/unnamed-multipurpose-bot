from disnake.ext import commands


class Imgen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Imgen(bot))
