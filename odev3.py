
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.by import By

class Test_Sauce_Hmw:
    #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_nousernameandpassword(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        sleep(3)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(3)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(3)
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(1000)
        
test_class=Test_Sauce_Hmw()



#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.