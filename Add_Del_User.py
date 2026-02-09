
import time
from itertools import count

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager

print(" NOTE:-----Captcha code should not enabled on gateway-----:)")
Name=input(" Please Enter your name-")
print(" Hi,",Name,":), I am Adi,here to assist you\n","Please select an option as given below..")
userinput = int(input(" To add user , press 1.\n To delete user from user management, Press 2.\n To create duplicate of VIA Setting Default template, Press 3."))
#num = int(input("How many user you want add?,Please Enter int number: "))
#Launch_Chrome_Browser___
#ist/new_aproach
driver=webdriver.Chrome() #to launch/invoke chrome browser.__not for all time.


#old_aproach_
#service_obj=Service("C:\chromedriver-win64\chromedriver.exe")                                                           # to launch chrome browser
#driver=webdriver.Chrome(service=service_obj)  # to launch chrome browser
driver.maximize_window()
time.sleep(2)

driver.get("https://172.30.92.111/viaIndex/index") #url_open_in_browser
#P1_Security_page
Adv=driver.find_element(By.ID,"details-button").click()                                                           #for Advance(Adv) button
time.sleep(2)

#driver.find_element(By.ID,value="details-button").click()
pro=driver.find_element(By.ID,"proceed-link").click()                                                             #click on Proceed to 172.30## (unsafe)

#P2_Welcome_TO_VIA
print(driver.find_element(By.CSS_SELECTOR,".text-light.align-middle").text)                                       #print page title
ManageGatewaySettings=driver.find_element(By.CLASS_NAME,"manageSettingCss").click()                               #to click on manage gateway settings
time.sleep(2)

#P3_Login_Page
driver.find_element(By.ID,"login_name").send_keys("su")                                                           #enter user ID
driver.find_element(By.ID,"login_password").send_keys("supass")                                                   #Enter user password
driver.find_element(By.NAME,"submit").click()                                                                     #Click on Submit button

time.sleep(5)
#p4_Dashboard_Page
driver.execute_script("window.scrollBy(0, -500);")

if userinput==1:
    #num = int(input("How many user you want add?,Please Enter int number: "))
    num=100
    time.sleep(5)
    print("Adding", num, "users is inprogress......\n It'll take sometime..,Please wait..")

    driver.find_element(By.CSS_SELECTOR,"#nav > section > section > div > nav > ul > li:nth-child(7) > a > span").click()  # Click on User management
    #driver.find_element(By.XPATH,"driver.find_element(By.XPATH, "/html/body/section/section/section/aside/section/section/div/nav/ul/li[7]/a")
    time.sleep(3)

    for i in range(1, num + 1):
        driver.find_element(By.CSS_SELECTOR,"#content > section > section > div.heading > h3 > span > button").click()  # click on Add user
        time.sleep(2)
        # driver.find_element(By.ID,"addUserModal").
        driver.find_element(By.ID, "txtUserId").send_keys(Name, ".", i)  # enter user name
        driver.find_element(By.ID, "txtPassword").send_keys("1234")  # enterpassword
        driver.find_element(By.ID, "txtConfirmPassword").send_keys("1234")  # enter confirm password
        # driver.find_element(By.ID,"adduserbtn").click()
        time.sleep(3)
        driver.find_element(By.ID, "chkAdministrator").click()  # to checked the check box of webadminstration
        # print(driver.find_element(By.ID,"chkAdministrator").is_selected())  # to know webadminstration checke box is checked or not
        # print(driver.find_element(By.XPATH, "//button[@id='adduserbtn']").text)  # to print text of button
        driver.find_element(By.XPATH, "//button[@id='adduserbtn']").click()  # to click on SAVE button
        time.sleep(3)
        count=i #save the user count
    print(count, "user Added successfully..") #print the user count

    #print("Congratulation..", count, "users succesfully added")
elif userinput==2:
    num = int(input("How many user you want delete?,Please Enter int number: "))
    print("Adding", num, "users is inprogress......\n It'll take sometime..,Please wait..")
    driver.find_element(By.CSS_SELECTOR,"body > section:nth-child(47) > section:nth-child(4) > section:nth-child(1) > aside:nth-child(1) > section:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)").click()  # Click on User management
    time.sleep(3)

    for i in range(0,num):

        count=i
        driver.find_element(By.CSS_SELECTOR,value="body > section:nth-child(47) > section:nth-child(4) > section:nth-child(1) > section:nth-child(2) > section:nth-child(2) > section:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
    print("Congratulation..",count,"user deleted successfully..")
#VIA_SETTINGS.
elif userinput==3:
    driver.find_element(By.CLASS_NAME, value="pull-right").Click()

time.sleep(50)