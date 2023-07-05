from .mycog import RiotCog


async def setup(bot):
    await bot.add_cog(RiotCog(bot))