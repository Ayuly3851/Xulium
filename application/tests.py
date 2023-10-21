from libs.MutiDownload import DownloadAsync, MutiDownloadAsync
import asyncio
# import libs.
muti_download_async = MutiDownloadAsync(replace = True)

# asyncio.run(da.download_url(url = 1,file_path = 1, session = 1))

urls = ["https://rr1---sn-8qj-8ppe.googlevideo.com/videoplayback?expire=1694950862&ei=bZEGZeLwOqa02roPofeukAg&ip=2001%3Aee0%3A4363%3A4460%3Af69f%3A4ac4%3A8663%3A643a&id=o-AK137zbW8JY01xEPt2p8kTA1yTeds2h1r5XcVv_-D4L5&itag=140&source=youtube&requiressl=yes&mh=82&mm=31%2C29&mn=sn-8qj-8ppe%2Csn-8qj-i5ody&ms=au%2Crdu&mv=m&mvi=1&pl=53&initcwndbps=1828750&vprv=1&mime=audio%2Fmp4&gir=yes&clen=3044424&dur=188.058&lmt=1576459563930070&mt=1694928797&fvip=3&keepalive=yes&fexp=24007246&c=ANDROID_MUSIC&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgMHu9GzZ9G_2kT9g6O7WK6Qjbkea6R_pFDO1OqB47nm4CIDH4Q6ml8Ofj7Dt-ho2rujM9a-VkVmMwPemqJASveD3t&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPI5DMrk1DwIm9NyM0Hd74gkmzuF-jXnvplba9EYQkfrAiEAlqzH5qhtZbTX6Lu93UpbOhImKllKiW0P7NkkQN6TklQ%3D", "https://rr4---sn-8qj-8ppe.googlevideo.com/videoplayback?expire=1694950987&ei=65EGZYmZLYSMvcAPo_C7uAM&ip=2001%3Aee0%3A4363%3A4460%3Af69f%3A4ac4%3A8663%3A643a&id=o-ABofv3_1L5Bqo-mdwu6nC4YA6QpUK2Dwtuw8mR8roALf&itag=140&source=youtube&requiressl=yes&mh=k7&mm=31%2C29&mn=sn-8qj-8ppe%2Csn-8qj-i5ody&ms=au%2Crdu&mv=m&mvi=4&pcm2cms=yes&pl=53&initcwndbps=1847500&vprv=1&mime=audio%2Fmp4&gir=yes&clen=4899131&dur=302.648&lmt=1671013596047356&mt=1694929034&fvip=6&keepalive=yes&fexp=24007246&beids=24350017&c=ANDROID_MUSIC&txp=5318224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgJMm5Htjs4IfYOQbLSGdyJ20LweX__uqsLtNqVBgBa-cCIQDNO7qKP8HV0iSnnalrc80bNkV9NjJDYkH1vC9t0hbikg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgBlYYRx31lDSqtfwWwVdFBRS-E1mz-Ha_PnBvGjfmwFkCIEj8PL6QLr5iWo8sUlrNl9yzMO-2oJXNYRrWkTHUf_Ps"]
out_folder = "/home/ayuly/sda3/.Data/Xulium/"
file_names = ["Better Days.mp3", "Franco - Better Days (Lyrics).mp3"]

muti_download_async.downloads(urls = urls, out_folder = out_folder, file_names = file_names)

# import time
# from loguru import logger
# from rich.console import Console
# from rich.progress import Progress
#
# console = Console(color_system=None)
# logger.remove()
#
# logger.add(
#     lambda m: console.print(m, end=""),
#     level='TRACE',
#     format="<green>{time:HH:mm:ss A Z}</green> | <level><bold>{level:^4}</bold></level> <g>▶</g> <lvl>{message}</lvl>",
#     colorize=True,
# )
#
# def work(i):
#     logger.debug("Working: {}", i)
#     time.sleep(0.05)
#
# def main():
#     logger.info("Before")
#     with Progress(console=console) as progress:
#         for i in progress.track(range(100)):
#             work(i)
#     logger.info("After")
#
#
# if __name__ == "__main__":
#     # logger.remove()  # Remove default 'stderr' handler
#     #
#     # # We need to specify end=''" as log message already ends with \n (thus the lambda function)
#     # # Also forcing 'colorize=True' otherwise Loguru won't recognize that the sink support colors
#     # logger.add(lambda m: console.print(m, end=""), colorize=True)
#
#     main()


# import asyncio
# import random
#
# from tqdm.asyncio import tqdm_asyncio
#
#
# class AsyncException(Exception):
#     def __int__(self, message):
#         super.__init__(self, message)
#
#
# async def some_coro(simu_exception=False):
#     delay = round(random.uniform(1.0, 5.0), 2)
#
#     # We will simulate throwing an exception if simu_exception is True
#     if delay > 4 and simu_exception:
#         raise AsyncException("something wrong!")
#
#     await asyncio.sleep(delay)
#
#     return delay
#
# async def main():
#     tasks = []
#     for _ in range(2000):
#         tasks.append(some_coro())
#
#     for done in tqdm_asyncio.as_completed(tasks):
#         await done
#
#     print(f"The tqdm_asyncio.as_completed also works fine.")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
