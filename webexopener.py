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
url="https://github.com/mr-php20/SREC-WEBEX-Auto-opener/blob/main/URL%20NOT%20FOUND"

#Creating new driver with webex extension
options = webdriver.ChromeOptions()
options.add_extension('PATH_TO_WEBEXCRX\webexcrx.crx')
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")

#user Details
usrName='NAME'
mail='example@mail.com'

#Finding the right URL for the Day and time
if day == 0:
    sub1= 'https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t56809d0b737543a890f57504a79882a5'
    sub2='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=td94a68ddb6c846ac9582e01d5d9d5c68'
    sub3='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tc8da1964364245a09298ab83d5a0b26b'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=sub1
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=sub2
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins < 45):
        url=sub3

elif day == 1:
    sub1='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tc04d935f3ee4452aa357a8df79dc4448'
    sub2='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t7ba920de6dfd46978f48a400c05c9442'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=sub1
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=sub2

elif day == 2:
    sub1='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t9e14d79f4bdd4009972bc12c71a6eede'
    sub2='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t18d88e5ff8674838b20d9165c9265247'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=sub1
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins < 45):
        url=sub2

elif day == 3:
    sub1='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t6076d6e1294f4a9eaace43b7f4ae00be'
    sub2='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t60683628af324085aef369a3a93aa0f9'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=sub1
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=sub2

elif day == 4:
    sub1='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=ta8e1c55df7874373905efa5e08cf6fe5'
    sub2='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tcd15171bd8624cea9910c6a56748ba7c'
    sub3='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t18d88e5ff8674838b20d9165c9265247'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins <= 45):
        url=sub1
    elif (hr == 10 and mins > 55) or (hr == 11) or (hr == 12 and mins <= 45):
        url=sub2
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins <= 45):
        url=sub3

elif day == 5:
    sub1='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=tacc9348ac70e47988b32c6ca4e285dd0'
    sub2='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t357155d444704b608a23307d59eba4dc'
    sub3='https://snrsrec.webex.com/snrsrec/k2/j.php?MTID=t8b06da59e9db4b77a5d88a2b09daecb4'
    if hr == 9 or (hr == 8 and mins > 55) or (hr == 10 and mins < 45):
        url=sub1
    elif (hr == 10 and mins > 55) or hr == 11 or (hr == 12 and mins < 45):
        url=sub2
    elif (hr == 13 and mins > 55) or hr == 14 or (hr == 14 and mins < 45):
        url=sub3

#Opening Browser and Getting URL
browser = webdriver.Chrome(options=options)
browser.get(url)
time.sleep(2)

#Filling Details and Entering
#As webex uses some specific frames find_element_by_xpath can't be done.
#Input fields are identified by their positions.
if url != 'https://github.com/mr-php20/SREC-WEBEX-Auto-opener/blob/main/URL%20NOT%20FOUND':
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
    time.sleep(20)
    browser.quit()
