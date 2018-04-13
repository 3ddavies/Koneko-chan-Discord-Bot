from __future__ import unicode_literals
import os
import sys
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import shlex
from discord import utils
from discord.object import Object
from discord.enums import ChannelType
from discord.voice_client import VoiceClient
from discord.ext.commands.bot import _get_variable
from discord import message
import logging
import datetime
import re
from pybooru import Danbooru
from random import randint
import urllib.request
from random import *
import shutil
from song import *

"""
Koneko-Chan Discord Bot
Created By: Gabriel Peressini
Protected by CC BY-SA 4.0

https://creativecommons.org/licenses/by-sa/4.0/
"""




admins =['Jupiter and Mars#9960','Cyro#6377','⛧AirStrikerAlex⛧#8618']
danclient = Danbooru('danbooru', username='Put your Danbooru username here', api_key='Put your Danbooru api key here')
tags = danclient.tag_list(order='date')

"""
artists = client.artist_list('ma')
for artist in artists:
    print("Name: {0}".format(artist['name']))
"""

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
usedimgs = []
"""

class myClient(discord.client):

	@asyncio.coroutine
	def on_message(self, message):	
		yield from self.send_message(message.channel, 'Hello World!')

"""

koneko = Bot(description="A Discord Bot!", command_prefix="!", pm_help = True)
#koneko.remove_command('help')

@koneko.event
async def on_ready():
	print('Logged in as '+koneko.user.name+' (ID:'+koneko.user.id+') | Connected to '+str(len(koneko.servers))+' servers | Connected to '+str(len(set(koneko.get_all_members())))+' users')
	print('Discord.py Version: {} | Python Ver: {}'.format(discord.__version__, platform.python_version()))
	print('Invite link {}:'.format(koneko.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(koneko.user.id))
	return await koneko.change_presence(game=discord.Game(name='Hand Delivering Hentai'))
	
@koneko.event
async def on_message(message):
		await koneko.process_commands(message)
 
@koneko.event
async def on_error(self, event, *args, **kwargs):
	ex_type, ex, stack = sys.exc_info()

	if ex_type == exceptions.HelpfulError:
		print("Exception in", event)
		print(ex.message)

		await asyncio.sleep(2)
		await self.logout()

	elif issubclass(ex_type, exceptions.Signal):
		self.exit_signal = ex_type
		await self.logout()

	else:
		traceback.print_exc()


@koneko.command()
async def ping(*args):
	await koneko.say(":ping_pong: Pong!")
	
@koneko.command(pass_context=True)
async def logout(ctx,*args):
	if (str(ctx.message.author) in admins):
		await koneko.say("See ya later, Alligator!")
		await asyncio.sleep(1)
		await koneko.logout()
	else:
		await koneko.say("Please, "+ctx.message.author.mention+", don't touch me there!")

@koneko.command(pass_context=True)
async def ss(ctx,*args):
	"""
	Sets the ingame status of the bot.
	!ss With Fire
	"""
	st = ' '.join(args)
	return await koneko.change_presence(game=discord.Game(name=st))

@koneko.command(pass_context=True)
async def climsg(ctx,*args):
	if (str(ctx.message.author) in admins):
		dsmid=id
		print(dsmid)
		climsgv = input("Cmd: ")
		await koneko.say(climsgv)
		#pass_context=True
	else:
		await koneko.say("I'm sorry "+ctx.message.author.mention+", but this command is not currently, and may not ever be, available to the public.")

@koneko.command(pass_context=True)
async def anako(ctx,*args):
	if (str(ctx.message.author) in admins):
		await koneko.say("Awaiting instruction")
		while True:
			xwts = input("Say: ")
			if (xwts == '/halt/'):
				break
			if (xwts == ''):
				print("Error: Can not send empty message.")
			else:
				await koneko.say(xwts)
	else:
		await koneko.say("STRANGER DANGER!!!")

@koneko.command(pass_context=True)
async def stsca(ctx,*args):
	if (str(ctx.message.author) in admins):
		nescargmt = input("New esc arg: ")
		f = open('escchar.txt','w')
		f.write(nescargmt)
		f.close()
		print("New escape argument successfully set to: "+nescargmt)
		await koneko.say("Change Sucessfull. Change will come into effect upon next restart.")
	else:
		await koneko.say("Do you even know what this does, "+ctx.message.author.mention+"?")

@koneko.command(pass_context=True)
async def restart(ctx,*args):
	
	"""
	Restarts the bot.
	!restart
	"""
	if (str(ctx.message.author) in admins):

		await koneko.say("Restarting!")
		await koneko.logout()
		os.system('run.bat')
		exit()
	else:
		await koneko.say("You can't do this "+ctx.message.author.mention+"!")

@koneko.command(pass_context=True)
async def omgmt(ctx, message: discord.Message = None):
	if (str(ctx.message.author) in admins):
		if message is None:
			message = ctx.message.id
			channel = ctx.message.channel
			print(message)
			print(channel)

		await koneko.say(message)
		await koneko.say(koneko.get_message(channel,str(message)))
		print(koneko.get_message(channel,str(message)))
		asyncio.sleep(5)
		await koneko.delete_message(ctx.message.id)
	else:
		await koneko.say("Only senpai can touch me there "+ctx.message.author.mention+".")

@koneko.command()
async def pwd(*args):
	"""
	Prints the present working directory in chat.
	!pwd
	"""
	await koneko.say(os.getcwd())

@koneko.command()

async def ls(*args):
	"""
	Lists the contents of the present working directory.
	!ls
	"""
	sicwd='\n'.join(os.listdir(os.getcwd()))
	await koneko.say("Directory of "+os.getcwd())
	await koneko.say(sicwd)


@koneko.command()

async def cd(*args):
	"""
	Changes the present working directory.
	!restart
	"""
	try:
		os.chdir(*args)
		asyncio.sleep(1)
		await koneko.say("Current working directory has been changed to "+os.getcwd())
	except TypeError:
		await koneko.say("Invalid Directory")
@koneko.command()

async def ostimes(*args):
	await koneko.say(os.times())


@koneko.command()
async def time(*args):
	"""
	Prints the time in chat.
	!time
	"""
	cdat = datetime.datetime.now()
	await koneko.say("The time is "+str(cdat.hour)+":"+str(cdat.minute)+":"+str(cdat.second)+" and the date is "+str(cdat.day)+"/"+str(cdat.month)+"/"+str(cdat.year))

@koneko.command()
async def gab(*args):
	pyalmem=str(sys.getallocatedblocks())
	print(sys.getallocatedblocks())
	await koneko.say(pyalmem)

@koneko.command(pass_context=True)
async def vomit(ctx,*args):
	if (str(ctx.message.author) in admins):
		testvomitstring = 'Thisisaverylongstring!'
		vomitf = open('discord.log','r')
		vomitstring=vomitf.read()
		print(re.findall(r'.{1,2000}',vomitstring,re.DOTALL))
		vomitarray = re.findall(r'.{1,2000}',vomitstring,re.DOTALL)
		vomitlength = len(vomitarray)
		print(vomitlength)
		vomititr = 0
		while (vomitlength >= vomititr):
			await koneko.say(vomitarray[vomititr])
			vomititr+=1
	else:
		await koneko.say("Sorry "+ctx.message.author.mention+", I only vomit for senpai.:wink:")
		
@koneko.command(pass_context=True)
async def hentaidan(ctx,*args):
	if (str(ctx.message.author) in admins):
		await koneko.say("http://danbooru.donmai.us/posts/"+str(randint(1, 3000000)))
	else:
		await koneko.say("I'm sorry "+ctx.message.author.mention+", but this command is not currently, and may not ever be, available to the public.")

@koneko.command(pass_context=True)
async def hentaigel(ctx,*args):
	if (str(ctx.message.author) in admins):
		await koneko.say("https://gelbooru.com/index.php?page=post&s=view&id="+str(randint(1,4079175)))
	else:
		await koneko.say("I'm sorry "+ctx.message.author.mention+", but this command is not currently, and may not ever be, available to the public.")

@koneko.command(pass_context=True)
async def hentai(ctx,*args):
	"""
	( ͡° ͜ʖ ͡°)
	"""
	whatpage=1
	hentaif = open('hchanids.txt','r')
	ahca = hentaif.read()
	hentaif.close()
	naca = re.findall(r'.{1,18}',ahca,re.DOTALL)
	if (str(ctx.message.channel.id) in naca):#checks if the channel is allowed to have hentai posted in it.
		urlarr=[]
		iserr=0#tracks errors
		henstr=''#henstr stands for Hentai String
		lnkitr=0#lnkitr stands for Link Iteration
		stupidvar=5#helps seperate the urls into chunks of 5
		tstr = list(args)
		tstr = tstr[1:len(tstr)]
		try:
			tiaziion = int(args[0])
		except ValueError:
			await koneko.say("Oopsie! The first argument should be an integer (Number) but it looks like you put a string. If you are confused, try !help hentai :wink:")
		
		try:
			tiaoe = args[1]
		except IndexError:
			await koneko.say("Woah there, bud. You gotta help me out a bit here. :stuck_out_tongue_winking_eye:\n```\nUsage: !hentai NumberOfImages Tags Tags Tags (you get the idea)\n```")
			iserr = 1

		if(iserr==0):
			ham=int(args[0])#HAM stands for Hentai Ammount
			posts = danclient.post_list(tags=tstr, limit=ham)
			try:
				for post in posts:
					ftst = post['file_url']
					firsttwentysix = ftst[0:26]
					if (firsttwentysix == 'https://hijiribe.donmai.us'):
						ftst = ftst[26:len(ftst)]
						urlarr.append("http://danbooru.donmai.us"+ftst)
						usedimgs.append(post['file_url'])
					else:
						urlarr.append("http://danbooru.donmai.us"+post['file_url'])
						usedimgs.append(post['file_url'])
				print(usedimgs)
			except KeyError:
				await koneko.say("Sorry, "+ctx.message.author.mention+", but I couldn't find "+str(ham)+" images with the tags: "+str(tstr)+" Here's what I did find, though (If I don't post anything then I didn't find anything.) :o")
			try:
				while (ham > lnkitr):
					if (lnkitr > stupidvar):
						await koneko.say(henstr)
						henstr=''
						stupidvar+=5
					else:
						henstr+=urlarr[lnkitr]+"\n"
						lnkitr = lnkitr +1
				await koneko.say(henstr)
			except IndexError:
				await koneko.say("S-sorry m-mister. I-i... The n-numbers... were t-to big.:flushed:\n```\nUsage: !hentai NumberOfImages Tags Tags Tags (you get the idea)\n```")
	else:
		await koneko.say("This channel is not set up for this kind of content. If it should be, please use !setchan")


		
@koneko.command()
async def listtags(*args):
	dantaglist = []
	for tag in tags:
		dantaglist.append(tag['name'])
		print(dantaglist)
	await koneko.say(dantaglist)
@koneko.command(pass_context=True)
async def arclog(ctx,*args):
	if (str(ctx.message.author) in admins):
		cdat = datetime.datetime.now()
		arclogf=open("discord.log",'r')
		thl = arclogf.read()
		arclogf.close()
		arclogft = open(str(cdat.hour)+"."+str(cdat.minute)+"."+str(cdat.second)+"_"+str(cdat.day)+"."+str(cdat.month)+"."+str(cdat.year)+'.log','w')
		arclogft.write(thl)
		arclogft.close()
		await koneko.say("Log Cleared!")
		await koneko.logout()
		os.system('rmlgrs.bat')
		exit()
	else:
		await koneko.say("Fuck off "+ctx.message.author.mention+"!")

@koneko.command()
async def ppap(*args):
	await koneko.say("Just for you, Gil:")
	await koneko.say("https://www.youtube.com/watch?v=0E00Zuayv9Q")

@koneko.command()
async def credits(*args):
	"""
	Displays credits.
	"""
	myid = '<@266286756893032451>'
	cyroid = '<@137974023979139073>'
	await koneko.say("Programmed by Gabe "+myid)


@koneko.command(pass_context=True)
async def getauth(ctx):
	if (str(ctx.message.author) in admins):
		await koneko.say(ctx.message.author)
	else:
		await koneko.say("I'm sorry "+ctx.message.author.mention+", but this command is not currently, and may not ever be, available to the public.")

@koneko.command(pass_context=True)
async def setchan(ctx):
	if (str(ctx.message.author) in admins):
		f = open('hchanids.txt','r')
		allchans = f.read()
		nac = re.findall(r'.{1,18}',allchans,re.DOTALL)
		print(nac)
		f.close()
		f = open('hchanids.txt','a')
		f.write(str(ctx.message.channel.id))
		f.close()
		await koneko.say("Channel set.")
	else:
		await koneko.say("How about no.")


@koneko.command()
async def stats():
	"""
	Displays stats.
	"""
	await koneko.say("I'm currently enjoying the privilege of being connected to "+str(len(koneko.servers))+" servers and I'm currently serving "+str(len(set(koneko.get_all_members())))+" lovely users!")
	await koneko.say(":kissing_heart:")

@koneko.command(pass_context=True)
async def gif(ctx):
	with open('dancingmiku2.gif', 'rb') as f:
		await koneko.send_file(ctx.message.channel, f)


koneko.run('Put your bot token here')
