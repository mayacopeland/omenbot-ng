import discord
import json
import commands
import util

bot_config = None
runtimes = None

class config:
    def __init__(self, t, p):
        self.token = t
        self.prefix = p

class bot_user(discord.Client):
    async def on_ready(self):
        print(f'Now logged in as {self.user}')
    async def on_message(self, message):
        if message.content.startswith(bot_config.prefix):
            command = message.content[1:].split(' ')
            args = command[1:]
            if command[0] == 'runtimes':
                await message.channel.send(commands.get_runtimes.get_runtimes_api())
            elif command[0] == "help":
                await message.channel.send(commands.get_help.send_help())
            elif command[0] == "run":
                await message.channel.send(commands.run_code.run_code(args, runtimes))
            else:
                print(f'Unhandled command: {command[0]} - args: {args}')



def reminder_loop():
    print('remind')


def main():
    global bot_config
    global runtimes

    print('Omenbot V2')
    print('Parsing Configuration')
    config_file = open('config.json', 'r')
    c = json.load(config_file)
    bot_config = config(c['token'], c['prefix'])
    print('Getting available command runtimes')
    runtimes = util.get_runtimes.create_classes()
    discord_client = bot_user()
    discord_client.run(bot_config.token)

if __name__ == "__main__":
    main()
