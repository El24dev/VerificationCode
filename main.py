import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType, utils
from discord_slash.utils.manage_commands import create_option

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="verificationembed",
           description="Manda el embed de verificacion",
           options=[
               create_option(
                   name="channel",
                   description="Choose the channel where the embed will be sent.",
                   option_type=SlashCommandOptionType.CHANNEL,
                   required=True # Do Not Touch
               ),
           ])
async def verificationembed(ctx, canal: discord.TextChannel = None):
    embed = discord.Embed(
        title="Verification",
        url="", # redirect by clicking on the title link
        description="", # EMBED Description Message
        color=discord.Color.from_rgb(255, 105, 180)
    )
    embed.set_image(url="") # The link to your image
    embed.set_footer(text="Dev by El24")
    
    message = await (canal or ctx.channel).send(embed=embed)
    await message.add_reaction("YOUR_EMOJI")
    await ctx.send(f"Mensaje enviado al canal <#{message.channel.id}>", hidden=True)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return
    
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    
    if str(payload.emoji) == "YOUR_EMOJI" and message.author == bot.user:
        role = discord.utils.get(payload.member.guild.roles, name="NAME_YOUR_ROL")
        if role:
            await payload.member.add_roles(role)

bot.run("YOUR_TOKEN")
            