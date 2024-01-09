import discord
import discord.ext.commands.bot


class Client(discord.ext.commands.bot.Bot):

    # A few constants never hurt
    LOBBY_ID = 1190327818463215617
    NEWBIE_ROLE_ID = 1190600846011015258

    def __init__(self):
        super().__init__("\\", intents=discord.Intents.default() | 
                         discord.Intents(message_content=True, members=True))
        self.setup_commands()

    def setup_commands(self):
        # Bot commands
        @self.command()
        async def test(ctx):
            await ctx.send("test")

        @self.command
        async def steal_emoji(ctx):
            pass

    async def on_join(self, member: discord.Member):
        """Upon joining, assign the Jr. Associate consultant role"""
        await member.add_roles(member.guild.get_role(self.NEWBIE_ROLE_ID))
