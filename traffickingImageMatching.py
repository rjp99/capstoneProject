#imports
import cv2

#function to match images
def match_images(image):
    #open folder with images
    count = 1
    img_name = 'image'  + str(count) + '.jpg'
    #retrieve first image
    ht_image = cv2.imread(img_name)
    #for loop going through all images proven to be related to trafficking
        #match (using SIFT) the given image to the library images
        #if similarities are found return percentage (or true)
            #break
        #else go to next image

#main()
    #ask user to upload image
    #image = (get image)
    #result = match_images(image)
    #display result
