import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
d = {'key':'value'}
m = {'key':'value'}
c = {'key':'value'}

cnt = 0
selfile=''
selparent=''

def orb_compute(file1,file2,cnt):

    img1 = cv2.imread(file1,0) # queryImage
    img2 = cv2.imread(file2,0) # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    file = os.path.basename(file2)
    parent=os.path.basename(os.path.dirname(file2))
    m[file]= matches
    c[file]= parent
    cnt = len(matches)
    #if(len(matches)>= cnt ):
    #    cnt=len(matches)
    #    selfile=file
    #    selcategory=parent
    return cnt

def pic_search(pic_list,cat_list,pic_path,):

    cnt = 0
    cnt1 = 0
    selfile = ''
    selcat = 0
    i = 0
    for pic in pic_list:
        file1 = f'./myapp/static/myapp/media/{pic}'
        file2 = f'./myapp/static/myapp/media/{pic_path}'

        cnt1 = orb_compute(file1, file2, cnt)
        if cnt1 >= cnt:
            selfile = file1
            selcat = cat_list[i]
        cnt = cnt1
        i = i + 1
        print(f"{file1},{file2},{cnt}")
    print(selfile)
    print(selcat)
    return selfile,selcat