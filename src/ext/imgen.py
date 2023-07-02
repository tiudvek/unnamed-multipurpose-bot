'''
Thanks to AlexFlipnote and the Dank Memer people for a lot of the code here
'''

import random

import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import disnake
from disnake.ext import commands

achievement_icons = {
    "1": "Grass block",
    "2": "Diamond",
    "3": "Diamond sword",
    "4": "Creeper",
    "5": "Pig",
    "6": "TNT",
    "7": "Cookie",
    "8": "Heart",
    "9": "Bed",
    "10": "Cake",
    "11": "Sign",
    "12": "Rail",
    "13": "Crafting bench",
    "14": "Redstone",
    "15": "Fire",
    "16": "Cobweb",
    "17": "Chest",
    "18": "Furnace",
    "19": "Book",
    "20": "Stone block",
    "21": "Wooden plank block",
    "22": "Iron ingot",
    "23": "Gold ingot",
    "24": "Wooden door",
    "25": "Iron Door",
    "26": "Diamond chestplate",
    "27": "Flint and steel",
    "28": "Glass bottle",
    "29": "Splash potion",
    "30": "Creeper spawnegg",
    "31": "Coal",
    "32": "Iron sword",
    "33": "Bow",
    "34": "Arrow",
    "35": "Iron chestplate",
    "36": "Bucket",
    "37": "Bucket with water",
    "38": "Bucket with lava",
    "39": "Bucket with milk",
    "40": "Diamond boots",
    "41": "Wooden hoe",
    "42": "Bread",
    "43": "Wooden sword",
    "44": "Bone",
    "45": "Oak log"
}


class Imgen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def achievement(
            self,
            inter: disnake.ApplicationCommandInteraction,
            text: str,
            title: str = 'Achievement get!'
    ):
        '''
        Make a minecraft achievement

        Parameters
        ----------
        text: The text of the achievement
        '''

        color = (255, 255, 0, 255)
        icon = random.randint(1, 45)

        randomimage = icon if icon else random.randint(1, 45)
        front = Image.open(f"src/utils/assets/achievement/{randomimage}.png")

        txt = Image.new("RGBA", (len(text) * 15, 64))

        fnt = ImageFont.truetype('src/utils/assets/_fonts/Minecraft.ttf', 16)
        drawn = ImageDraw.Draw(txt)

        width, height = drawn.textsize(text, font=fnt)
        width = max(320, width)

        mid = Image.new("RGBA", (width + 20, 64), (255, 255, 255, 0))

        midd = Image.open("src/utils/assets/achievement/achmid.png")
        end = Image.open("src/utils/assets/achievement/achend.png")

        for i in range(0, width):
            mid.paste(midd, (i, 0))
        mid.paste(end, (width, 0))

        txt = Image.new("RGBA", (width + 20, 64), (255, 255, 255, 0))

        drawn = ImageDraw.Draw(txt)
        drawn.text((0, 9), title, font=fnt, fill=color)
        drawn.text((0, 29), text, font=fnt, fill=(255, 255, 255, 255))
        mid = Image.alpha_composite(mid, txt)

        img = Image.new("RGBA", (width + 80, 64))

        img.paste(front, (0, 0))
        img.paste(mid, (60, 0))

        bio = io.BytesIO()
        img.save(bio, "PNG")
        bio.seek(0)
        file = disnake.File(bio, "image.png")

        await inter.send(file=file)

    @commands.slash_command()
    async def trash(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @trash.sub_command()
    async def peterparker(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
        '''
        Say that someone is trash

        Parameter
        ---------
        user: The user that is trash
        '''
        avatar = user.display_avatar
        avatar = await avatar.read()
        avatar = io.BytesIO(avatar)
        avatar = Image.open(avatar).convert('RGBA').resize((480, 480))

        base = Image.open('src/utils/assets/trash/peter.jpg').convert('RGBA')

        avatar = avatar.filter(ImageFilter.GaussianBlur(radius=6))
        base.paste(avatar, (480, 0), avatar)
        base = base.convert('RGBA')

        bio = io.BytesIO()
        base.save(bio, format='png')
        bio.seek(0)
        file = disnake.File(bio, 'image.png')

        await inter.send(file=file)


def setup(bot):
    bot.add_cog(Imgen(bot))
