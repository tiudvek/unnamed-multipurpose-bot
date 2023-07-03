import io
from PIL import Image


async def parseAvatar(asset):
    result = Image.open(
        io.BytesIO(await asset.read())  # type: ignore # SHUT THE FUCK UPPP
    ).convert("RGBA")

    return result
