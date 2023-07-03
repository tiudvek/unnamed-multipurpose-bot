import json
import os
from disnake.ext import commands
from src.utils.functions import utils

config = json.load(open("src/core/config.json"))  # Fuck you, Windows users >:)


class Bot(commands.InteractionBot):
    def __init__(self):
        self.config = config
        self.utils = utils
        super().__init__(test_guilds=config["bot"]["test_guilds"])

    async def on_ready(self):
        print(f"Ready on {self.user} ({self.user.id})")

    def load_extensions(self):
        for filename in os.listdir("src/ext"):  # Fuck you, Windows users >:)
            if filename.endswith(".py"):
                cog_name = filename[:-3]  # Remove the '.py' extension
                cog_path = f"src.ext.{cog_name}"
                self.load_extension(cog_path)
                print(f"Loaded extension: {cog_path}")

    def main(self):
        self.load_extensions()
        self.run(self.config["bot"]["token"])
