from opsdroid.matchers import match_event
from opsdroid.events import Message


@match_event(Message)
async def echo(opsdroid, config, message):
    mxid = opsdroid.get_connector("matrix").mxid
    if mxid in message.text:
        newtext = message.text.split(":")[1]
        await message.respond(newtext)
