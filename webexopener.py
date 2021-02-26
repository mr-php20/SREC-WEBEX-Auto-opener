from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime

#Getting Day and Time
day = int(datetime.datetime.now().weekday())
hr = int(datetime.datetime.now().strftime("%H"))
mins = int(datetime.datetime.now().strftime("%M"))
print(day,hr,mins)

#if No URL FOUND
url="https://github.com/mr-php20"

#Creating new driver with webex extension
options = webdriver.ChromeOptions()
options.add_extension('D:\@College\Python programming\Python\webexcrx.crx')
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")

#user Details
usrName='Arivalan C P'
mail='arivalan.1801011@srec.ac.in'

#Finding the right URL for the Day and time
if day == 0:
    MCT= 'https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t56809d0b737543a890f57504a79882a5'
    AIML='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=td94a68ddb6c846ac9582e01d5d9d5c68'
    IOTLAB='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tc8da1964364245a09298ab83d5a0b26b'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=MCT
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=AIML
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins < 45):
        url=IOTLAB

elif day == 1:
    IOT='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tc04d935f3ee4452aa357a8df79dc4448'
    MCT='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t7ba920de6dfd46978f48a400c05c9442'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=IOT
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=MCT

elif day == 2:
    DS='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t9e14d79f4bdd4009972bc12c71a6eede'
    ENG='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t18d88e5ff8674838b20d9165c9265247'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=DS
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins < 45):
        url=ENG
        usrName='1801011 Arivalan C P'

elif day == 3:
    DSLAB='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t6076d6e1294f4a9eaace43b7f4ae00be'
    UX='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t60683628af324085aef369a3a93aa0f9'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=DSLAB
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=UX

elif day == 4:
    UX='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=ta8e1c55df7874373905efa5e08cf6fe5'
    IOT='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tcd15171bd8624cea9910c6a56748ba7c'
    ENG='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t18d88e5ff8674838b20d9165c9265247'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins <= 45):
        url=UX
    elif (hr == 10 and mins > 55) or (hr == 11) or (hr == 12 and mins <= 45):
        url=IOT
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins <= 45):
        url=ENG
        usrName='1801011 Arivalan C P'

elif day == 5:
    AIML='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tacc9348ac70e47988b32c6ca4e285dd0'
    DS='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t357155d444704b608a23307d59eba4dc'
    MCTLAB='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t8b06da59e9db4b77a5d88a2b09daecb4'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=AIML
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=DS
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins < 45):
        url=MCTLAB

#Opening Browser and Getting URL
browser = webdriver.Chrome(options=options)
browser.get(url)
time.sleep(2)

#Filling Details and Entering
if url != 'https://github.com/mr-php20':
    actions = ActionChains(browser)
    actions.move_to_element_with_offset(browser.find_element_by_xpath('/html'), 0,0)
    actions.move_by_offset(1070, 270).click()
    actions.send_keys(usrName)
    actions.move_to_element_with_offset(browser.find_element_by_xpath('/html'), 0,0)
    actions.move_by_offset(1070, 295).click()
    actions.send_keys(mail)
    time.sleep(3)
    actions.move_to_element_with_offset(browser.find_element_by_xpath('/html'), 0,0)
    actions.move_by_offset(1070, 360).click().perform()
    time.sleep(5)
    browser.quit()
