from flask import jsonify, request, make_response
from flask_restful import Resource, abort

#---import models
from models.tables import Images

#--- import db
from extensions import db

#--- for comparing img 
import cv2
import numpy as np
import requests
from io import BytesIO



#Examples of calls


class Compareimg(Resource): #to get all questions, or create a new one
    def get(self):
        pass

    def post(self):
        data = request.json
        url1 = data.get("url1") # original img
        url2 = data.get("url2") # img with differences marked
        url3 = data.get("url3") # img with differences not marked

        response1 = requests.get(url1)
        response2 = requests.get(url2)
        response3 = requests.get(url3)

        image_data1 = BytesIO(response1.content)
        image_data2 = BytesIO(response2.content)
        image_data3 = BytesIO(response3.content)

        image_array1 = np.asarray(bytearray(image_data1.read()), dtype=np.uint8)
        image_array2 = np.asarray(bytearray(image_data2.read()), dtype=np.uint8)
        image_array3 = np.asarray(bytearray(image_data3.read()), dtype=np.uint8)

        image1 = cv2.imdecode(image_array1, cv2.IMREAD_COLOR)
        image2 = cv2.imdecode(image_array2, cv2.IMREAD_COLOR)
        image3 = cv2.imdecode(image_array3, cv2.IMREAD_COLOR)


        difference = cv2.absdiff(image1, image2)
        gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #-----------------------------------------------------------------------------------------------------------
        #diff_coordinates = []
        #for contour in contours:
            #x, y, w, h = cv2.boundingRect(contour)
            #diff_coordinates.append((x, y, x + w, y + h))

        #for (x1, y1, x2, y2) in diff_coordinates:
         #   cv2.rectangle(image3, (x1, y1), (x2, y2), (0, 255, 0), 2)

        #Save or display the image with bounding boxes
        #cv2.imshow('image_with_bboxes.png', image3)
        #----------------------------------------------------------------------------------------------------------- this draws rectangles instead of wacky circles

        cv2.drawContours(image3, contours, -1, (0, 255, 0), 2)
        cv2.imshow('Image with Contours', image3)
        cv2.imshow('og', image1)
        cv2.imshow('differences', image2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        center_coordinates = []


        for contour in contours:
            # Calculate the moments of the contour
            M = cv2.moments(contour)
            
            # Calculate the centroid (center) of the contour
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                # Handle the case where the contour has no area (division by zero)
                cX, cY = 0, 0
            
            # Append the center coordinates to the list
            if cX != 0 and cY != 0:
                center_coordinates.append((cX, cY))

            # Print the center coordinates of each contour
        for i, (cX, cY) in enumerate(center_coordinates):
            print(f"Contour {i + 1}: Center = ({cX}, {cY})")

        
        return jsonify({"coordinates" : center_coordinates})
    
#class specificQuestion(Resource): 
    
    #def delete(self, question_id): 
       #pass

    
#class handleOption(Resource): 
    
    
    #def put(self,option_id):
        #data = request.json
        #pass
    
