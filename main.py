from telethon import TelegramClient, events
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    api_id = '(api_id)'  # гайд как получить api_id https://tlgrm.ru/docs/api/obtaining_api_id
    api_hash = '(api_hash)'  # так же в личном кабинете будет api_hash
    client = TelegramClient('anon', api_id, api_hash)

    @client.on(events.NewMessage(chats='(название канала)')) # введите название канала из телеграма куда пользователь/бот зашёл
    async def my_event_handler(event):
        print(event)
        channel = bot.get_channel((айди)) #вставьте айди канала из дискорда куда будут отправляться сообщения (вводить айди без скобочек)
        if hasattr(event.media, 'poll'):
            embed = discord.Embed(title="Новый опрос!", description=event.media.poll.question)
            embed.set_author(name="(название)", icon_url="(ссылка на аватарку)")  # вставьте название канала и ссылка на аватрку канала или другую картинку
            for text in event.media.poll.answers:
                embed.add_field(name="Вариант ответа", value=text.text, inline=True)
            return await channel.send(embed=embed)
        if not hasattr(event.media, 'poll'):
            embed = discord.Embed(title="Новый пост!", description=event.raw_text)
            embed.set_author(name="(название)", icon_url="(ссылка на аватарку)")  # вставьте название канала и ссылка на аватрку канала или другую картинку
            if event.media != None:
                await event.download_media(file="(директория)") # файл будет скачиваться в папку, укажите директорию
                path = "(директория, не опять а снова)" # укажите ту же самую директорию сверху
                files = os.listdir(path)
                paths = [os.path.join(path, basename) for basename in files]
                last_file = max(paths, key=os.path.getctime)[len(path) + 1:]
                l = f"{path}/{last_file}"
                file = discord.File(l, filename="image.png")
                embed.set_image(url="attachment://image.png")
                await channel.send(file=file, embed=embed)
            #    os.remove(l) # уберите # в начале если хотите чтобы картинки потом удалялись
                return
            await channel.send(embed=embed)
    await client.start()
    await client.run_until_disconnected()


bot.run('(токен бота)') # гайд как получить токен бота и как добавить бота на сервер https://black-minecraft.com/tutorial/2141-kak-poluchit-token-bota-discord.html

