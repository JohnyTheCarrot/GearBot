import asyncio

import discord
from discord.ext import commands

from Util import GearbotLogging, Emoji

yesID = 465582004260569088
noID = 465582003874693130
yes = None
no = None




async def confirm(ctx: commands.Context, text, timeout=30, on_yes=None, on_no=None, delete=True):
    yes = Emoji.get_emoji("YES")
    no = Emoji.get_emoji("NO")
    message: discord.Message = await ctx.send(text)
    await message.add_reaction(yes)
    await message.add_reaction(no)

    def check(reaction: discord.Reaction, user):
        return user == ctx.message.author and reaction.emoji in (yes, no) and reaction.message.id == message.id

    try:
        reaction, user = await ctx.bot.wait_for('reaction_add', timeout=timeout, check=check)
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send(f"I got no answer within {timeout} seconds.. Aborting.")
        return
    GearbotLogging.info(f"CONFIRMATOR RESPONCE RECEIVED:\nreaction: {reaction}\nemoji: {reaction.emoji}\non_yes: {on_yes}\non_no: {on_no}")
    if reaction.emoji == yes and on_yes is not None:
        if delete:
            try:
                await message.delete()
            except discord.Forbidden:
                pass
        await on_yes()
    elif reaction.emoji == no:
        if delete:
            try:
                await message.delete()
            except discord.Forbidden:
                pass
        if on_no is not None:
            await on_no()
        else:
            await GearbotLogging.send_to(ctx, "NO", "command_canceled")
