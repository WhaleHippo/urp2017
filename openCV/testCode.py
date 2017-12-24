

#from : http://blog.naver.com/PostView.nhn?blogId=chandong83&logNo=220929493682&categoryNo=29&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView&userTopListOpen=true&userTopListCount=20&userTopListManageOpen=false&userTopListCurrentPage=1
import cv2
import mod1
'''
CAM_ID = 0
FRAME_COUNT = 0
cam = cv2.VideoCapture(CAM_ID)
if cam.isOpened() == False:
    print ('Can\'t open the CAM(%d)' % (CAM_ID))
    exit()
else :
    print ('Can open the CAM(%d)' % (CAM_ID))


width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print ('size = [%f, %f]\n' % (width, height))


cv2.namedWindow('CAM_Window')
cv2.resizeWindow('CAM_Window', 1280, 720)

while(True):
    FRAME_COUNT = FRAME_COUNT + 1

    ret, frame = cam.read()
    if(ret):

        cv2.imshow('CAM_Window', frame)
        

        img = mod1.Rotate(frame, 180) #90 or 180 or 270

        #cv2.imshow('CAM_RotateWindow', img)
        
        # test edge
        cv2.imshow('CAM_edge_Window', mod1.edge(frame))

        if FRAME_COUNT == 100 :
            cv2.imwrite("result.png", mod1.edge(frame));


        if cv2.waitKey(10) >= 0:
            1+1
            #break 
    else:
        break


cam.release()
cv2.destroyWindow('CAM_Window')
cv2.destroyWindow('CAM_RotateWindow')
cv2.destroyWindow('CAM_edge_Window')
'''
frame = cv2.imread("parking.jpg");
cv2.imwrite("result.png", mod1.edge(frame));
