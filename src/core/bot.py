import json
from disnake.ext import commands

config = json.load(open('src/core/config.json')) # Fuck you, Windows users >:)

class Bot(commands.InteractionBot):
    def __init__(self):
        self.config = config
    
        super().__init__(
            test_guilds=config['bot']['test_guilds']
        )
    
    async def on_ready(self):
        print(f'Ready on {self.user} ({self.user.id})')
    
    def main(self):
        self.run(self.config['bot']['token'])