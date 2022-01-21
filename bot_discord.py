import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
	print('Bot is succesfully authorized! Enjoy!')

@bot.command()
async def are_you_here(ctx):
	author = ctx.message.author
	await ctx.send(f"{author.mention}, ready to serve You!")

@bot.command()
async def info(ctx, arg):
	if arg == 'data':
		a = []
		for i in range(10):
			a.append(str(random.randint(1, 100)))
		await ctx.send(f'The port is {".".join(a)} || All the databases are succesfully connected')
	elif arg == 'main':
		await ctx.send('The bot is awaiting your commands || CMD is online')
	elif arg == 'sys':
		await ctx.send('Line *head = nullptr; / for (string line; getline(cin, line);) / cout << "Lines: " << size(head) << "";')
		await ctx.send('Binary decryption: 01000101 01100001 01110011 01110100 01100101 01110010 01011111 01100101 01100111 01100111')
	else:
		await ctx.send(f'{author.mention}, the command is unavailable! Input ">help" to see the command list!')

@bot.command()
async def slash(ctx, arg, *body):
	author = ctx.message.author
	if arg == 'right':
		output = ''.join(body)
		await ctx.send("'" + output.replace('\\', '/') + "'")
	elif arg == 'left':
		output = ''.join(body)
		await ctx.send("'" + output.replace('/', '\\') + "'")
	else:
		await ctx.send(f'{author.mention}, the command is unavailable! Input ">help" to see the command list!')

@bot.command()
async def html_preset(ctx, arg, frame):
	author = ctx.message.author
	if arg == 'full' and frame == 'no_frame':
		await ctx.send(f'{author.mention}\n<!DOCTYPE html>\n<html lang="">\n<head>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<title></title>\n\t<link rel="stylesheet" type="text/css" href="">\n\t<script src=""></script>\n</head>\n<body>\n\n</body>\n</html>\n')
	elif arg == 'basic' and frame == 'no_frame':
		await ctx.send(f'{author.mention}\n<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<title></title>\n\t<link rel="stylesheet" type="text/css" href="">\n\t<script src=""></script>\n</head>\n<body>\n\n\n</body>\n</html>\n')
	elif arg == 'frame' and frame == 'bootstrap':
		await ctx.send(f"{author.mention}, dont't forget to download the official ZIP-file of Bootstrap (https://getbootstrap.com/) and apply your paths to its files. Enjoy coding :computer:")
		await ctx.send('\n<!DOCTYPE html>\n<html lang="">\n\t<head>\n\t\t<title></title>\n\t\t<meta charset="utf-8">\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t\t<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n\t\t<link rel="stylesheet" href="your css">\n\t\t<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n\t\t<script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>\n\t\t<script src="your code"></script>\n\t</head>\n\t<body>\n\n\n\t\t<script src="https://code.jquery.com/jquery.js"></script>\n\t\t<script src="your directory/bootstrap.min.js "></script>\n\t</body>\n</html>\n')
	elif arg == 'frame' and frame == 'skeleton':
		await ctx.send(f"{author.mention}, don't forget to download the official ZIP-file of Skeleton (http://getskeleton.com/) and apply your paths to its files. Enjoy coding :computer:")
		await ctx.send('\n<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="utf-8">\n\t<title>Your page title here :)</title>\n\t<meta name="description" content="">\n\t<meta name="author" content="">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">\n\t<link rel="stylesheet" href="css/normalize.css">\n\t<link rel="stylesheet" href="css/skeleton.css">\n\t<link rel="icon" type="image/png" href="images/favicon.png">\n</head>\n<body>\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="one-half column" style="margin-top: 25%">\n\t\t\t\t<h4>Basic Page</h4>\n\t\t\t\t<p>This index.html page is a placeholder with the CSS, font and favicon. It is just waiting for you to add some content! If you need some help hit up the <a href="">Skeleton documentation</a>.</p>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</body>\n</html>\n')
	elif arg == 'frame' and frame == 'kube':
		await ctx.send(f"{author.mention}, don't forget to download the official ZIP-file of Kube (https://kube7.imperavi.com/) and apply your paths to its files. Enjoy coding :computer:")
		await ctx.send('<!doctype html>\n<html>\n<head>\n\t<title>Basic Template</title>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="your-folder/css/kube.min.css">\n</head>\n<body>\n\t<h1>Hello, world!</h1>\n\n\n\t<script src="your-folder/js/kube.min.js"></script>\n\t<script>\n\t\t$K.init();\n\t</script>\n</body>\n</html>\n')
	else:
		await ctx.send(f'{author.mention}, the command is unavailable! Input ">help" to see the command list!')

@bot.command()
async def discordpy_preset(ctx, arg):
	author = ctx.message.author
	if arg == 'client':
		await ctx.send(f"{author.mention}, don't forget to install 'Discord.py', 'pip', and 'python' (min. 3.9 version) to work comfortly! Enjoy coding :computer:")
		await ctx.send("import discord\n\nclient = discord.Client()\n\n@client.event\nasync def on_ready():\n\tprint('We have logged in!')\n\n@client.event\nasync def on_message(message):\n\tif message.author == client.user:\n\t\treturn\n\n\tif message.content.startswith('$hello'):\n\t\tawait message.channel.send('Hello!')\n\nclient.run('your token here')\n")
	elif arg == 'bot':
		await ctx.send(f"{author.mention}, don't forget to install 'Discord.py', 'pip', and 'python' (min. 3.9 version) to work comfortly! Enjoy coding :computer:")
		await ctx.send("import discord\nfrom discord.ext import commands\n\nbot = commands.Bot(command_prefix='>')\n\n@bot.command()\nasync def ping(ctx):\n\tawait ctx.send('pong')\n\nbot.run('token')\n")
	else:
		await ctx.send(f'{author.mention}, the command is unavailable! Input ">help" to see the command list!')
		
@bot.command()
async def css_preset(ctx, arg):
	author = ctx.message.author
	if arg == 'media':
		await ctx.send("\n/***** Large Devices Only ********/\n@media (min-width: 1200px) {\n\n}\n\n/***** Medium Devices Only ********/\n@media (min-width: 992px) and (max-width: 1199px) {\n\n}\n\n/***** Small Devices Only ********/\n@media (min-width: 768px) and (max-width: 991px) {\n\n}\n/***** Extra Small Devices Only ********/\n@media (max-width: 767px) {\n\n}\n")
	else:
		await ctx.send(f'{author.mention}, the command is unavailable! Input ">help" to see the command list!')

@bot.command()
async def discordjs_preset(ctx):
	author = ctx.message.author
	await ctx.send(f"{author.mention}, don't forget to download required files (you can read them here: https://discord.js.org/#/docs/discord.js/stable/general/welcome) to work comfortly! Enjoy coding :computer:")
	await ctx.send("const { Client, Intents } = require('discord.js');\nconst client = new Client({ intents: [Intents.FLAGS.GUILDS] });\n\nclient.on('ready', () => {\n\tconsole.log(`Logged in as ${client.user.tag}!`);\n});\n\nclient.on('interactionCreate', async interaction => {\n\tif (!interaction.isCommand()) return;\n\n\tif (interaction.commandName === 'ping') {\n\t\tawait interaction.reply('Pong!');\n\t}\n});\n\nclient.login('token');\n")

@bot.command()
async def intro(ctx):
	author = ctx.message.author
	await ctx.send(f"{author.mention}, Hi! My name is IT-Helper and I'm made by a beginner programmer named Michael Marphin to make other programmers' life better and easier.\nI can really save your time because you don't need to write your presets anymore. Now I'm giving it to you!\n\nP.S\nIt's my demo version, so if you want me to go into full flow you'll need to purchase a licence\n\n\nCopyright MS Entertaiment 2022\nBeta Version v1.0\n")

bot.run('OTMwMjAwNTc2MTg3MzIyNDI4.Ydyayw.g7v6IafO02URiQCgRhWS4eRF0AY')

'''
const { Client, Intents } = require('discord.js');\nconst client = new Client({ intents: [Intents.FLAGS.GUILDS] });\n\nclient.on('ready', () => {\n\tconsole.log(`Logged in as ${client.user.tag}!`);\n});\n\nclient.on('interactionCreate', async interaction => {\n\tif (!interaction.isCommand()) return;\n\n\tif (interaction.commandName === 'ping') {\n\t\tawait interaction.reply('Pong!');\n\t}\n});\n\nclient.login('token');\n
'''
