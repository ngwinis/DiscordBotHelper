import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv
from config import Config
from utils.logger import setup_logger
from commands.basic import BasicCommands

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logger()


class PTITBot(commands.Bot):

    def __init__(self):
        # Setup intents
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            command_prefix=Config.COMMAND_PREFIX,
            intents=intents,
            help_command=None  # Disable default help command
        )

    async def setup_hook(self):
        """Called when the bot is starting up"""
        # Add cogs
        await self.add_cog(BasicCommands(self))
        logger.info("Bot setup completed")

    async def on_ready(self):
        """Called when the bot has successfully connected to Discord"""
        logger.info(f'{self.user} has connected to Discord!')
        logger.info(f'Bot is in {len(self.guilds)} guilds')

        # Set bot status
        await self.change_presence(activity=discord.Game(
            name=f"{Config.COMMAND_PREFIX}help | PTIT CTF 2025"))

    async def on_member_join(self, member):
        """Called when a new member joins the server"""
        try:
            # Get welcome channel
            welcome_channel = self.get_channel(Config.WELCOME_CHANNEL_ID)

            if welcome_channel is None:
                logger.warning(
                    f"Welcome channel with ID {Config.WELCOME_CHANNEL_ID} not found"
                )
                return

            # Create welcome embed
            description_text = f"""
            Chào mừng bạn {member.mention} đã tham gia server PTIT CTF 2025!
            Để đảm bảo quyền lợi, hãy thực hiện đúng các yêu cầu trong kênh <#{Config.RULES_CHANNEL_ID}>!
            """

            embed = discord.Embed(
                title="✨ CHÀO MỪNG THÀNH VIÊN MỚI ✨",
                description=description_text,
                color=discord.Color(0x3498db),
            )

            # Send welcome message
            await welcome_channel.send(embed=embed)
            logger.info(
                f'Welcome message sent for {member.name} (ID: {member.id})')

        except Exception as e:
            logger.error(f"Error in on_member_join: {e}")

    async def on_member_remove(self, member):
        """Called when a member leaves the server"""
        logger.info(f'{member.name} (ID: {member.id}) left the server')

    async def on_command_error(self, ctx, error):
        """Global error handler for commands"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(
                f"❌ Lệnh không tồn tại. Sử dụng `{Config.COMMAND_PREFIX}help` để xem danh sách lệnh."
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"❌ Thiếu tham số. Sử dụng `{Config.COMMAND_PREFIX}help {ctx.command}` để xem cách sử dụng."
            )
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Tham số không hợp lệ. Vui lòng kiểm tra lại.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f"⏰ Lệnh đang trong thời gian chờ. Vui lòng thử lại sau {error.retry_after:.1f} giây."
            )
        else:
            logger.error(f"Unhandled command error: {error}")
            await ctx.send(
                "❌ Đã xảy ra lỗi khi thực hiện lệnh. Vui lòng thử lại sau.")


def main():
    """Main function to run the bot"""
    # Check if token is available
    if not Config.DISCORD_TOKEN:
        logger.error("DISCORD_TOKEN not found in environment variables")
        return

    # Create and run bot
    bot = PTITBot()

    try:
        bot.run(Config.DISCORD_TOKEN)
    except discord.LoginFailure:
        logger.error("Invalid Discord token")
    except Exception as e:
        logger.error(f"Error running bot: {e}")


if __name__ == "__main__":
    main()
