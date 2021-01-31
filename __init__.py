from opsdroid.matchers import match_event
from opsdroid.events import Message


@match_event(Message)
async def echo(opsdroid, config, message):
    conn = opsdroid.get_connector("matrix")
    nick, mxid = conn.nick, conn.mxid
    nick = nick if nick else "no nick, don't match this"
    if nick in message.text:
        newtext = message.text.split(nick)[1].strip("</a>").strip(":").strip()
        await message.respond(newtext)
    elif mxid in message.text:
        newtext = message.text.split(mxid)[1].strip("</a>").strip(":").strip()
        await message.respond(newtext)
