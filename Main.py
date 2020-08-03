import cv2
import numpy
from time import *
import threading
from math import hypot
import multiprocessing
import asyncio

cup = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
x_list = []
thread_list = []






st_points = []
end_points = []
st_points_2 = []
end_points_2 = []
known_distance = 260
max_dist = 30

def Calk_focal_length(P, W, D = known_distance):
    F = (P * D) / W
    return F
print(Calk_focal_length(200, 70))
def Calk_distanse(P, W, F):
    D = (W * F) / P
    return round(D)




# def Thread(func):
#     def Wrapper(*args, **kwargs):
#         active_threads = []
#         while threading.active_count() < 2:
#
#             current_thread = threading.Thread(target= func, args= args, kwargs= kwargs)
#             current_thread.run()
#             current_thread.setName('My thread')
#             current_thread.getName()
#             active_threads.append(current_thread)
#             for
#
#

            # sleep(60)
            # current_thread.join()
            # current_thread.run()
    #
    # return Wrapper
# def Running(func, thr, ):
#     thread = thr
#     thread.run()
#
#
# # @Thread
def Delayer(timing):
    print('sleeping...')


#     sleep(timing)
# delay_thr = threading.Thread(target= Delayer(80))
# delay_thr.start()
#
#
# print(Delayer(300))
# time_thread = threading.Thread(Timer(60))
# time_thread.start()
#
#
#
#






while True:
    rel, frame = cup.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, gray_2 = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(gray_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(gray_2, [cnt], -1, (200, 50, 5), 3)

        cur = cv2.contourArea(cnt)
        print(cur)
        if cur > 38732.5:
            cv2.putText(gray,'Too low light!', (300, 100), cv2.FONT_ITALIC, 1, (200, 1, 1), 3)
        # else:
        #     cv2.putText(gray,'Enough light', (300, 100), cv2.FONT_ITALIC, 1, (200, 1, 1), 3)
    # _, thrashold = cv2.threshold(gray, 255, 5, cv2.THRESH_BINARY)
    # roi = gray[0:190, 0:640]
    shape = gray.shape
    font = cv2.FONT_ITALIC
    # threchold = cv2.thr

    # print(shape)
    # eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.1, minSize=(10, 10))

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minSize=(120, 80))




    for (fx, fy, fw, fh) in faces:
        roi = gray[fy + 5 : int(fy + fh / 2), fx : fx + fw]
        cv2.rectangle(gray, (fx, fy), (fx + fw, fy + fh), (1, 1, 255), 2)

        eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.1, minSize=(15, 15))

        for (x, y, w, h) in eyes:

                # cv2.line(roi, (x + w // 2, y + h // 2), (x + w // 2, y + h // 2), (200, 0, 0), 3 )
                cv2.rectangle(roi ,(x, y), (x + w, y + h), (1, 1, 255), 2)
                rect = cv2.rectangle(roi ,(x, y), (x + w, y + h), (1, 1, 255), 2)
                shape_2 = rect.shape
                print(shape_2)
                F = Calk_focal_length(shape_2[1], 70, 260)
                # print(shape_2[1])
                if int(Calk_distanse(shape_2[1], 70, 742.8)) // 10 < max_dist:
                    cv2.putText(gray, 'Keep the distance', (300, 300), font, 1, (200, 1, 1), 3)
                # print(str(Calk_distanse(shape_2[1], 70, 742.8) // 10))

                x_list.append(x + w // 2)
                # if len(eyes) >= 1:
                #     delay_thr.run()
                #     print(threading.active_count())
                #     print(threading.enumerate())
                #     if threading.active_count() == 1 and len(eyes) >= 1:
                #         cv2.putText(gray, "Give some rest to your eyes", (300, 200), font, 1, (200, 1, 1), 2)

                # hor_fir = (x, y + int(h/ 2))
                # st_points_2.append(hor_fir)
                # hor_sec = (x + w, y + int(h / 2))
                # end_points_2.append(hor_sec)
                # cv2.line(roi, hor_fir, hor_sec, (200, 1, 1), 3)
                # fir = (x  + int(w // 2), y)
                # st_points.append(fir)
                # sec = (x + int(w// 2), y + h)
                # end_points.append(sec)
                # cv2.line(roi, fir, sec, (200, 1, 1), 3)
                # ver_line_len = hypot((st_points[0] - end_points[0]), end_points_2[])






                # if state != 1 and time.time() - start >= 10:
                #     text = "You should blink your eyes"
                #     cv2.putText(gray, text, (240, 320), cv2.FONT_ITALIC, 1,(1, 1, 255), 3)
                # else:
                #     if time.time() - start > 5:
                #
                #         text = 'Good job!'
                #         cv2.putText(gray, text, (240, 320), cv2.FONT_ITALIC, 1, (1, 1, 255), 3)
                #

        #     for c in thread_list:
        #         c.start()













    cv2.imshow('Frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cup.release()
cv2.destroyAllWindows()