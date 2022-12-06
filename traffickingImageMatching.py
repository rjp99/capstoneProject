#imports
import cv2
import tkinter as tk
from tkinter import filedialog

#set up gui window
window = tk.Tk()
text = tk.Label(window, text="")

#function to match images
def match_images(test):
    
    #for loop going through all images proven to be related to trafficking
    bestPercent = 0.0
    for i in range(12):
        #open folder with images
        img = cv2.imread('images/image'  + str(i+1) + '.jpg')


        print('\n\nIMAGE: '  + str(i+1))

        #match (using SIFT) the given image to the library images
        sift = cv2.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(img,None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(test,None)
        print('IMAGE keypoints: ', len(keypoints_1))
        print('TEST keypoints: ', len(keypoints_2))

        #match the keypoints of the images
        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        matches = bf.match(descriptors_1,descriptors_2)
        matches = sorted(matches, key = lambda x:x.distance)
        percent = round((len(matches)/len(keypoints_1)) * 100,2)

        if percent > bestPercent:
            bestPercent = percent
            bestMatch = "Image " + str(i+1) 

        print('DONE\n MATCHES:', len(matches), '\n Percentage Match: ', percent)

    #output
    text['text'] = ("The best match is: " + bestMatch + " at " + str(bestPercent) + "%.")
    text.place(x=100,y=180)

def uploadFile():

    text['text'] = ("")
    #upload only jpg file
    filename = filedialog.askopenfilename(title = "Select a File", filetypes = ([('Jpg Files', '*.jpg')]))

    #match images
    match_images(cv2.imread(filename))
    return

def main():
    #Set up gui title
    window.title('Human Trafficking Image Matching')
  
    # Set window size
    window.geometry("350x300")
    
    #Set window buttons and title
    explore = tk.Label(window, text = "Human Trafficking Image Matching")
    upload = tk.Button(window, text = "Upload Image", command = uploadFile)
    quit = tk.Button(window, text = "Quit", command = exit)

    #set up positions for buttons/ text
    window.grid_rowconfigure(1, minsize=100)
    explore.grid(column = 4, row = 1)
    upload.grid(column = 4, row = 6)
    quit.grid(column = 1,row = 0)

    window.mainloop()

main()
#free images from: https://unsplash.com