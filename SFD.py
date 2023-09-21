import time
import requests

def progressbar(total, current, barsize=60):

    progress = int(current*barsize/total)
    print(f'{chr(9608)*progress} {"."*(barsize-progress)} {current/total*100:.2f}% {current}/{total} bytes', sep='', end='\r', flush=True)

print("Hello, please provide url (example: https://yoursite.com/filename.extension) or write 'q' to quit")
url = input()
while (url != 'q'):
    if url == 'q': exit()
    else:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(url.split('/')[-1], 'wb') as f:
                print("Downloading %s" % url.split('/')[-1])
                total_length = int(r.headers.get('content-length'))

                if total_length is None: # no content length header
                    f.write(r.content)
                else:
                    dl = 0
                    progressbar(total_length, dl)
                    oldtime = time.time()
                    for chunk in r.iter_content(chunk_size=2048):
                        if not chunk: 
                            break
                        dl += len(chunk)
                        f.write(chunk)
                        if (time.time() - oldtime >= 1):
                            oldtime = time.time()
                            progressbar(total_length, dl)
                    progressbar(total_length, dl) 
                    print("Download is complete.")
    url = input()
