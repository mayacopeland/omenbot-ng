import discord
import json
import commands
import util

bot_config = None
runtimes = None
client = None

class config:
    def __init__(self, t, p, bdr, sar, rc, rr, pn):
        self.token = t
        self.prefix = p
        self.bot_dev_role = bdr
        self.server_admin_role = sar
        self.reminder_channel = rc
        self.reminder_role = rr
        self.presence_name = pn

class bot_user(discord.Client):
    async def on_ready(self):
        if bot_config.presence_name != '':
            await self.change_presence(activity=discord.Game(bot_config.presence_name))
        print(f'Now logged in as {self.user}')
    
    async def on_message(self, message):
        if message.content.startswith(bot_config.prefix):
            command = message.content[1:].split(' ')
            args = command[1:]
            sender_allowed_elevated_commands = bot_config.bot_dev_role.lower() in [r.name.lower() for r in message.author.roles] or bot_config.server_admin_role.lower() in [r.name.lower() for r in message.author.roles]
            if command[0] == 'runtimes':
                await message.channel.send(commands.get_runtimes.get_runtimes_api())
            elif command[0] == "help":
                await message.channel.send(commands.get_help.send_help())
            elif command[0] == "run":
                await message.channel.send(commands.run_code.run_code(args, runtimes))
            elif command[0] == "inspiration" or command[0] == "inspire" or command[0] == "motivation":
                await message.channel.send(commands.inspiration.inspire())
            elif command[0] == "roll":
                await message.channel.send(commands.roll.roll(message.author, args))
            elif command[0] == "warn" and sender_allowed_elevated_commands:
                await message.channel.send(commands.alerts.alert(args))
                await message.delete()
            elif command[0] == "remind" and sender_allowed_elevated_commands:
                if '"' in message.content and "'" in message.content:
                    await message.channel.send("Please don't mix both ' and \" I'm fragile.")
                    return

                if "'" in message.content:
                    args = message.content[1:].split("'")[1:]
                else:
                    args = message.content[1:].split('"')[1:]
                chan = discord.utils.get(message.guild.channels, name=bot_config.reminder_channel)
                await message.channel.send(await commands.remind.remind_users(chan, bot_config.reminder_role, args[0], args[2], args[4]))
            elif command[0] == "update_presence" and sender_allowed_elevated_commands:
                await commands.update_presence.update_presence(self, " ".join(args))
            elif command[0] == "join":
                if not message.author.voice:
                    await message.channel.send("You aren't currently in a voice channel dummy")
                else:
                    await message.author.voice.channel.connect()
            elif command[0] == "leave":
                voice_channel = message.guild.voice_client
                if voice_channel.is_connected():
                    await voice_channel.disconnect()
                else:
                    await message.channel.send("I'm no't currently in a voice channel dummy")
            elif command[0] == "p":
                await message.channel.send("Music bot features aren't re-implemented, sorry")
            else:
                await message.channel.send("Unknown command.")
                print(f'Unhandled command: {command[0]} - args: {args}')
        
        if 'owo' in message.content:
            await message.channel.send('whats this?')



def reminder_loop():
    print('remind')


def main():
    global bot_config
    global runtimes
    global client

    print('Omenbot V2')
    print('Parsing Configuration')
    config_file = open('config.json', 'r')
    c = json.load(config_file)
    bot_config = config(c['token'], c['prefix'], c['bot_dev_role'], c['admin_role'], c['reminder_channel_name'], c['reminder_role'], c['playing_status'])
    print('Getting available command runtimes')
    runtimes = util.get_runtimes.create_classes()
    discord_client = bot_user()
    discord_client.run(bot_config.token)
    client = discord_client
    

if __name__ == "__main__":
    main()
