import threading
import requests
import time

def get_data_sync(urls):        # birden fazla url olacak
    st = time.time()            # time.time()    o an bu kod hangi zamanda çalışıyorsa onun zamanını gösterir
    json_array = []             # birden fazla yere istek atacağız, cevaplar geldikçe bu json_array içine koyacağız

    for url in urls:
        json_array.append(requests.get(url).json())

    et = time.time()            # işlemin bitiş zamanını da alıyoruz
    elapsed = et-st             # geçen süreyi hesaplarız
    print("Execution time: ", elapsed, " seconds")

    return json_array


urls = ['https://postman-echo.com/delay/3'] * 10              # 3 saniye bekletmeli sayfa url i

get_data_sync(urls)   # 36 saniyede çalıştı

