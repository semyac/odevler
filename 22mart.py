from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.by import By

class Test_Sauce_Hmw:
    # Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_nousernameandpassword(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://saucedemo.com/")
        sleep(2)
       
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
       
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(10)

# testClass=Test_Sauce_Hmw()
# testClass.test_nousernameandpassword()


# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def test_nopassword(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://saucedemo.com/")
        sleep(2)
       
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
       
        usernameInput.send_keys("username")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(10)

# testClass=Test_Sauce_Hmw()
# testClass.test_nopassword()


# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_lockedoutuser(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://saucedemo.com/")
        sleep(2)
       
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
       
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(10)

# testClass=Test_Sauce_Hmw()
# testClass.test_lockedoutuser()



# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. 
# Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)

    def test_iconX(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://saucedemo.com/")
        sleep(2)
       
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
       
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        iconredX1=driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1)")
        sleep(2)
        iconredX2=driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2)")
        sleep(2)
        
        closeBtn=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        closeBtn.click()
     
        sleep(100)

# testClass=Test_Sauce_Hmw()
# testClass.test_iconX()



# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    def std_user(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://saucedemo.com/")
        sleep(2)
       
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
       
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        getUrl= driver.current_url
        if (getUrl == "https://www.saucedemo.com/inventory.html"):
            print(f"Geçerli Url /inventory.html'e eşittir. : {True}")
        else:
            print(False)

# testClass=Test_Sauce_Hmw()
# testClass.std_user()



# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def numberofproduct(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://saucedemo.com/")
        sleep(2)
        self.std_user()
        sleep(2)
        listofproduct=driver.find_elements(By.CLASS_NAME,"inventory item")
        if(listofproduct.__len__()==6):
            print(f"Ürün sayısı 6'dır. :{True}")
        
        else:
            print(f"Ürün sayısı 6'dır. :{False}")


testClass=Test_Sauce_Hmw()
testClass.numberofproduct()





