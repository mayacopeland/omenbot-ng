import json
import discord

async def update_reply(reply, botfig):
    config = open('config.json', 'r')
    config_parsed = json.load(config)
    config.close()
    config = open('config.json', 'w')
    if reply != "" and "add_bot_reply" not in reply:
        config_parsed['funny_replies'].append(reply)
        botfig.funny_replies.append(reply)
        config.write(json.dumps(config_parsed))
        return 'added reply.'
    else:
        return ':person_facepalming:'
    

