#imports
import cv2

#function to match images
def match_images(image):
    #open folder with images
    count = 1
    img_name = 'image'  + str(count) + '.jpg'
    #retrieve first image
    ht_image = cv2.imread(img_name)
    #black and white - not sure if its needed
    imgColorlessHT = cv2.cvtColor(ht_image, cv2.COLOR_BGR2GRAY)
    testImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #for loop going through all images proven to be related to trafficking
    for i in range(20):
        #match (using SIFT) the given image to the library images
        sift = cv2.xfeatures2d.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(imgColorlessHT,None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(testImage,None)

        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

        matches = bf.match(descriptors_1,descriptors_2)
        matches = sorted(matches, key = lambda x:x.distance)

        img3 = cv2.drawMatches(imgColorlessHT, keypoints_1, testImage, keypoints_2, matches[:50], testImage, flags=2)
        plt.imshow(img3),plt.show()
        #if similarities are found return percentage (or true)
            #break
        #else go to next image

#main()
    #ask user to upload image
    #image = (get image)
    #result = match_images(image)
    #display result
