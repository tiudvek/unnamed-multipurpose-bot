import io
from PIL import Image


async def parseAvatar(asset, resize: bool = False, dimensions: tuple = ()):
    result = Image.open(
        io.BytesIO(await asset.read())  # type: ignore # SHUT THE FUCK UPPP
    ).convert("RGBA")

    result = result.resize(dimensions) if resize else result

    return result
