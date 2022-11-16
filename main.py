import cv2 as cv

fclass = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eclass = cv.CascadeClassifier('haarcascade_eye.xml')

def fd(img, size=0.5):

    #cvtcolor converts img to gray here (it uses BRG insted of RGB)
    
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = fclass.detectMultiScale(gray, 1.3, 5)
    
    #detectMultiscale gives us the location of the features we want and it gives us 4 things, a tuple of x, y, height and width
    
    #converted to grayscale for optimisation purposes
   
    #this checks if the coordinates and the height and with values provided by the detect Multiscale fucntion is existing, which will only happen if the face is found otherwise it'll be an empty tuple, i tried using == insted of is but it crashed.
    
    if faces is ():
        return img

    #if no face is found the it will just return the image withouth any thing
    #this is resposoble for taking in the values and using them to draw a rectangle over the face using the coordinates provided by faces tuple from detectMultiScale

    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eclass.detectMultiScale(roi_gray)
    
    #same rectange making thing but for eyes here
    
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    roi_color = cv.flip(roi_color,1)
    return roi_color
    
    # 0 selects default camera feed

cap = cv.VideoCapture(0)

    #this is for the window that opens for image showing

while True:

    ret, frame = cap.read()
    cv.imshow('omg ye to mera face h!!!', fd(frame))
    if cv.waitKey(1) == 13: 

    #13 is the Enter Key, yhios is here so that the program can be exited brom the gui itself and Ctrl+C dosent have to be done to close the prpgram as clicking the window cloase button brom the Desktop enviorment dosnt close it
    
        break
        
cap.release()

    #releases the video capture

cv.destroyAllWindows()

    #closes/anhialates the windows to high heven
