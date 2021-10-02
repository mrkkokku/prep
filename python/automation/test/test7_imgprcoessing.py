import requests
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as npimg

url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream=True).raw

img = Image.open(r)
#img.show()
img.save('src.png')

BUF_SIZE = 1024

with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)

dst_img = npimg.imread('dst.png')
print(dst_img)

pseudo = dst_img [:, :, 0]
print (pseudo)

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(npimg.imread('src.png'))

plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = npimg.imread('dst.png')
pseudo = dst_img[:, :, 0]
plt.imshow(pseudo)
plt.show()