from discord.ext import commands
import discord


class my_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='테스트')
    async def 테스트(self, ctx):
        await ctx.send(f'{ctx.author}: {self.bot.user} 정상 작동 중입니다.')

    @commands.command(name='청소')
    async def 청소(self, ctx, channel_name: str):
        channel = discord.utils.get(ctx.guild.channels, name=channel_name, type=discord.ChannelType.text)

        if not channel:
            await ctx.send(f"{channel_name} 채널을 찾을 수 없습니다.")
            return

        deleted = await channel.purge(limit=100)
        await ctx.send(f"{len(deleted)}개의 메시지를 {channel_name} 채널에서 삭제했습니다.")


async def setup(bot):
    await bot.add_cog(my_commands(bot))
