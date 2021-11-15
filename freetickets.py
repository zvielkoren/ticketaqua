import discord, discord.utils
from discord_components import DiscordComponents, Button, ButtonStyle
from discord.ext import commands
from discord.utils import get
from ez import *

intents = discord.Intents().all()
prefix="-"

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help") #deletes the default help command
DiscordComponents(client)

Guild=client.get_guild(903288271277260900)

BotToken="ODY3NzQ2MDU4NTMxNTA0MTM4.YPllfg.SyWmPUWkpyRo3VeptdQD3wMm48Y"
TicketEmbedButtonName="פתיחת טיקט"#after the message of the open tickets has been sent, this line can be deleted
TicketEmbedButtonEmoji="🎫"#after the message of the open tickets has been sent, this line can be deleted
TicketEmbedTitle="פתיחת טיקט חדש"#after the message of the open tickets has been sent, this line can be deleted
TicketEmbedDescription="לא לפתוח סתם טיקטים \n !אי אפשר לפתוח יותר מטיקט אחד "#after the message of the open tickets has been sent, this line can be deleted

@client.event
async def on_ready():
    print(f"{client.user} IS ONLINE NOW")


@client.command()#after the message of the open tickets has been sent, this line can be deleted
async def send_ticket_command(ctx):#after the message of the open tickets has been sent, this line can be deleted
    channel=client.get_channel(903666092751331408)
    embed = discord.Embed(title=TicketEmbedTitle,description=TicketEmbedDescription, color=discord.Colour.blue())#after the message of the open tickets has been sent, this line can be deleted
    await channel.send(embed=embed, components=[Button(label=TicketEmbedButtonName, emoji=TicketEmbedButtonEmoji, style=ButtonStyle.red)])#after the message of the open tickets has been sent, this line can be deleted


@client.event
async def on_button_click(button):
    msg = button.message
    user = get(client.get_all_members(), id=button.author.id)
    guild = client.get_guild(button.guild_id)
    Staff = get(guild.roles, id=903288271294046219)
    if button.component.label==TicketEmbedButtonName:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            user:discord.PermissionOverwrite(view_channel=True, read_messages=True, send_messages=True,attach_files=True),
            Staff:discord.PermissionOverwrite(view_channel=True, read_messages=True, send_messages=True,attach_files=True)
            }
        category = discord.utils.get(guild.categories, id=903663609538809926)
        if not varexists(f"{user.id}ticket", "tickets"):
            ticket = await guild.create_text_channel(f"ticket-{user.name}", category=category, topic=f"{user.id}",overwrites=overwrites)
            setvar(f"{user.id}ticket", f"{ticket.id}", "tickets")
            setvar(f"{ticket.id}creator", f"{user.id}", "tickets")
            embed = discord.Embed(title=f"{guild.name} TICKETS",description=f"הצוות יגיע בקרוב.\n כדי לסגור את הטיקט, כתבו ``-close``",color=discord.Colour.blue())
            embed.set_author(name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
            await ticket.send(embed=embed)
            await ticket.send(f"{Staff.mention}", delete_after=1)
            
    
@client.event
async def on_guild_channel_delete(channel):
    if varexists(f"{channel.id}creator", "tickets"):
        user=getvar(f"{channel.id}creator", "tickets")
        deletevar(f"{channel.id}creator", "tickets")
        deletevar(f"{user.id}ticket", "tickets")

@client.command()
async def close(ctx):
    if varexists(f"{ctx.channel.id}creator", "tickets"):
        embed = discord.Embed(description=f"הטיקט ייסגר בקרוב", colour=discord.Colour.dark_red())
        await ctx.reply(embed=embed)
        user = get(client.get_all_members(), id=int(getvar(f"{ctx.channel.id}creator", "tickets")))
        messages = await ctx.channel.history(limit=150000, oldest_first=True).flatten()
        
        await ctx.channel.delete()
        deletevar(f"{user.id}ticket", "tickets")
        deletevar(f"{ctx.channel.id}creator", "tickets")

@client.event
async def on_message(message):
    await client.process_commands(message)

client.run(BotToken)
