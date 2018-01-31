import numpy as np
import time
import json
import codecs
import random
#http://vision.imar.ro/human3.6m/description.php
#https://deeplearning4j.org/opendata
#https://github.com/ShownX/FacePaperCollection
#https://gist.github.com/smajida/8b86fe93b3c736a55146bc009cf771ab
#https://github.com/L706077/DNN-Face-Recognition-Papers
# http://www.iri.upc.edu/people/esimo/en/research/fashion/
# http://hi.cs.waseda.ac.jp/~esimo/en/data/fashion550k/
# https://github.com/bearpaw/clothing-co-parsing
#https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/
#tool segment
# http://web.archive.org/web/20110825025054/http://kspace.cdvp.dcu.ie:80/public/interactive-segmentation/screenshots.html
# https://www.researchgate.net/post/What_is_the_best_fee_software_for_image_segmentation
data = {}
# data['people'] = []
# data['people'].append(
#     {
#         'name': 'Scott',
#         'website': 'abc.com',
#         'from' : 'Web'
#     }
# )
#
# data['people'].append(
#     {
#         'name': 'Larry',
#         'website': 'def.com',
#         'from' : 'Mi'
#     }
# )
#
# data['people'].append(
#     {
#         'name': 'Tim',
#         'website': 'fds.com',
#         'from' : 'Al'
#     }
# )
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)
#     print("OK")
#
data['matrix'] = []
A = np.array(
    [[1,2],
    [3,4],
    [5,6]]
)
B = np.array(
    [[5,2],
    [3,0],
    [5,7]]
)
data['matrix'].append(A)
# data['matrix'].append(B)
# print(data['matrix'])
# print('start')
# with open('data.txt', 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile)
#     print("OK")

data2 = [[[0]*2]*3]*2
mask = np.array([
    [2,3,2],
    [3,3,3]
])
data4 = np.random.randint(3,size=(512,512))
data3 = np.random.randint(1,size=(512,512,10))
data5 = np.random.randint(1,size=(512,512,10))
startTime = time.time()
for i in range(10):
    data3[:,:, i] = np.where(
        data4 == 2,
        data3[:,:,i] + 1,
        data3[:,:, i]
    )
print("time: ", time.time() - startTime)
# print(data3)
startTime = time.time()
for i in range(10):
    for j in range(512):
        for k in range(512):
            if data4[j][k] == 2:
                data5[j][k][i] = 1
print("time: ", time.time() - startTime)
for i in range(10):
    for j in range(512):
        for k in range(512):
            if data3[j][k][i] != data5[j][k][i]:
                print("Wrong")
print("OK")


from skimage.io import imread_collection

#your path 
col_dir = 'cats/*.jpg'

#creating a collection with the available images
col = imread_collection(col_dir)


# fast load image
dir = 'data/'
list = [os.path.join(dir,f) for f in os.listdir(dir)]
print(list)

startTime = time.time()
image = []
for img in list:
    image.append( io.imread(img))
print (len(image))
print("time: ", time.time() - startTime)
startTime = time.time()
col = io.imread_collection(list)
print("time: ", time.time() - startTime)
# io.imshow(col[1])
print(sys.getsizeof(image))
print(sys.getsizeof(col))
del col
del image
pyplot.show()
