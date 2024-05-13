import json
import os
from dotenv import load_dotenv
from dyn_funcs import *
from nextcord import (
    Interaction,
    Intents,
)

from nextcord.ext.commands import Bot
load_dotenv('./bot.env')
_TOKEN = os.getenv('BOT_TOKEN')

intents = Intents.default()
intents.message_content = True

bot = Bot(default_guild_ids=[854423652262215710], intents=intents)


@bot.slash_command(description="Adds a custom command that will be loaded on next bot startup.")
async def add_command(ctx: Interaction, name: str, response: str):
    key = str(ctx.guild.id)

    with (open('funcs.json', 'r') as funcs_file):
        func_dict: dict[str: list[dict[str, str]]] = json.load(funcs_file)

    func_dict.setdefault(key, [])
    func_dict[key].append({"name": name, "response": response})

    with open('funcs.json', 'w') as funcs_file:
        json.dump(func_dict, funcs_file, indent=2)

    await ctx.send(f"Added command {name} with response {response}", ephemeral=True)


@bot.slash_command(description="Restarts the bot to reload slash commands")
async def restart(ctx: Interaction):
    await ctx.send("Restarting.", ephemeral=True)
    await ctx.client.s
    await ctx.client.start(_TOKEN)
    await ctx.send("Restarted.", ephemeral=True)


if __name__ == '__main__':
    with open('funcs.json', 'r') as f:
        funcs = json.load(f)

    for server in funcs:
        for func in funcs[server]:
            load_dynamic_function(bot, int(server), func['name'], func['response'])

    bot.run(_TOKEN)
