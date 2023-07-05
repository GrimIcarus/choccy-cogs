from redbot.core import errors  # isort:skip
import importlib
import json
import os
import sys

try:
    import AAA3A_utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/AAA3A-AAA3A/AAA3A_utils.git`. A restart of the bot isn't necessary."
    )
modules = sorted(
    [module for module in sys.modules if module.split(".")[0] == "AAA3A_utils"], reverse=True
)
for module in modules:
    importlib.reload(sys.modules[module])
del AAA3A_utils
import AAA3A_utils
AAA3A_utils.dev.Cog = AAA3A_utils.Cog
AAA3A_utils.cog.DevEnv = AAA3A_utils.DevEnv
AAA3A_utils.dev.SharedCog = AAA3A_utils.SharedCog

from redbot.core.bot import Red  # isort:skip
from redbot.core.utils import get_end_user_data_statement

from .minecraft import Minecraft

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)


async def setup(bot: Red) -> None:
    cog = Minecraft(bot)
    await bot.add_cog(cog)