import os

import discord
from discord import app_commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

embed = discord.Embed(
    title="Title",
    description="description",
    color=0x1e1e1e
)
embed.add_field(name="Name `highlighted`:",
                value="value of Field"
                )

tree = app_commands.CommandTree(client)


@tree.command(name="cmd", description="My first application Command", guild=discord.Object(id=928336424514752534))
async def first_command(interaction):
    await interaction.response.send_message("Reacted 2 Command")


@client.event
async def on_ready():
    print(client.guilds)
    await tree.sync(guild=discord.Object(id=928336424514752534))
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/'):
        prompt = message.content[1:]
        print(message.guild.id)
        if prompt.startswith('hello'):
            await message.channel.send("Hello!")
        if prompt.startswith('embed'):
            await message.channel.send(embed=embed)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client.run(token)
