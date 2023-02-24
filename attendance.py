import numpy as np
import cv2
import pickle
from conect_to_DB import mycursor
from conect_to_DB import myconn
from datetime import datetime

class takeAttendance():

    def att():

        face_cascade = cv2.CascadeClassifier(
            'cascades/data/haarcascade_profileface.xml')
        face_cascade2 = cv2.CascadeClassifier(
            'cascades/data/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainner.yml")
        labels = {"person_name": 1}
        with open("abels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}
        cap = cv2.VideoCapture(0)
        while (True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.4, minNeighbors=5)
            facess = face_cascade2.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in facess:
                roi_gray = gray[y:y+h, x:x+w]

                id_, conf = recognizer.predict(roi_gray)
                if conf >= 45 and conf <= 85:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1,
                                color, stroke, cv2.LINE_AA)
                    print(name)
                    name = labels[id_]
                    return name
                color = (255, 0, 0) 
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h

                cv2.rectangle(frame, (x, y), (end_cord_x,
                              end_cord_y), color, stroke)

            for (xi, yi, wi, hi) in faces:


                roi_gray = gray[yi:yi+hi, xi:xi+wi]  


            # recognize? deep learned model predict keras tensorflow pytorch scikit learn
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 4 and conf <= 84:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name2 = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (xi, yi), font, 1,
                                color, stroke, cv2.LINE_AA)
                    print(name)
                    return name2
                color = (255, 0, 0) 
                stroke = 2

                end_cord_xi = xi + wi
                end_cord_yi = yi + hi
                cv2.rectangle(frame, (xi, yi), (end_cord_xi,
                                                end_cord_yi), color, stroke)


            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    def insert():
        studentid = takeAttendance.att()
        st = str(studentid)
        global local_time,local_date,today
        local_time = datetime.strptime(datetime.today().strftime('%H:%M:%S'), '%H:%M:%S').time()
        local_date = datetime.today().strftime("%Y-%m-%d")
        today = datetime.today().strftime("%A")
        print(today)
        sql1 = "SELECT * FROM section_registration WHERE student_Id=%s AND day=%s"
        mycursor.execute(sql1, (st, str(today)))
        a = mycursor.fetchall()
        
        if len(a)==0:
            print("there is no section for student")
            print("i am here")
        else: 
            for results in a:                
                    start_time1 = datetime.strptime(str(results[2]), '%H:%M:%S').time()
                    end_time1 = datetime.strptime(str(results[3]), '%H:%M:%S').time()
                    att_time = datetime.strptime(local_time.strftime("%H:%M:%S"), "%H:%M:%S").time()
                    section = results[1]
                    class_n = results[5]
                    sql4 = "SELECT * FROM attendance WHERE student_id=%s AND day=%s AND date=%s and section_id=%s"
                    # if the student did not take attendance for the the same date and section 
                    mycursor.execute(sql4, (int(st), str(today),local_date,int(section)))
                    b = mycursor.fetchall()

                    if len(b)==0 and att_time >= start_time1 and att_time <= end_time1:
                              sql = "INSERT IGNORE INTO  attendance (student_id,section_id,status_s,attendance_time,start_time,end_time,class_name,day,date) VALUES (%s,%s,'Present',%s,%s,%s,%s,%s,%s)"
                              mycursor.execute(sql, (st, int(section), local_time, start_time1, end_time1, str(class_n), str(today), local_date))
                              print("insert done 1")
                              myconn.commit()
                              
                         
                    elif len(b)==0 and att_time >= start_time1 and att_time >= end_time1:
                                    sql = "INSERT IGNORE INTO  attendance (student_id,section_id,status_s,attendance_time,start_time,end_time,class_name,day,date) VALUES (%s,%s,'Absent',%s,%s,%s,%s,%s,%s)"
                                    mycursor.execute(sql, (st, int(section), local_time, start_time1, end_time1, str(class_n), str(today), local_date))
                                    print("insert done 1")
                                    myconn.commit()     
                   
                    else:
                     for i in b:
                        print(i[3])
                        if i[3]=="Present":

                                    print("Present attendance has been taken ")
                        else:
                             print(" absent attendance has been taken ")    
                        
 

        sql7 = "SELECT * FROM section_registration WHERE day=%s"  
        mycursor.execute(sql7,(str(today),)) 
        results=mycursor.fetchall()
        if results==0:   
                    print("there is no section today") 
        else:  
                 for x in results:
                        start_time2 =datetime.strptime(str(x[2]), "%H:%M:%S").time()
                        end_time2 = datetime.strptime(str(x[3]), "%H:%M:%S").time()
                        class_n2 = x[5]    
                        if(local_time >= start_time2 and local_time >= end_time2):
                            sql2 = "INSERT IGNORE INTO attendance (student_id,section_id,attendance_time,start_time,end_time,class_name,day,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                            sql3 ="SELECT *\
                            FROM section_registration\
                            WHERE student_Id NOT IN(SELECT student_id\
                                    FROM attendance) and Start_time = %s and End_time = %s and day = %s"
                            sql4 ="SELECT *\
                            FROM section_registration\
                            WHERE student_Id  IN(SELECT student_id\
                                    FROM attendance) and Start_time = %s and End_time = %s and day = %s"
                            mycursor.execute(sql3,(start_time2,end_time2,str(today)))
                            results2=mycursor.fetchall()
                            for i in results2:

                                studentid_ = int(i[0])
                                sectionid_ = int(i[1])
                                mycursor.execute(sql2, (studentid_, sectionid_, local_time, start_time2, end_time2, str(class_n2), str(today), local_date))
                                myconn.commit()

                            mycursor.execute(sql4,(start_time2,end_time2,str(today)))
                            results2=mycursor.fetchall()
                            for i in results2:

                                studentid_ = int(i[0])
                                sectionid_ = int(i[1])
                                mycursor.execute(sql2, (studentid_, sectionid_, local_time, start_time2, end_time2, str(class_n2), str(today), local_date))
                                myconn.commit()
                             
