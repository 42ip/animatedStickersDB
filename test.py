import json,sys,requests,os
from PIL import Image

d = {}
with open(sys.path[0] + '/stickers.json') as f:
    d = json.load(f)
def getextension(url):
    if '.jpeg' in url:
        return '.jpeg'
    if '.png' in url:
        return '.png'
    if '.tif' in url:
        return '.tif'
    return '.gif'


stickersfolder = os.path.join(sys.path[0],'stickersraw')
for sticker in d.values():
    url = sticker[-1]
    imagetype = getextension(url)
    content = requests.get(url).content

    for name in sticker[:-1]:
        n = name + imagetype
        path = os.path.join(stickersfolder,n)
        with open(path,'wb') as f:
            f.write(content)
        if imagetype != ".gif":
            img = Image.open(path)
            img.save(os.path.join(stickersfolder,name) + ".gif")

# with open(sys.path[0] + '/00000001.gif','wb') as f:
#     f.write(requests.get('https://media.discordapp.net/attachments/881071746415992852/906889850832191528/IMG_1428.jpeg?width=410&height=400').content)




