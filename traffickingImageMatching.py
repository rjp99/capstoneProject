#imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

#function to match images
def match_images(test):
    
    #for loop going through all images proven to be related to trafficking
    for i in range(9):
        #open folder with images
        #retrieve first image
        img = cv2.imread('images/image'  + str(i+1) + '.jpg')
        print('\n\nIMAGE: '  + str(i+1))

        #match (using SIFT) the given image to the library images
        sift = cv2.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(img,None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(test,None)
        print('IMAGE keeypoints: ', len(keypoints_1))
        print('TEST keeypoints: ', len(keypoints_2))

        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

        matches = bf.match(descriptors_1,descriptors_2)
        matches = sorted(matches, key = lambda x:x.distance)

        ##COMMENT OUT IF YOU DON'T WANT TO SEE THE PLOTS
        img3 = cv2.drawMatches(img, keypoints_1, test, keypoints_2, matches[:50], test, flags=2)
        plt.imshow(img3),plt.show()
        print('DONE\n MATCHES:', len(matches), '\n Percentage Match: ', (len(matches)/len(keypoints_1)))
        #return
        #if 40% similarities are found return
        if (len(matches)/len(keypoints_1) > .4):
            print('THE IMAGES ARE A MATCH')
            return
            #break
        #else go to next image

def main():
    #ask user to upload image

    #image = (get image)
    test1 = cv2.imread('images/test.jpg')
    match_images(test1)

    test2 = cv2.imread('images/test2.jpg')
    match_images(test2)
    #display result

main()
