import json
import discord

async def update_presence(client, presence_name):
    config = open('config.json', 'r')
    config_parsed = json.load(config)
    config.close()
    config = open('config.json', 'w')
    if presence_name != "":
        config_parsed['playing_status'] = presence_name
        await client.change_presence(activity=discord.Game(presence_name))
        config.write(json.dumps(config_parsed))
    return 'updated the client presence'
    

