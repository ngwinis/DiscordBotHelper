import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime
from config import Config

class BasicCommands(commands.Cog):
    """Basic commands for the Discord bot"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='hello', help='Chào hỏi người dùng')
    @commands.cooldown(1, Config.COMMAND_COOLDOWN, commands.BucketType.user)
    async def hello(self, ctx):
        """Greet the user"""
        greetings = [
            f'Xin chào, {ctx.author.mention}! 👋',
            f'Chào bạn, {ctx.author.mention}! 🌟',
            f'Hello {ctx.author.mention}! Chúc bạn một ngày tốt lành! ✨',
            f'Chào mừng {ctx.author.mention} đến với PTIT CTF 2025! 🎯'
        ]
        
        greeting = random.choice(greetings)
        await ctx.send(greeting)
        
    @commands.command(name='add', help='Cộng hai số: !add <số1> <số2>')
    @commands.cooldown(1, Config.COMMAND_COOLDOWN, commands.BucketType.user)
    async def add(self, ctx, a: int, b: int):
        """Add two numbers"""
        result = a + b
        
        embed = discord.Embed(
            title="🧮 Kết quả phép tính",
            description=f"**{a} + {b} = {result}**",
            color=discord.Color.green(),
            timestamp=datetime.utcnow()
        )
        
        embed.set_footer(text=f"Được yêu cầu bởi {ctx.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command(name='subtract', aliases=['sub'], help='Trừ hai số: !subtract <số1> <số2>')
    @commands.cooldown(1, Config.COMMAND_COOLDOWN, commands.BucketType.user)
    async def subtract(self, ctx, a: int, b: int):
        """Subtract two numbers"""
        result = a - b
        
        embed = discord.Embed(
            title="🧮 Kết quả phép tính",
            description=f"**{a} - {b} = {result}**",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        
        embed.set_footer(text=f"Được yêu cầu bởi {ctx.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command(name='multiply', aliases=['mul'], help='Nhân hai số: !multiply <số1> <số2>')
    @commands.cooldown(1, Config.COMMAND_COOLDOWN, commands.BucketType.user)
    async def multiply(self, ctx, a: int, b: int):
        """Multiply two numbers"""
        result = a * b
        
        embed = discord.Embed(
            title="🧮 Kết quả phép tính",
            description=f"**{a} × {b} = {result}**",
            color=discord.Color.purple(),
            timestamp=datetime.utcnow()
        )
        
        embed.set_footer(text=f"Được yêu cầu bởi {ctx.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command(name='divide', aliases=['div'], help='Chia hai số: !divide <số1> <số2>')
    @commands.cooldown(1, Config.COMMAND_COOLDOWN, commands.BucketType.user)
    async def divide(self, ctx, a: float, b: float):
        """Divide two numbers"""
        if b == 0:
            await ctx.send("❌ Không thể chia cho 0!")
            return
            
        result = a / b
        
        embed = discord.Embed(
            title="🧮 Kết quả phép tính",
            description=f"**{a} ÷ {b} = {result:.2f}**",
            color=discord.Color.orange(),
            timestamp=datetime.utcnow()
        )
        
        embed.set_footer(text=f"Được yêu cầu bởi {ctx.author.display_name}")
        await ctx.send(embed=embed)
        
    @commands.command(name='ping', help='Kiểm tra độ trễ của bot')
    async def ping(self, ctx):
        """Check bot latency"""
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Độ trễ: **{latency}ms**",
            color=discord.Color.gold(),
            timestamp=datetime.utcnow()
        )
        
        if latency < 100:
            embed.add_field(name="Trạng thái", value="🟢 Tuyệt vời", inline=True)
        elif latency < 200:
            embed.add_field(name="Trạng thái", value="🟡 Tốt", inline=True)
        else:
            embed.add_field(name="Trạng thái", value="🔴 Chậm", inline=True)
            
        await ctx.send(embed=embed)
        
    @commands.command(name='serverinfo', help='Thông tin về server')
    async def serverinfo(self, ctx):
        """Display server information"""
        guild = ctx.guild
        
        embed = discord.Embed(
            title=f"📊 Thông tin server: {guild.name}",
            color=discord.Color.blurple(),
            timestamp=datetime.utcnow()
        )
        
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        
        embed.add_field(name="👑 Chủ server", value=guild.owner.mention, inline=True)
        embed.add_field(name="👥 Thành viên", value=guild.member_count, inline=True)
        embed.add_field(name="💬 Kênh", value=len(guild.channels), inline=True)
        embed.add_field(name="🎭 Vai trò", value=len(guild.roles), inline=True)
        embed.add_field(name="📅 Ngày tạo", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="🆔 ID", value=guild.id, inline=True)
        
        await ctx.send(embed=embed)
        
    @commands.command(name='userinfo', help='Thông tin về người dùng: !userinfo [@user]')
    async def userinfo(self, ctx, member: discord.Member = None):
        """Display user information"""
        if member is None:
            member = ctx.author
            
        embed = discord.Embed(
            title=f"👤 Thông tin người dùng: {member.display_name}",
            color=member.color,
            timestamp=datetime.utcnow()
        )
        
        embed.set_thumbnail(url=member.display_avatar.url)
        
        embed.add_field(name="📛 Tên", value=member.name, inline=True)
        embed.add_field(name="🏷️ Biệt danh", value=member.display_name, inline=True)
        embed.add_field(name="🆔 ID", value=member.id, inline=True)
        embed.add_field(name="📅 Tham gia Discord", value=member.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="📅 Tham gia server", value=member.joined_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="🎭 Vai trò cao nhất", value=member.top_role.mention, inline=True)
        
        await ctx.send(embed=embed)
        
    @commands.command(name='help', help='Hiển thị danh sách lệnh')
    async def help_command(self, ctx, command_name=None):
        """Custom help command"""
        if command_name:
            # Show help for specific command
            command = self.bot.get_command(command_name)
            if command:
                embed = discord.Embed(
                    title=f"📖 Hướng dẫn lệnh: {Config.COMMAND_PREFIX}{command.name}",
                    description=command.help or "Không có mô tả",
                    color=discord.Color.blue()
                )
                
                if command.aliases:
                    embed.add_field(name="Tên khác", value=", ".join(command.aliases), inline=False)
                    
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"❌ Không tìm thấy lệnh `{command_name}`")
        else:
            # Show all commands
            embed = discord.Embed(
                title="📚 Danh sách lệnh",
                description="Sử dụng `!help <tên_lệnh>` để xem chi tiết",
                color=discord.Color.blue()
            )
            
            # Basic commands
            basic_commands = [
                "hello - Chào hỏi",
                "ping - Kiểm tra độ trễ",
                "add - Cộng hai số",
                "subtract - Trừ hai số",
                "multiply - Nhân hai số",
                "divide - Chia hai số",
                "serverinfo - Thông tin server",
                "userinfo - Thông tin người dùng"
            ]
            
            embed.add_field(
                name="🔧 Lệnh cơ bản",
                value="\n".join(f"`{Config.COMMAND_PREFIX}{cmd}`" for cmd in basic_commands),
                inline=False
            )
            
            embed.set_footer(text=f"Tiền tố lệnh: {Config.COMMAND_PREFIX}")
            await ctx.send(embed=embed)
