from opsdroid.matchers import match_event
from opsdroid.events import Message


@match_event(Message)
async def echo(opsdroid, config, message):
    conn = opsdroid.get_connector("matrix")
    nick, mxid = conn.nick, conn.mxid
    if nick in message.text or mxid in message.text:
        newtext = message.text.split(":")[1].strip()
        await message.respond(newtext)
