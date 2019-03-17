## Find The M&M's!!!

This project makes use of OpenCV to find m&m's in multiple photos. The biggest help OpenCV offers is a built in function
called HOUGH_CIRCLES that can locate circular objects in images. The main issue was fading out the wooden background while 
still being able to locate the brown m&m's. A mix of carefully incremented functions of Gaussian BLur, Edge Detection, and 
Dilation allows the program to find and colorize all the M&M's in the picture. 

Below are the image results once it goes through the program. 
### Small image of M&M's on table:
<img width="1002" alt="Screen Shot 2019-03-17 at 2 02 10 PM" src="https://user-images.githubusercontent.com/35508425/54497295-960e0c80-48be-11e9-9910-b57fe9c6ddb5.png">

### Larger image of M&M's on tables: 
Note that there is an extra circle (top right). This happens on occasion as HOUGH_CIRCLES are not perfect. When we calculate 
the color however, the false circle falls below the threshold for brown so we do not count it letting us get an accurate count
M&M's. 



