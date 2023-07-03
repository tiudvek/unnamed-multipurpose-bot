import io
from PIL import Image


async def parseAvatar(
    asset,
    resize: bool = False,
    dimensions: tuple = (),
    rotate: bool = False,
    rotatenumber: int = 0,
    rotate_expand: bool = True,
    rotate_resample=Image.BICUBIC,
):
    result = Image.open(
        io.BytesIO(await asset.read())  # type: ignore # SHUT THE FUCK UPPP
    ).convert("RGBA")

    result = result.resize(dimensions) if resize else result
    result = (
        result.rotate(
            rotatenumber,
            expand=rotate_expand,
            resample=rotate_resample,  # type: ignore # SHUT THE FUCK UPP
        )
        if rotate
        else result
    )

    return result
