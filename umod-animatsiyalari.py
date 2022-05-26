# ▀█▀ █▀▀ █▀▄▀█ █░█ █▀█
# ░█░ ██▄ █░▀░█ █▄█ █▀▄
# ═══════════════════════
# █▀▀ █▀█ █▄▀ █ █▄░█ █▀█ █░█
# ██▄ █▀▄ █░█ █ █░▀█ █▄█ ▀▄▀
# ═════════════════════════════
# meta developer: @netuzb
# meta channel: @umodules

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
from asyncio import sleep
import random

__version__ = (2, 1, 43)

def register(cb):
	cb(MillatlarMod())
	
class MillatlarMod(loader.Module):
	"""Millatlar aro qisqartma nomlar"""

	strings = {"name": "Millatlar",}

	async def tadjikcmd(self, message):
		"""tadjik style"""
		
		umd = """
╔══╗──╔╗╔╦╗
╚╗╔╩╗╔╝╠╬╣╠╗
─║║╬╚╣╬╠╣║═╣
─╚╩══╩╦╝╠╩╩╝
──────╚═╝"""
		await message.edit(umd)
		return
	
	async def tadjik2cmd(self, message):
		"""tadjik style 2"""
		
		umd = """
╔════╗───╔╗─╔╗
║╔╗╔╗║───║╠╗║║
╚╝║║╠╩═╦═╝╠╬╣║╔╗
──║║║╔╗║╔╗╠╬╣╚╝╝
──║║║╔╗║╚╝║║║╔╗╗
──╚╝╚╝╚╩══╣╠╩╝╚╝
─────────╔╝║
─────────╚═╝"""
		await message.edit(umd)
		return

	async def uzbekcmd(self, message):
		"""uzbek style"""
		
		umd = """
╔╦╦═╦╗──╔╗
║║╠═║╚╦═╣╠╗
║║║═╣╬║╩╣═╣
╚═╩═╩═╩═╩╩╝"""
		await message.edit(umd)
		return
	
	async def uzbek2cmd(self, message):
		"""uzbek style 2"""
		
		umd = """
╔╗─╔╗───╔╗────╔╗
║║─║║───║║────║║
║║─║╠═══╣╚═╦══╣║╔╗
║║─║╠══║║╔╗║║═╣╚╝╝
║╚═╝║║══╣╚╝║║═╣╔╗╗
╚═══╩═══╩══╩══╩╝╚╝"""
		await message.edit(umd)
		return

	async def russcmd(self, message):
		"""russ style"""
		
		umd = """
╔═╗─╔═╦═╗
║╬╠╦╣═╣═╣
║╗╣║╠═╠═║
╚╩╩═╩═╩═╝"""
		await message.edit(umd)
		return
	
	async def russ2cmd(self, message):
		"""russ style 2"""
		
		umd = """
╔═══╗
║╔═╗║
║╚═╝╠╗╔╦══╦══╗
║╔╗╔╣║║║══╣══╣
║║║╚╣╚╝╠══╠══║
╚╝╚═╩══╩══╩══╝"""
		await message.edit(umd)
		return

	async def usacmd(self, message):
		"""usa style"""
		
		umd = """
╔╦╦══╦══╗
║║║══╣╔╗║
║║╠══║╠╣║
╚═╩══╩╝╚╝"""
		await message.edit(umd)
		return
	
	async def usa2cmd(self, message):
		"""usa style 2"""
		
		umd = """
╔╗─╔╦═══╦═══╗
║║─║║╔═╗║╔═╗║
║║─║║╚══╣║─║║
║║─║╠══╗║╚═╝║
║╚═╝║╚═╝║╔═╗║
╚═══╩═══╩╝─╚╝"""
		await message.edit(umd)
		return

	async def kgzcmd(self, message):
		"""kgz style"""
		
		umd = """
╔╦╗─╔═╗
║╔╬═╬═║
║╚╣╬║═╣
╚╩╬╗╠═╝
──╚═╝"""
		await message.edit(umd)
		return
	
	async def kgz2cmd(self, message):
		"""kgz style 2"""
		
		umd = """
╔╗╔═╗
║║║╔╝
║╚╝╝╔══╦═══╗
║╔╗║║╔╗╠══║║
║║║╚╣╚╝║║══╣
╚╝╚═╩═╗╠═══╝
────╔═╝║
────╚══╝"""
		await message.edit(umd)
		return

	async def trkcmd(self, message):
		"""trk style"""
		
		umd = """
╔══╗╔╗
╚╗╔╬╣╠╗
─║║╔╣═╣
─╚╩╝╚╩╝"""
		await message.edit(umd)
		return
	
	async def trk2cmd(self, message):
		"""trk style 2"""
		
		umd = """
╔════╗╔╗
║╔╗╔╗║║║
╚╝║║╠╩╣║╔╗
──║║║╔╣╚╝╝
──║║║║║╔╗╗
──╚╝╚╝╚╝╚╝"""
		await message.edit(umd)
		return

	async def kzxcmd(self, message):
		"""kzx style"""
		
		umd = """
╔╦╦═╗
║╔╬═╠╦╗
║╚╣═╬║╣
╚╩╩═╩╩╝"""
		await message.edit(umd)
		return
	
	async def kzx2cmd(self, message):
		"""kzx style 2"""
		
		umd = """
╔╗╔═╗
║║║╔╝
║╚╝╝╔═══╦╗╔╗
║╔╗║╠══║╠╬╬╝
║║║╚╣║══╬╬╬╗
╚╝╚═╩═══╩╝╚╝"""
		await message.edit(umd)
		return

	async def jpncmd(self, message):
		"""jpn style"""
		
		umd = """
─╔╗
─║╠═╦═╦╗
╔╣║╬║║║║
╚═╣╔╩╩═╝
──╚╝"""
		await message.edit(umd)
		return
	
	async def jpn2cmd(self, message):
		"""jpn style 2"""
		
		umd = """
──╔╗
──║║
──║╠══╦═╗
╔╗║║╔╗║╔╗╗
║╚╝║╚╝║║║║
╚══╣╔═╩╝╚╝
───║║
───╚╝"""
		await message.edit(umd)
		return

	async def krscmd(self, message):
		"""krs style"""
		
		umd = """
╔╦╗─╔═╗
║╔╬╦╣═╣
║╚╣╔╬═║
╚╩╩╝╚═╝"""
		await message.edit(umd)
		return
	
	async def krs2cmd(self, message):
		"""krs style 2"""
		
		umd = """
╔╗╔═╗
║║║╔╝
║╚╝╝╔═╦══╗
║╔╗║║╔╣══╣
║║║╚╣║╠══║
╚╝╚═╩╝╚══╝"""
		await message.edit(umd)
		return

	async def chncmd(self, message):
		"""chn style"""
		
		umd = """
╔═╦╗
║╔╣╚╦═╦╗
║╚╣║║║║║
╚═╩╩╩╩═╝"""
		await message.edit(umd)
		return
	
	async def chn2cmd(self, message):
		"""chn style 2"""
		
		umd = """
╔═══╦╗
║╔═╗║║
║║─╚╣╚═╦═╗
║║─╔╣╔╗║╔╗╗
║╚═╝║║║║║║║
╚═══╩╝╚╩╝╚╝"""
		await message.edit(umd)
		return