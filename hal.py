import discord


prefix = ">"
client = discord.Client()


@client.event
async def on_ready():
    print(f' Name: {client.user}')
    print(f'   Id: {client.user.id}')
    print(f'Email: {client.user.email}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(prefix):
        command = message.content[len(prefix):]
        if (command == "quit"):
            await message.channel.send(f"{client.user} is leaving...")
            await client.close()
        else:
            await message.channel.send(execute(message.content))
    if message.content == "open the pod bay doors":
        msg = f"I'm afraid i can not do that @{message.author}..."
        await message.channel.send(msg)


def execute(command):
    print("Executing: " + command)
    if command == "ping":
        return "pong"
    else:
        return command + " is not a command..."


def archive(image):
    pass


def main():
    client.run(input("Token: "))


if __name__ == '__main__':
    main()
