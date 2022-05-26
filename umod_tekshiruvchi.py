# ▀█▀ █▀▀ █▀▄▀█ █░█ █▀█
# ░█░ ██▄ █░▀░█ █▄█ █▀▄
# ═══════════════════════
# █▀▀ █▀█ █▄▀ █ █▄░█ █▀█ █░█
# ██▄ █▀▄ █░█ █ █░▀█ █▄█ ▀▄▀
# ═════════════════════════════
# meta developer: @netuzb
# meta channel: @umodules

from telethon import events
from .. import loader, utils
from asyncio import sleep
import random

__version__ = (3, 2, 21)

def register(cb):
	cb(TekshiruvchiMod())

umod_emoji = "🌇 "
umod_second = "\n🌉 "

class TekshiruvchiMod(loader.Module):
	"""Kerakli manzillar"""
	
	strings = {
		"name": "Tekshiruvchi",
		"izlash": umod_emoji + "<b>Quyidagi ijtimoiy tarmoqlardan maʼqulini tanlang</b>",
		"yut": umod_emoji + "<b>Shaxsan siz uchun YouTube'ga havola.</b>",
		"gug": umod_emoji + "<b>Shaxsan siz uchun Google'ga havola.</b>",
		}
		
	async def shxcmd(self, message):
		"""📃 inline - tekshirish manzillari"""
		
		text = utils.get_args_raw(message)
		top = f"\n<b>Izlanayotgan shaxs: <code>{text}</code></b>"
		await self.inline.form(
                    self.strings("izlash", message) + umod_second + top,
                    reply_markup=[
                        [{"text": "📔 Telegramda", "url": f"https://t.me/{text}"}],
                        [{"text": "📙  Instagramda", "url": f"https://instagram.com/{text}"}],
                        [{"text": "📘  Facebookda", "url": f"https://m.facebook.com/{text}"}],
                        [{"text": "📕  Twitterda", "url": f"https://twitter.com/{text}?lang=ru"}],
                    ],
                    ttl=10,
                    message=message,
                )

	async def yutcmd(self, message):
		"""📃 inline - youtube'dan izlash"""
		
		text = utils.get_args_raw(message)
		top = f"<b>Kiritilgan soʻz: <code>{text}</code></b>"
		await self.inline.form(
                    self.strings("yut", message) + umod_second + top,
                    reply_markup=[
                        [{"text": "🏙️ YouTube'ga", "url": f"https://m.youtube.com/results?sp=mAEA&search_query={text}"}],
                    ],
                    ttl=10,
                    message=message,
                )

	async def gugcmd(self, message):
		"""📃 inline - google'dan izlash"""
		
		text = utils.get_args_raw(message)
		top = f"<b>Kiritilgan soʻz: <code>{text}</code></b>"
		await self.inline.form(
                    self.strings("yut", message) + umod_second + top,
                    reply_markup=[
                        [{"text": "🏙️ Google'ga", "url": f"https://www.google.com/search?q={text}"}],
                    ],
                    ttl=10,
                    message=message,
                )             

	async def yandcmd(self, message):
		"""📃 inline - yandex'dan izlash"""
		
		text = utils.get_args_raw(message)
		top = f"<b>Kiritilgan soʻz: <code>{text}</code></b>"
		await self.inline.form(
                    self.strings("yut", message) + umod_second + top,
                    reply_markup=[
                        [{"text": "🏙️ Yandex'ga", "url": f"https://yandex.uz/search/touch/?text={text}"}],
                    ],
                    ttl=10,
                    message=message,
                )
