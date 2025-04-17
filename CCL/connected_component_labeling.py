import numpy as np
import cv2
import itertools
import copy
from random import randint

original = cv2.imread("C:/Users/PC/Desktop/images.jpg")
cv2.imshow("original image",original)
blur = cv2.GaussianBlur(original, (5,5),1)
cv2.imshow("blurred image image",blur)
gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray)
threshold1 = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)
threshold = threshold1[1]
cv2.imshow("thresholded image image",threshold)
kernel1= np.ones((5,5),np.uint8)
image = cv2.erode(threshold,kernel1,iterations = 1) 
cv2.imshow("eroded image image",image)

#resimdeki beyaz kısımalrı 1 yapıyoruz
#etiketler 2 den başlıyıcak
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j] == 255:
            image[i][j] = 1


#resimde beyaz kısımlar 1 olduğu için etiketi 2 den başlatacağım
label = 2
label_list = []
#resim matrisinden değerler alınıp üzerine yeni etiket değerleri atanacak 
for i in range(1,(image.shape[0]-1),1):
    for j in range(1,(image.shape[1]-1),1):
    #resim pikselleri üzerinde tek tek gezilecek
    #eğer önplan pikseliyse komşu piksellerine bakılacak
        if  image[i][j] != 0:
            #komşu pikselleri tanımla 
            left = image[i][j-1]
            up = image[i-1][j]
            left_up = image[i-1][j-1]
            right_up = image[i-1][j+1]
            a = [left,left_up,up,right_up]
            a = sorted(a) #listeyi küçükten büyüğe sırala
            b=[]
            #komşu piksellerden değeri 0 olmayan ve,
            #bir sonraki değere eşit olmayan sayılar b listesine alınır
            for z in a: 
                if (z != 0) & (z not in b):
                    b.append(z)
            #0 olan değerler çıkarılınca liste boyutu 0 oluyorsa,
            #yeni etiket ata, etiket değerini 1 arttır
            if len(b) == 0:
                labell=[label]
                if labell in label_list:
                    pass
                else:
                    label_list.append(labell)
                image[i][j] = label
                label = label+1
            #0 olan değerler çıkarılında liste boyutu 1 oluyorsa, 
            #listedeki değeri etiket olarak ata
            elif len(b) == 1:
                image[i][j] = b[0]
                if b in label_list:
                    pass
                else:
                    label_list.append(b)
            #0 olan değerler çıkarılınca liste boyutu 1den büyük ise 
            #b listesinin 0. değerini etiket
            else:
                image[i][j] = b[0]
                #eğer benzer b listesinden label_list'de varsa pas geç.
                if b in label_list:
                    pass
                #yoksa listeyi label_list'e aktar.
                else:
                    label_list.append(b)


d=[]


#burda benzer etiket değerleri için oluşturduğumuz label_list'i düzenliyoruz.
#listede aynı elemanlardan varsa bu iki listeyi birleştirecek. 
def group_equals(lst):
    groups = []
    for pair in lst:
        pair = set(pair)  
        equals_found = 0
        for idx, group in enumerate(groups):
            if group.intersection(pair):
                equals_found += 1
                if equals_found == 1:
                    # We found a first group that contains one of our values,
                    # we can add our pair to the group
                    group.update(pair)
                    first_group = group
                elif equals_found == 2:
                    # We found a second group that contains the other one of 
                    # our values, we merge it with the first one
                    first_group.update(group)
                    del groups[idx]    
                    break
        # If none of our values was found, we create a new group
        if not equals_found:
            groups.append(pair)

    return [list(sorted(group)) for group in groups]

label_list_last = group_equals(label_list)

#burda label_list_last'deki listede bulunan değerler yeni etiket değerleri ile değiştiriliyor.
#i ve j resim pikselleri içinde gezmek için 
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        #k ve l de label_list array'inde gezmek için
        for k in range(len(label_list_last)):  # k değeri kaç tane liste olduğunu veriyor. bunu etiket ataması için kullanıyoruz.
            for l in range(len(label_list_last[k])):
                if image[i][j] == label_list_last[k][l]:
                    image[i][j] = k + 1  #k 0 dan başladığı için 1 üst değerini etiket olarak atıyoruz.

image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
print("resimde {} tane nesne bulunuyor.".format(len(label_list_last)))
#bu kısım aynı etiket değeri olan pikselleri random renge boyamak için.
#kaç tane etiket değeri varsa o kadar random renk üretip listeye atıyoruz.
color_list=[(0,0,0)]        
for k in range(len(label_list_last)):
    r = np.uint8(randint(0, 255))
    g = np.uint8(randint(0, 255))
    b = np.uint8(randint(0, 255))
    rand_color = [r, g, b] 
    color_list.append(rand_color) 
    
#listedeki renkleri resme uyguluyoruz.
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        a=int(image[i][j][0])
        image[i][j] = np.uint8(color_list[a])
                                    
cv2.imshow("two-pass-algorithm",image)
cv2.waitKey(1)