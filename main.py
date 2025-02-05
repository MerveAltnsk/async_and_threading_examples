import threading
import requests
import time
import asyncio
import aiohttp

def get_data_sync(urls):        # birden fazla url olacak
    st = time.time()            # time.time()    o an bu kod hangi zamanda çalışıyorsa onun zamanını gösterir
    json_array = []             # birden fazla yere istek atacağız, cevaplar geldikçe bu json_array içine koyacağız

    for url in urls:
        json_array.append(requests.get(url).json())

    et = time.time()            # işlemin bitiş zamanını da alıyoruz
    elapsed = et-st             # geçen süreyi hesaplarız
    print("Execution time: ", elapsed, " seconds")

    return json_array





class ThreadingDownloader(threading.Thread):            # Aynı anda birden fazlaişlem yaptırırken Threading kullanabiliriz

    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array


def get_dat_treading(urls):

    st = time.time()  # time.time()    o an bu kod hangi zamanda çalışıyorsa onun zamanını gösterir

    threads = []
    for url in urls:
        t = ThreadingDownloader(url)     #KEndi oluşturduğummuz sınıf
        t.start()                        # start  dendiği anda def run fonksiyonu çalışacak
        threads.append(t)

    for t in threads:
        t.join()
        #print(t)


    et = time.time()  # işlemin bitiş zamanını da alıyoruz
    elapsed = et - st  # geçen süreyi hesaplarız
    print("Execution time: ", elapsed, " seconds")




async def get_data_async_but_as_wrapper(urls):
    st = time.time()  # time.time()    o an bu kod hangi zamanda çalışıyorsa onun zamanını gösterir
    json_array = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())

    et = time.time()  # işlemin bitiş zamanını da alıyoruz
    elapsed = et - st  # geçen süreyi hesaplarız
    print("Execution time: ", elapsed, " seconds")
    return json_array





async def get_data(session, url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []


    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
        await asyncio.gather(*tasks)


    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return json_array





urls = ['https://postman-echo.com/delay/3'] * 10              # 3 saniye bekletmeli sayfa url i

#get_data_sync(urls)                                     # 36 saniyede çalıştı
#get_dat_treading(urls)                                  # 3.6 saniyede çalıştı
#asyncio.run(get_data_async_but_as_wrapper(urls))        # 32 saniyede çalıştı
asyncio.run(get_data_async_concurrently(urls))           # 4 saniyede çalıştı
