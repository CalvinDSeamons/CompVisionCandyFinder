## Find The M&M's!!!

This project makes use of OpenCV to find m&m's in multiple photos. The biggest help OpenCV offers is a built in function
called HOUGH_CIRCLES that can locate circular objects in images. The main issue was fading out the wooden background while 
still being able to locate the brown m&m's. A mix of carefully incremented functions of Gaussian BLur, Edge Detection, and 
Dilation allows the program to find and colorize all the M&M's in the picture. 

Below are the image results once it goes through the program. 
