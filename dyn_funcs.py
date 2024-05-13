from typing import Callable

from nextcord import Interaction
from nextcord.ext.commands import Bot


class FunctionExistsError(Exception):
    pass


def load_dynamic_function(bot: Bot, server: int, name: str, response: str) -> Callable:
    print(bot.add_all_application_commands(), bot.get_all_application_commands())

    @bot.slash_command(name=name, description="Custom command added by users.", guild_ids=[server])
    async def dyn_func(ctx: Interaction, func_input: str):
        await ctx.send(response.format(func_input))

    return dyn_func
