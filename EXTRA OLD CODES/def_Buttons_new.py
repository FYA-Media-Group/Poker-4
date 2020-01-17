import pyautogui
from pyautogui import pixelMatchesColor

po=pyautogui.locateOnScreen('mainpic.png')

def Available_Seat(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+362, po[1]+408, (1,79,164) ) #Seat1
        x2 = pixelMatchesColor( po[0]+362, po[1]+408, (21,102,189) ) #Seat1_Light
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+107, po[1]+411, (1,78,163) ) #Seat2
        x2 = pixelMatchesColor( po[0]+107, po[1]+411, (21,101,188) ) #Seat2_Light
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-148, po[1]+408, (1,79,164) ) #Seat3
        x2 = pixelMatchesColor( po[0]-148, po[1]+408, (21,102,189) ) #Seat3_Light
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-178, po[1]+103, (1,79,164) ) #Seat4
        x2 = pixelMatchesColor( po[0]-178, po[1]+103, (21,102,189) ) #Seat4_Light
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+392, po[1]+103, (1,79,164) ) #Seat5
        x2 = pixelMatchesColor( po[0]+392, po[1]+103, (21,102,189) ) #Seat5_Light
        return (x1 or x2)

def Click_on_Available_Seat(Number): #this function is already satisfied in Sit In
    if Number == 1 :
        pyautogui.click( po[0]+362, po[1]+408 ) #Seat1
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5

def Fold_Button():
    x1 = pixelMatchesColor( po[0]+51, po[1]+581, (190,22,28) ) #Fold
    x2 = pixelMatchesColor( po[0]+51, po[1]+581, (220,27,33) ) #Fold_Light
    return (x1 or x2)

def Click_on_Fold_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Fold_Button() :
        pyautogui.click( po[0]+51, po[1]+581 )
    else :
        Vital_Signs()
        if Cards( My_Seat_Number ) and Fold_Button() :
            pyautogui.click( po[0]+51, po[1]+581 )            

def Check_Button():
    x1 = pixelMatchesColor( po[0]+246, po[1]+578, (1,83,170) ) #Check_up
    x2 = pixelMatchesColor( po[0]+246, po[1]+584, (254,254,254) ) #Check_down
    x3 = pixelMatchesColor( po[0]+246, po[1]+578, (1,95,194) ) #Check_up_Light
    x4 = pixelMatchesColor( po[0]+246, po[1]+584, (254,254,254) ) #Check_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Check_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Check_Button() :
        pyautogui.click( po[0]+246, po[1]+578 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Check_Button1 = Check_Button()
        if Cards( My_Seat_Number ) and Check_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+246, po[1]+578 )
        else :
            Check_Mod = True
            
def Call_Button():
    x1 = pixelMatchesColor( po[0]+261, po[1]+575, (0,84,172) ) #Call_up
    x2 = pixelMatchesColor( po[0]+260, po[1]+579, (249,249,249) ) #Call_down
    x3 = pixelMatchesColor( po[0]+261, po[1]+575, (0,97,198) ) #Call_up_Light
    x4 = pixelMatchesColor( po[0]+260, po[1]+579, (249,249,249) ) #Call_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Call_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Call_Button() :
        pyautogui.click( po[0]+261, po[1]+575 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Call_Button1 = Call_Button()
        if Cards( My_Seat_Number ) and Call_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+261, po[1]+575 )
        else :
            Check_Mod = True

def Bet_Button():
    x1 = pixelMatchesColor( po[0]+461, po[1]+576, (24,115,0) ) #Bet_up
    x2 = pixelMatchesColor( po[0]+463, po[1]+579, (242,242,242) ) #Bet_down
    x3 = pixelMatchesColor( po[0]+461, po[1]+576, (28,135,0) ) #Bet_up_Light
    x4 = pixelMatchesColor( po[0]+463, po[1]+579, (242,242,242) ) #Bet_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Bet_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Bet_Button() :
        pyautogui.click( po[0]+461, po[1]+576 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Bet_Button1 = Bet_Button()
        if Cards( My_Seat_Number ) and Bet_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+461, po[1]+576 )
        else :
            Check_Mod = True

def Raise_Button():
    x1 = pixelMatchesColor( po[0]+461, po[1]+576, (25,117,0) ) #Raise_up
    x2 = pixelMatchesColor( po[0]+448, po[1]+579, (239,239,239) ) #Raise_down
    x3 = pixelMatchesColor( po[0]+461, po[1]+576, (29,137,0) ) #Raise_up_Light
    x4 = pixelMatchesColor( po[0]+448, po[1]+579, (239,239,239) ) #Raise_down_Light
    return ( (x1 and x2) or (x3 and x4) )

def Click_on_Raise_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Raise_Button() :
        pyautogui.click( po[0]+461, po[1]+576 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Raise_Button1 = Raise_Button()
        if Cards( My_Seat_Number ) and Raise_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+461, po[1]+576 )
        else :
            Check_Mod = True

def Plus_Button():
    x1 = pixelMatchesColor( po[0]+246, po[1]+648, (58,68,83) ) #Plus_Button
    x2 = pixelMatchesColor( po[0]+246, po[1]+648, (77,88,105) ) #Plus_Button_Light
    return (x1 or x2)

def Number_of_Clicks_on_Plus_Button(Number): #Number of clicks
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Plus_Button() :
        for i in range (Number):
            pyautogui.click( po[0]+246, po[1]+648 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Plus_Button1 = Plus_Button()
        if Cards( My_Seat_Number ) and Plus_Button1 and time1 <= 10 :
            for i in range (Number):
                pyautogui.click( po[0]+246, po[1]+648 )
        else :
            Check_Mod = True

def Minus_Button():
    x1 = pixelMatchesColor( po[0]-9, po[1]+648, (58,68,83) ) #Minus_Button
    x2 = pixelMatchesColor( po[0]-9, po[1]+648, (77,88,105) ) #Minus_Button_Light
    return (x1 or x2)

def Number_of_Click_on_Minus_Button(Number): #Number of clicks
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Minus_Button() :
        for i in range (Number):
            pyautogui.click( po[0]-9, po[1]+648 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        Minus_Button1 = Minus_Button()
        if Cards( My_Seat_Number ) and Minus_Button1 and time1 <= 10 :
            for i in range (Number):
                pyautogui.click( po[0]-9, po[1]+648 )
        else :
            Check_Mod = True

def All_In_Button():
    x1 = pixelMatchesColor( po[0]+531, po[1]+648, (207,90,6) ) #All_In_Button
    x2 = pixelMatchesColor( po[0]+531, po[1]+648, (235,98,0) ) #All_In_Button_Light
    return (x1 or x2)

def Click_on_All_In_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if All_In_Button() :
        pyautogui.click( po[0]+531, po[1]+648 )
    else :
        time0 = time.time()
        Vital_Signs()
        time1 = time.time() - time0
        All_In_Button1 = All_In_Button()
        if Cards( My_Seat_Number ) and All_In_Button1 and time1 <= 10 :
            pyautogui.click( po[0]+531, po[1]+648 )
        else :
            Check_Mod = True

def Exit_Button():
    x1 = pixelMatchesColor( po[0]+378, po[1]+21, (130,135,146) ) #Exit_Button
    x2 = pixelMatchesColor( po[0]+378, po[1]+21, (156,160,168) ) #Exit_Button_Light
    return (x1 or x2)

def Click_on_Exit_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Exit_Button():
        pyautogui.click( po[0]+378, po[1]+21 )
    else :
        Vital_Signs()
        if Exit_Button():
            pyautogui.click( po[0]+378, po[1]+21 )
        else : #can't proceed to here
            Raise_What_is_Problem("Click_on_Exit_Button")
            
def Exit_Yes_Button():
    x1 = pixelMatchesColor( po[0]+47, po[1]+355, (168,11,16) ) #Exit_Yes_Button
    x2 = pixelMatchesColor( po[0]+47, po[1]+355, (177,13,19) ) #Exit_Yes_Button_Light
    return (x1 or x2)

def Click_on_Exit_Yes_Button():
    if Exit_Yes_Button():
        pyautogui.click( po[0]+47, po[1]+355 )
    else :
        Raise_What_is_Problem("Click_on_Exit_Yes_Button")

def Menu_Button():
    x1 = pixelMatchesColor( po[0]-399, po[1]-66, (38,44,47) ) #Menu_Button
    x2 = pixelMatchesColor( po[0]-399, po[1]-66, (78,83,97) ) #Menu_Button_Light
    return (x1 or x2)

def Click_on_Menu_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Menu_Button():
        pyautogui.click( po[0]-399, po[1]-66 )
    else :
        Vital_Signs()
        if Exit_Button():
            pyautogui.click( po[0]-399, po[1]-66 )
        else :
            Raise_What_is_Problem("Click_on_Exit_Button")

def Rebuy_Menu_Button():
    x1 = pixelMatchesColor( po[0]+513, po[1]+14, (203,0,6) ) #Rebuy_Menu_Button
    return (x1)

def Click_on_Rebuy_Menu_Button():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Rebuy_Menu_Button():
        pyautogui.click( po[0]+513, po[1]+14 )
    else :
        Vital_Signs()
        if Rebuy_Menu_Button():
            pyautogui.click( po[0]+513, po[1]+14 )
        else :
            Raise_What_is_Problem("Click_on_Rebuy_Menu_Button")

def Leave_Next_Hand_OK_Button():
    x1 = pixelMatchesColor( po[0]+108, po[1]+342, (0,83,171) ) #Leave_Next_Hand_OK_Button
    x2 = pixelMatchesColor( po[0]+108, po[1]+342, (0,95,193) ) #Leave_Next_Hand_OK_Button_Light
    return (x1 or x2)

def Click_on_Leave_Next_Hand_OK_Button():
    if Leave_Next_Hand_OK_Button() :
        pyautogui.click( po[0]+108, po[1]+342 )
    else :
        Raise_What_is_Problem("Click_on_Leave_Next_Hand_OK_Button")
    
def Buy_In_Button():
    x1 = pixelMatchesColor( po[0]+71, po[1]+448, (26,123,0) ) #Buy_In_Button
    x2 = pixelMatchesColor( po[0]+71, po[1]+448, (32,149,0) ) #Buy_In_Button_Light
    return (x1 or x2)

def Click_on_Buy_In_Button():
    if Buy_In_Button() :
        pyautogui.click( po[0]+71, po[1]+448 )
    else :
        Raise_What_is_Problem("Click_on_Buy_In_Button")   

def Buy_In_Plus_Button(): 
    x1 = pixelMatchesColor( po[0]+264, po[1]+236, (58,68,83) ) #Buy_In_Plus_Button
    x2 = pixelMatchesColor( po[0]+264, po[1]+236, (77,88,105) ) #Buy_In_Plus_Button_Light
    return (x1 or x2)

def Hold_Click_on_Buy_In_Plus_Button(): #hold left click for 10s
    if Buy_In_Plus_Button() :
        pyautogui.mouseDown(x=po[0]+264, y=po[1]+236)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Buy_In_Plus_Button() :
            pyautogui.mouseDown(x=po[0]+264, y=po[1]+236)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            Raise_What_is_Problem("Hold_Click_on_Buy_In_Plus_Button") 

def Buy_In_Minus_Button():
    x1 = pixelMatchesColor( po[0]-46, po[1]+244, (54,62,76) ) #Buy_In_Minus_Button
    x2 = pixelMatchesColor( po[0]-46, po[1]+244, (70,80,96) ) #Buy_In_Minus_Button_Light
    return (x1 or x2)

def Hold_Click_Buy_In_Minus_Button(): #hold left click for 10s
    if Buy_In_Minus_Button():
        pyautogui.mouseDown(x=po[0]-46, y=po[1]+244)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Buy_In_Minus_Button():
            pyautogui.mouseDown(x=po[0]-46, y=po[1]+244)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            Raise_What_is_Problem("Hold_Click_Buy_In_Minus_Button")

def Re_Buy_Button():
    x1 = pixelMatchesColor( po[0]+91, po[1]+430, (26,124,0) ) #Re_Buy_Button
    x2 = pixelMatchesColor( po[0]+91, po[1]+430, (32,150,0) ) #Re_Buy_Button_Light
    return (x1 or x2)

def Click_on_Re_Buy_Button():
    if Click_on_Re_Buy_Button() :
        pyautogui.click( po[0]+91, po[1]+430 )
    else :
        Raise_What_is_Problem("Click_on_Re_Buy_Button")

def Re_Buy_Plus_Button(): 
    x1 = pixelMatchesColor( po[0]+264, po[1]+254, (58,68,83) ) #Re_Buy_Plus_Button
    x2 = pixelMatchesColor( po[0]+264, po[1]+254, (77,88,105) ) #Re_Buy_Plus_Button_Light
    return (x1 or x2)

def Hold_Click_on_Re_Buy_Plus_Button(): #hold left click for 10s
    if Re_Buy_Plus_Button() :
        pyautogui.mouseDown(x=po[0]+264, y=po[1]+254)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Re_Buy_Plus_Button() :
            pyautogui.mouseDown(x=po[0]+264, y=po[1]+254)
            time.sleep(10)
            pyautogui.mouseUp()        
        else :
            Raise_What_is_Problem("Hold_Click_on_Re_Buy_Plus_Button")

def Re_Buy_Minus_Button():
    x1 = pixelMatchesColor( po[0]-46, po[1]+261, (54,62,76) ) #Re_Buy_Minus_Button
    x2 = pixelMatchesColor( po[0]-46, po[1]+261, (70,80,96) ) #Re_Buy_Minus_Button_Light
    return (x1 or x2)

def Hold_Click_on_Re_Buy_Minus_Button(): #hold left click for 10s
    if Re_Buy_Minus_Button() :
        pyautogui.mouseDown(x=po[0]-46, y=po[1]+261)
        time.sleep(10)
        pyautogui.mouseUp()
    else :
        time.sleep(0.5)
        
        if Re_Buy_Minus_Button() :
            pyautogui.mouseDown(x=po[0]-46, y=po[1]+261)
            time.sleep(10)
            pyautogui.mouseUp()
        else :
            Raise_What_is_Problem("Hold_Click_on_Re_Buy_Minus_Button")

def I_am_back_Button():
    x1 = pixelMatchesColor( po[0]+137, po[1]+608, (1,80,165) ) #I_am_back_Button
    x2 = pixelMatchesColor( po[0]+137, po[1]+608, (1,91,188) ) #I_am_back_Button_Light
    return (x1 or x2)

def Click_on_I_am_back_Button(): #this function is already satisfied in vital signs
    global Check_Mod
    pyautogui.click( po[0]+137, po[1]+608 )
    Check_Mod = True
    


# 2017: -----------------------------

def fold():
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return Click_on_Fold_Button()

def check():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return Click_on_Check_Button()

def call():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    return Click_on_Call_Button()


def Raise( Blinds ):
    """ if Blinds == 2 (or less): won't click on plus button """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    Number_of_Clicks_on_Plus_Button( Blinds - 2 )
    return  Click_on_Raise_Button()

def bet( Blinds ):
    """ if Blinds == 1 (or less): won't click on plus button """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    Number_of_Clicks_on_Plus_Button( Blinds - 1 )
    return Click_on_Bet_Button()

def all_in( Minus_Blinds ):
    """ if 0 : all_in everything """
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Minus_Blinds == 0 :
        Click_on_All_In_Button()
        if Bet_Button() == True :
            return Click_on_Bet_Button()
        else :
            return Click_on_Raise_Button()
    else :
        Click_on_All_In_Button()
        Number_of_Click_on_Minus_Button( Minus_Blinds )
        if Bet_Button() == True :
            return Click_on_Bet_Button()
        else :
            return Click_on_Raise_Button()

def check_fold():
    global Check_Mod , Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    if Check_Button() :
        Click_on_Check_Button()
    elif Fold_Button() :
        Click_on_Fold_Button()
    else :
        Check_Mod = True #It's already True
        Vital_Signs()
        if Check_Button() :
            Click_on_Check_Button()
        elif Fold_Button() :
            Click_on_Fold_Button()        








# 2017: Neutralized due to import in main code (There is no need for Vital signs of below):

"""

#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------

import pyautogui, time
# OCR_My_Name(My_Seat_Number)
My_Profile_Name = "Canary7"
My_Seat_Number = 4#None
Lost_Connection_Time = {} #at the first line of the code!!

def getpo_for_starting(): #when i am watching the game myself, raise the Exeption 
    global po
    
    po=pyautogui.locateOnScreen('mainpic.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic.png')
        if po_new is None:
            Screenshot_Error("Could not find game on screen") #Type_of_Error in string
            raise Exception('Could not find game on screen. Is the game visible?')
        po=( po_new[0]+329 , po_new[1]-258 )


def getpo():
    global po
    
    po=pyautogui.locateOnScreen('mainpic.png')
    if po==None:
        po_new=pyautogui.locateOnScreen('Alternative main pic.png')
        if po_new == None:
            return None

###########

from PIL import Image
from pytesseract import image_to_string
import pyautogui
from pyautogui import pixelMatchesColor

def Win_Finish_Others(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+419, po[1]+412, (249,126,8) ) #Win-Finish-Others-seat-1
    if Seat==2:
        return pixelMatchesColor( po[0]+164, po[1]+411, (249,127,8) ) #Win-Finish-Others-seat-2
    if Seat==3:
        return pixelMatchesColor( po[0]-91, po[1]+419, (248,123,9) ) #Win-Finish-Others-seat-3
    if Seat==4:
        return pixelMatchesColor( po[0]-121, po[1]+112, (248,124,9) ) #Win-Finish-Others-seat-4
    if Seat==5:
        return pixelMatchesColor( po[0]+449, po[1]+112, (248,124,9) ) #Win-Finish-Others-seat-5

def Win_Finish_Me(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+442, po[1]+415, (248,125,9) ) #Win-Finish-Me-seat-1
    if Seat==2:
        return pixelMatchesColor( po[0]+187, po[1]+422, (248,123,10) ) #Win-Finish-Me-seat-2
    if Seat==3:
        return pixelMatchesColor( po[0]-68, po[1]+415, (248,125,9) ) #Win-Finish-Me-seat-3
    if Seat==4:
        return pixelMatchesColor( po[0]-98, po[1]+95, (250,130,6) ) #Win-Finish-Me-seat-4
    if Seat==5:
        return pixelMatchesColor( po[0]+472, po[1]+95, (250,130,6) ) #Win-Finish-Me-seat-5

def Gray_Sign_Seat(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+291, po[1]+348, (62,72,86) ) #Gray_Sign_Me_seat_1
        x2 = pixelMatchesColor( po[0]+315, po[1]+351, (61,70,85) ) #Gray_Sign_Other_seat_1
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+36, po[1]+351, (61,70,85) ) #Gray_Sign_Me_seat_2
        x2 = pixelMatchesColor( po[0]+60, po[1]+353, (61,71,86) ) #Gray_Sign_Other_seat_2
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-219, po[1]+348, (62,72,86) ) #Gray_Sign_Me_seat_3
        x2 = pixelMatchesColor( po[0]-195, po[1]+351, (61,70,85) ) #Gray_Sign_Other_seat_3
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-249, po[1]+43, (62,72,87) ) #Gray_Sign_Me_seat_4
        x2 = pixelMatchesColor( po[0]-225, po[1]+46, (61,70,85) ) #Gray_Sign_Other_seat_4
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+321, po[1]+43, (62,72,87) ) #Gray_Sign_Me_seat_5
        x2 = pixelMatchesColor( po[0]+345, po[1]+46, (61,70,85) ) #Gray_Sign_Other_seat_5
        return (x1 or x2)
    

def OCR(x,y,h,w):
    im=pyautogui.screenshot(region=(x, y , h, w) )
    ratio=5
    im=im.resize((im.size[0]*ratio,im.size[1]*ratio) ,Image.ANTIALIAS)
    return image_to_string( im )


def OCR_My_Name_String(Seat_Num):
    if Seat_Num == 1 :
        return OCR(po[0]+298,po[1]+363,140,16)  #seat1_Me_Name
    if Seat_Num == 2 :
        return OCR(po[0]+43,po[1]+366,140,16)  #seat2_Me_Name
    if Seat_Num == 3 :
        return OCR(po[0]-212,po[1]+363,140,16)  #seat3_Me_Name    
    if Seat_Num == 4 :
        return OCR(po[0]-243,po[1]+58,140,16)  #seat4_Me_Name
    if Seat_Num == 5 :
        return OCR(po[0]+328,po[1]+58,140,16)  #seat5_Me_Name

def OCR_My_Name(Seat_Num):
    x1 = Win_Finish_Me(Seat_Num)
    y1 = Gray_Sign_Seat(Seat_Num)
    string = OCR_My_Name_String(Seat_Num)
    x2 = Win_Finish_Me(Seat_Num)
    y2 = Gray_Sign_Seat(Seat_Num)
    if ( x1 or y1 or x2 or y2 ):
        while ( x1 or y1 or x2 or y2 ):
            x1 = Win_Finish_Me(Seat_Num)
            y1 = Gray_Sign_Seat(Seat_Num)
            x2 = Win_Finish_Me(Seat_Num)
            y2 = Gray_Sign_Seat(Seat_Num)
        return OCR_My_Name_String(Seat_Num)
    else :
        return string

#############

def Available_Seat(Number):
    if Number == 1 :
        x1 = pixelMatchesColor( po[0]+362, po[1]+408, (1,79,164) ) #Seat1
        x2 = pixelMatchesColor( po[0]+362, po[1]+408, (21,102,189) ) #Seat1_Light
        return (x1 or x2)
    if Number == 2 :
        x1 = pixelMatchesColor( po[0]+107, po[1]+411, (1,78,163) ) #Seat2
        x2 = pixelMatchesColor( po[0]+107, po[1]+411, (21,101,188) ) #Seat2_Light
        return (x1 or x2)
    if Number == 3 :
        x1 = pixelMatchesColor( po[0]-148, po[1]+408, (1,79,164) ) #Seat3
        x2 = pixelMatchesColor( po[0]-148, po[1]+408, (21,102,189) ) #Seat3_Light
        return (x1 or x2)
    if Number == 4 :
        x1 = pixelMatchesColor( po[0]-178, po[1]+103, (1,79,164) ) #Seat4
        x2 = pixelMatchesColor( po[0]-178, po[1]+103, (21,102,189) ) #Seat4_Light
        return (x1 or x2)
    if Number == 5 :
        x1 = pixelMatchesColor( po[0]+392, po[1]+103, (1,79,164) ) #Seat5
        x2 = pixelMatchesColor( po[0]+392, po[1]+103, (21,102,189) ) #Seat5_Light
        return (x1 or x2)

def Click_on_Available_Seat(Number):
    if Number == 1 :
        pyautogui.click( po[0]+362, po[1]+408 ) #Seat1
    if Number == 2 :
        pyautogui.click( po[0]+107, po[1]+411 ) #Seat2
    if Number == 3 :
        pyautogui.click( po[0]-148, po[1]+408 ) #Seat3
    if Number == 4 :
        pyautogui.click( po[0]-178, po[1]+103 ) #Seat4
    if Number == 5 :
        pyautogui.click( po[0]+392, po[1]+103 ) #Seat5

def Click_on_Exit_Button(): #this should be compeleted at futurefor Sit_In!!!!!!!!!!!!!!!!!!!!!  (maybe should be compeleted, maybe not)
    pyautogui.click( po[0]+378, po[1]+21 )

def Sit_In(Chips): # "Min buy in" or "Max buy in"
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    My_Seat_Number = None
    for i in range(1 ,6 ):
        if Available_Seat(i) == True :
            Click_on_Available_Seat(i)
            My_Seat_Number = i
            break
    if My_Seat_Number == None :
        Click_on_Exit_Button()
    else :
        x1 = time.time()
        time1 = 0
        Buy_In = None
        while ( (time1 < 5) and Buy_In !=True ):
            Buy_In = Buy_In_Button()
            x2 = time.time()
            time1 = x2-x1
        if Buy_In != True :
            Raise_What_is_Problem("Sit_In Buy_In_Button")
        if (Chips == "Min buy in" and My_Seat_Number != None) :
            Hold_Click_Buy_In_Minus_Button()
        if (Chips == "Max buy in" and My_Seat_Number != None):
            Hold_Click_on_Buy_In_Plus_Button()
        if My_Seat_Number != None :
            Click_on_Buy_In_Button()
            Just_Seated = True


def I_am_back_Button():
    x1 = pixelMatchesColor( po[0]+137, po[1]+608, (1,80,165) ) #I_am_back_Button
    x2 = pixelMatchesColor( po[0]+137, po[1]+608, (1,91,188) ) #I_am_back_Button_Light
    return (x1 or x2)

def Click_on_I_am_back_Button():
    pyautogui.click( po[0]+137, po[1]+608 )

def Check_I_am_In_or_Out():
    global My_Seat_Number , My_Profile_Name
    if I_am_back_Button() == True :
        Click_on_I_am_back_Button()
    if OCR_My_Name(My_Seat_Number) == My_Profile_Name :
        return ("In")
    else :
        return ("Out")
        
   
def Vital_Signs(): #if getpo() == None or ...
    global Lost_Connection_Time , My_Seat_Number , My_Profile_Name , Just_Seated
    
    Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
    if Lost_Connection == True :
        x1 = time.time()
        while ( Lost_Connection == True  ):
            Lost_Connection=pyautogui.locateOnScreen('Lost_Connection.png')
        x2 = time.time()
        Lost_Connection_Time[x1]= x2-x1 

    pyautogui.click(0, 720) # click to Exit probable Advertisement

    getpo_for_starting() #if None,it will raise the Exeption 
    if I_am_back_Button() == True :
        Click_on_I_am_back_Button()

    if Check_I_am_In_or_Out() == "Out":
        Sit_In("Min buy in")

#if (buttoms are still not visible after vital signs).... : #My pixel matching were wrong somewhere
#    t = time.time()
#    pyautogui.screenshot( 'Error %s.png' %t )
#    raise Exception('what was the probelm on %s?' %t ) 
        
def Screenshot_Error(Type_of_Error): #Type_of_Error in string
    t = time.time()
    pyautogui.screenshot( 'Error %s %s.png' %(Type_of_Error,t) )

def Raise_What_is_Problem(string):
    Screenshot_Error( 'What is the Problem (%s)' %string )
    raise Exception('What is the Problem?')

def Cards(Seat):
    if Seat==1:
        return pixelMatchesColor( po[0]+330, po[1]+331, (154,7,13) ) #Cards_seat_1
    if Seat==2:
        return pixelMatchesColor( po[0]+74, po[1]+332, (154,7,13) ) #Cards_seat_2
    if Seat==3:
        return pixelMatchesColor( po[0]-181, po[1]+331, (154,7,13) ) #Cards_seat_3
    if Seat==4:
        return pixelMatchesColor( po[0]-140, po[1]+212, (154,7,13) ) #Cards_seat_4
    if Seat==5:
        return pixelMatchesColor( po[0]+359, po[1]+212, (154,7,13) ) #Cards_seat_5  

"""
