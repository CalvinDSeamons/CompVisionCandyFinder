import cv2 
import numpy as np
####################################################
#Author Calvin Seamons
#Computer Vision CSCI442
#Hunter Llyod class
#NOTE: For closing the Picture. You must have to clicked on the Image to close it, then it will promt you for new image or quit with 5.
####################################################
def __main__():
    print("All solutions are printed to the terminal! Images show computer vision finding the values")
    print("\n\n")
    choice = "candy"
    #Here the user can select the choice of media to scan.
    while(choice != str(8)):
        print("Select Photo or Video (NOTE: for grading please use candyBig.jpg (or equal size for the new 'stichedimage')")
        print("\t 1) one.jpg")
        print("\t 2) two.jpg")
        print("\t 3) three.jpg")
        print("\t 4) four.jpg")
        print("\t 5) candyBig.jpg")
        print("\t 6) video")
        print("\t 7) Type name of text file (for grading).")
        print("\t 8) Quit.")
        choice = input("")

        if(choice==str(1)):
            val = 'one.jpg'
            candyScan(val,1)

        elif(choice==str(2)):
            val = "two.jpg"
            candyScan(val,2)

        elif(choice==str(3)):
            val = "three.jpg"
            candyScan(val,3)

        elif(choice == str(4)):
            val = "four.jpg"
            candyScan(val,4)

        elif(choice ==str(5)):
            val = "candyBig.jpg"
            candyScan(val,6)
        elif(choice ==str(6)):
            videoCounter("ManMVideoSmall.mp4")

        elif(choice == str(7)):
            val = input("Enter File name:")
            candyScan(val,7)

        elif(choice==str(10)):
            val = "candyBigSmaller.jpg"
            candyScan(val,8)

        elif(choice==str(9)):
            val = "candyBigSmallerTiny.jpg"
            candyScan(val,9)

    print("bye...")
#main method to scan and find candy
def candyScan(photo,value):
        height = 0
        width = 0
        img = cv2.imread(photo)
        height, width, channels = img.shape
        #kernel definition of dilation and erotion
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
        key = None
        #here we blur get edges,dilate, then blur again and start looking for circles
        black = np.zeros((height,width,3), np.uint8)
        edge = cv2.GaussianBlur(img,(11,9),1.55)
        edge = cv2.Canny(edge,88,99)
        edge = cv2.dilate(edge,kernel,iterations=1)
        edge = cv2.GaussianBlur(edge,(19,5),0)
        #circles are defined here as 6-60pxl they cannot be within 30 pixels of center to another center. 
        #limit on center keeps from multiple circles stacking on eachother
        #if(height ==800 and width == 600):
        
        circles = cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,1,30,param1=60,
        param2=29,minRadius=6,maxRadius=60)

        if circles is not None:
        #here i scan through all the circles and draw them onto the image.
         circles = np.uint16(np.around(circles))
         for i in circles[0,:]:
             cv2.circle(img,(i[0],i[1]),int(i[2])-0,(255,255,255),2)
            
        ########################################################
        #time to get colors from circle!
        #below are variables to capture the total amount of shapes in each image.
        totalred=0
        totalblue=0
        totalgreen=0
        totalbrown=0
        totalyellow=0
        totalorange=0
        for j in circles[0,:]: #here i loop through to capture all pixels in the radius of the circle
            totalPixel = 0
            r = 0
            b = 0
            g=0
            for x in range(j[1]-j[2]+8, j[1]+j[2]-8):
                for y in range(j[0]-j[2]+8,j[0]+j[2]-8):
                        black[x,y] = img[x,y]
                        BGR   = img[x,y]
                        if(BGR[0] ==  0 and BGR[1] == 0 and BGR[2] == 0):#if its white we ignore (can affect average color val)
                            continue
                        else:
                            #increment total blue red and green...
                            b  += BGR[0]
                            g  += BGR[1]
                            r  += BGR[2]
                            totalPixel+=1

            #here i get the average of each color inside the shapes.
            
            r = int(r/totalPixel)
            g = int(g/totalPixel)
            b = int(b/totalPixel)
         

            #this loops colors the average color on a blank image to better show location and colors.
            for x in range(j[1]-j[2]+8, j[1]+j[2]-8):
                for y in range(j[0]-j[2]+8,j[0]+j[2]-8):
                    black[x,y,0] = b
                    black[x,y,1] = g
                    black[x,y,2] = r
               

            #Here is a conditional block to determine what color is what.
            if((b<130) and (g<130) and (r<130) and (b>30) and (g>30) and (r>30)):
                totalbrown = totalbrown+1
            
            elif((b>225) and (g > 149) and (g<209) and (r<45)):
                totalblue = totalblue+1

            elif((g>80) and (r < 35) and (b>55) and (b<255)):
                totalgreen = totalgreen+1

            elif((r>200) and (g>200) and (b<100)):
                totalyellow = totalyellow+1

            elif((r>150) and (b>63) and (b<160) and (g<123) and (g>35)):
                totalred = totalred+1
                #print("RED: "+str(j[0])+ " " + str(j[1]))

            if((r>172) and (g>99) and(g<165) and (b>25) and (b<129)):
                totalorange = totalorange+1
                #print("ORANGE: "+str(j[0])+ " " + str(j[1]))

        #after block we print out the total number of m&ms we find.
        print("#"*40)
        print("Brown: 16 Blue: 17 Green: 14 Orange: 8 Yellow: 14 Red: 7")
        print("Result of Imaged Scanned:")
        print("Brown: " + str(totalbrown)+ " Blue: " + str(totalblue) + " Green: " + str(totalgreen) + 
                " Orange: "+str(totalorange)+" Yellow: " + str(totalyellow)+ " Red: " +str(totalred))
        print("#"*40)
        tb = totalbrown
        tbl = totalblue
        tg = totalgreen
        to = totalorange
        ty = totalyellow
        tr = totalred
        cv2.putText(img,'Brown:' + str(tb) + '  Blue:' + str(tbl) + '  Green:' + str(tg),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2,cv2.LINE_AA)  
        cv2.putText(img,'Orange:' + str(to) + '  Red:'+ str(tr) + '  Yellow:' + str(ty),(50,100), cv2.FONT_HERSHEY_COMPLEX, 1 ,(0,0,0),2,cv2.LINE_AA)
        #here i show the black image with the average shaps and colors on them
        cv2.imshow('Orgin',black)
        #here i show the first image with the circles drawn on them.
        cv2.imshow('PreCircle',img)

        #condition to quit images...
        key == cv2.waitKey(0)
        if key:
         cv2.destroyWindow(img)
        cv2.destroyAllWindows()




def videoCounter(video):
    key = None
    cap = cv2.VideoCapture('MandMVideoSmall.mp4')
    while(cap.isOpened()):
        ret,frame=cap.read()
        cv2.imshow('Frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release() 
    cv2.destroyAllWindows()












__main__()

