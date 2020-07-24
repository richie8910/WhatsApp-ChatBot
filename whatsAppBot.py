from selenium import webdriver
from time import sleep
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")

#name = input('Enter the name of user or group : ')

#filepath = input('Enter your filepath (images/video): ')

input('Enter anything after scanning QR code')
#imma try to print the contacts
meta_info_list = []


name = " "
process = True

#Starting the process, a while loop waits for someone to initiate a process, ie by texting Hello Jane
run = False
while process == True:
    contact = driver.find_elements_by_css_selector("span._3ko75._5h6Y_._3Whw5")
    cnt = [contacts.text for contacts in contact]    
    #This checks for the newest message
    if cnt[1] == "Hello Jane":
        name = cnt[0]
        run = True
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        if run == True:
            user.click()
            message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            message_box.send_keys('Hey! My name is Jane, your own WhatsApp personal assistant. How may I help you today?. Press 1 for a personal greeting. Press 2 to receive the Rhapsody. Press 3 to know more about me. Press 4 for a picture of my creator. Press q to quit')
            send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
            send_button.click()

        while run == True:
            msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
            msg = [message.text for message in msg_got]    
            if (msg[-1] == "Hey! My name is Jane, your own WhatsApp personal assistant. How may I help you today?. Press 1 for a personal greeting. Press 2 to receive the Rhapsody. Press 3 to know more about me. Press 4 for a picture of my creator. Press q to quit"):
                continue
            elif (msg[-1] == "1"):
                message_box.send_keys("Hello, I sure hope you are having a good day, God Bless You \n")
                continue
        #send_button.click()
            elif (msg[-1] == "2"):
                message_box.send_keys("Sends Rhapsody... \n")
                continue
        #send_button.click() 
            elif (msg[-1] == "3"):
                message_box.send_keys("I am Jane, a robot, and my creator is Mukundi Chitamba, tell me about you? \n")
                continue
        #send_button.click() 
            elif (msg[-1] == "q"):
                message_box.send_keys("Thank You! Bye! \n")    
                break
            elif (msg[-1] == "4"):
                message_box.send_keys("Here's a nice one... \n")
                attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attachment_box.click()
                image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys("C:\\Users\\12 THE GREAT\\Desktop\\Untitled Export\\mkn.jpg")  
                sleep(10)
                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click()  
                continue
            else:
        #message_box.send_keys("I don't seem to recognize that command, please try again")
                continue
    else:
        continue
print("Done")
#send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')

#send_button.click()