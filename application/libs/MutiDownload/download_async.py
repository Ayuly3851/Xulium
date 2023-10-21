from urllib.parse import urlparse, unquote
from tqdm.asyncio import tqdm_asyncio
from loguru import logger
import async_timeout
import asyncio
import aiohttp
import sys
import os

### FOR WINDOW
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

### REMOVE DEFAULT FORMAT
logger.remove(0)

class DownloadAsync:

	def __init__(self, 
				replace: bool = False,
				debug: bool = False,
			  ):
		self._replace = replace

		self.logger = Logger(debug)

	async def download_url(self, url: str = None, file_path: str = None, session: aiohttp.ClientSession = None) -> bool:
		if not url:
			logger.error("Missing `url`") 
			return
		if not file_path:
			logger.error("Missing `file_path`")
			return
		if not session:
			logger.error("Missing `session`")
			return
		if os.path.exists(file_path) and not self._replace:
			logger.info(f"{file_path} are exist. skip")
			return

		logger.info(f"Downloading {file_path}")

		try:
			async with async_timeout.timeout(120):
				async with session.get(url) as response:
					with open(file_path, "wb") as fd:
						async for data in response.content.iter_chunked(1024):
							fd.write(data)

		except Exception as ex:
			logger.warning(f"Failed while downloading {file_path}")
			logger.error(ex)
			self.failed += 1
			return False

		logger.success(f"Download {file_path}")
		self.success += 1
		return True

class MutiDownloadAsync(DownloadAsync):
	
	@logger.catch
	async def muti_download_async(self, urls: list[str] = None, out_folder: str = None, file_names: list[str] = None) -> list[bool]:
		if not urls:
			logger.error("Missing `urls`")
			return
		if not out_folder:
			logger.error("Mussing `out_folder`")
			return
		if not file_names:
			logger.error("Missing `file_names")
			return
		
		self.success = 0
		self.failed = 0
		
		async with aiohttp.ClientSession() as session:
			tasks = [self.download_url(url, out_folder + file_names[index], session) for index, url in enumerate(urls)]
			result = await asyncio.gather(*tasks)
			logger.info(f"Success {self.success} | Failed {self.failed}")
			return result

	
	def downloads(self, urls: list[str] = None, out_folder: str = None, file_names: list[str] = None) -> list[bool]:
		asyncio.run(self.muti_download_async(urls, out_folder, file_names))
		
class Logger:
	def __init__(self, debug: bool) -> None:
		self.is_debug = debug

		self.debug("DEBUG MODE ON!")

		if self.is_debug:

			### ADD DEBUG FORMAT
			logger.add(sys.stderr, format="<green>{time:HH:mm:ss A Z}</green> | <level><bold>{level:^4}</bold></level> | <y>{name}</y>:<y>{function}</y>:<y>{line}</y> <g>▶</g> <lvl>{message}</lvl>", level="DEBUG", colorize=True)

		else:
			### ADD NORMAL FORMAT
			logger.add(sys.stderr, format="<green>{time:HH:mm:ss A Z}</green> | <level><bold>{level:^4}</bold></level> <g>▶</g> <lvl>{message}</lvl>", level="INFO", colorize=True)

	def debug(self, debug_message: str) -> None:
		if self.is_debug:
			logger.debug(debug_message)

