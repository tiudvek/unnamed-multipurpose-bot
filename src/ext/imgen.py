"""
Thanks to AlexFlipnote and the Dank Memer people for a lot of the code here
"""

import random

from typing import Optional, Union

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
    "45": "Oak log",
}


class Imgen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def achievement(
        self,
        inter: disnake.ApplicationCommandInteraction,
        text: str,
        title: str = "Achievement get!",
    ):
        """
        Make a minecraft achievement

        Parameters
        ----------
        text: The text of the achievement
        """

        await inter.response.defer()

        color = (255, 255, 0, 255)
        icon = random.randint(1, 45)

        randomimage = icon if icon else random.randint(1, 45)
        front = Image.open(
            f"src/utils/assets/achievement/{randomimage}.png"
        )  # Fuck you, Windows users >:)

        txt = Image.new("RGBA", (len(text) * 15, 64))

        fnt = ImageFont.truetype(
            "src/utils/assets/_fonts/Minecraft.ttf", 16
        )  # Fuck you, Windows users >:)
        drawn = ImageDraw.Draw(txt)

        width, height = drawn.textsize(text, font=fnt)
        width = max(320, width)

        mid = Image.new("RGBA", (width + 20, 64), (255, 255, 255, 0))

        midd = Image.open(
            "src/utils/assets/achievement/achmid.png"
        )  # Fuck you, Windows users >:)
        end = Image.open(
            "src/utils/assets/achievement/achend.png"
        )  # Fuck you, Windows users >:)

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
        """Container for trash subcommands"""
        pass

    @trash.sub_command()
    async def peterparker(
        self, inter: disnake.ApplicationCommandInteraction, user: disnake.User
    ):
        """
        Say that someone is equal to trash

        Parameters
        ----------
        user: The user that is equal to trash
        """

        await inter.response.defer()

        avatar = await self.bot.utils.parseAvatar(
            user.display_avatar, True, (480, 480)
        )

        base = Image.open("src/utils/assets/trash/peter.jpg").convert(
            "RGBA"
        )  # Fuck you, Windows users >:)

        avatar = avatar.filter(ImageFilter.GaussianBlur(radius=6))
        base.paste(avatar, (480, 0), avatar)
        base = base.convert("RGBA")

        bio = io.BytesIO()
        base.save(bio, format="png")
        bio.seek(0)
        file = disnake.File(bio, "image.png")

        await inter.send(file=file)

    @trash.sub_command()
    async def belongs(
        self, inter: disnake.ApplicationCommandInteraction, user: disnake.User
    ):
        """
        Say that someone belongs in the trash can

        Parameters
        ----------
        user: The person that belongs in the trash
        """

        await inter.response.defer()

        trash = await self.bot.utils.parseAvatar(
            user.display_avatar, True, (175, 175)
        )

        face = await self.bot.utils.parseAvatar(
            inter.user.display_avatar, True, (175, 175), True, 5
        )

        base = Image.open("src/utils/assets/trash/image.png")
        hand = Image.open("src/utils/assets/trash/hand.png")

        base.paste(face, (375, 80), face)
        base.paste(trash, (105, 190), trash)
        base.paste(hand, (156, 164), hand)

        bio = io.BytesIO()
        base.save(bio, format="png")
        bio.seek(0)
        file = disnake.File(bio, "image.png")

        await inter.send(file=file)

    @commands.slash_command()
    async def filters(self, inter: disnake.ApplicationCommandInteraction):
        """Container for the filter subcommands"""
        pass

    @filters.sub_command()
    async def blur(
        self,
        inter: disnake.ApplicationCommandInteraction,
        radius: int,
        target: Optional[Union[disnake.User, disnake.Member]] = None,
    ):
        """
        Blur someone

        Parameters
        ----------
        target: The target of the blur; If none, defaults to the author
        radius: The ammount of blur to apply
        """

        await inter.response.defer()

        target = target or inter.user  # I did a funny

        avatar = await self.bot.utils.parseAvatar(
            target.display_avatar, True, (500, 500)
        )

        result = avatar.filter(ImageFilter.GaussianBlur(radius=radius))

        bio = io.BytesIO()
        result.save(bio, format="png")
        bio.seek(0)
        file = disnake.File(bio, "image.png")

        await inter.send(file=file)

    @filters.sub_command()
    async def emboss(
        self,
        inter: disnake.ApplicationCommandInteraction,
        target: Optional[Union[disnake.User, disnake.Member]] = None,
    ):
        """
        Apply emboss on someone

        Parameters
        ----------
        target: The target of the emboss; If none, defaults to the author
        """

        await inter.response.defer()

        target = target or inter.user  # I did a funny

        avatar = await self.bot.utils.parseAvatar(
            target.display_avatar, True, (500, 500)
        )

        result = avatar.filter(ImageFilter.EMBOSS)

        bio = io.BytesIO()
        result.save(bio, format="png")
        bio.seek(0)
        file = disnake.File(bio, "image.png")

        await inter.send(file=file)

    @filters.sub_command()
    async def contour(
        self,
        inter: disnake.ApplicationCommandInteraction,
        target: Optional[Union[disnake.User, disnake.Member]] = None,
    ):
        """
        Apply contour on someone

        Parameters
        ----------
        target: The target of the contour; If none, defaults to the author
        """

        await inter.response.defer()

        target = target or inter.user  # I did a funny

        avatar = await self.bot.utils.parseAvatar(
            target.display_avatar, True, (500, 500)
        )

        result = avatar.filter(ImageFilter.CONTOUR)

        bio = io.BytesIO()
        result.save(bio, format="png")
        bio.seek(0)
        file = disnake.File(bio, "image.png")

        await inter.send(file=file)


def setup(bot):
    bot.add_cog(Imgen(bot))
