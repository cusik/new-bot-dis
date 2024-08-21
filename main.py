import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
	print(f"Bot {bot.user} is ready to work!")

@bot.event
async def on_member_join(member):
	role = await disnake.utils.get(guild.id=member.guild.id,role id=)
	channel = bot.get_channel() member.guild.system_channel
    embed = disnake.Embed(
		title="Новый читатель!",
		description=f"{member.name}#{member.discriminator}",
		color=0xffffff
	)
    
	await member.add_roles(role)
    await channel.send(embed=embed)




bot.run("")

