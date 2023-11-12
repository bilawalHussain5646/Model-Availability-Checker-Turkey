import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import tkinter.font as tkFont
import threading
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# def InfiniteScrolling(driver):
#         last_height = driver.execute_script("return document.body.scrollHeight")
#         while True:
#             # Scroll down to bottom
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#             # Wait to load page
#             time.sleep(4)

#             # Calculate new scroll height and compare with last scroll height
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height



def Teknosa_Web(driver,list_of_categories,data,Sharaf_DG):
        output_df = pd.DataFrame(columns=['Model','Teknosa'])
        check_once = 0
        model_ids :list = []
        product_links: list = []
        for cate in list_of_categories:
            df = data[data['Category'] == cate]
            # print(df)
            list_of_models = df["Models"]
            # We got the models of one category
           
            for models in list_of_models:
                # if check_once == 0:
                print("Model: ",models)
                df_link = Sharaf_DG[Sharaf_DG['Category'] == cate]
                keyword = models
                # print(df_link["Links"])
                dyno_link = df_link["Links"].iloc[0]
                # print(dyno_link)
        
                
                # driver.get("https://www.teknosa.com/lg-televizyon-ses-goruntu-sistemleri-bc-101")
                # # Get scroll height
                # InfiniteScrolling(driver)
                
                driver.get(dyno_link)
                # time.sleep(5)
                time.sleep(5)
                ids = driver.find_element(By.CSS_SELECTOR,".products")
                all_divs  = ids.find_elements(By.CSS_SELECTOR, ".prd")

                print(len(all_divs))
                
                while len(all_divs) < 100:
                    try:
                        # btn_next = driver.find_element(By.CSS_SELECTOR,".plp-paging-current-btn")
                        # label_BtnNext=driver.find_element(By.CSS_SELECTOR,".seo.plp-seo.seo-more.container-max-700")
                        # driver.execute_script("arguments[0].scrollIntoView();", label_BtnNext)
                        # Click the element
                        # action = ActionChains(driver)
                        # for i in range(0,3):
                        #     action.send_keys(Keys.UP).perform() 
                        # time.sleep(5)
                        driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-extra.plp-paging-load-more>span"))))
                        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-extra.plp-paging-load-more>span"))))
                        # action.move_to_element(btn_next).click().perform()
#                            driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-controls='skill-categories-expanded' and @data-control-name='skill_details']/span[normalize-space()='Show more']"))))
# driver.execute_scipt("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-controls='skill-categories-expanded' and @data-control-name='skill_details']/span[normalize-space()='Show more']"))))
                        print("Clicked button")
                        time.sleep(5)
                        # element.click()
                        ids = driver.find_element(By.CSS_SELECTOR,".products")
                        all_divs  = ids.find_elements(By.CSS_SELECTOR, ".prd")
                    except:
                        print("Its breaking")
                        time.sleep(15)
                        break
                    ids = driver.find_element(By.CSS_SELECTOR,".products")
                    all_divs  = ids.find_elements(By.CSS_SELECTOR, ".prd")
                    # print(len(all_divs))
                counter = 0
                # print(len(all_divs))
                # Compare product name with model name 
                for div in all_divs:
                    prod_link = div.find_element(By.CSS_SELECTOR,".prd-link").get_attribute("href")
                    title = div.find_element(By.CSS_SELECTOR,".prd-title.prd-title-style")
                    model_id = title.text
                   
                    print(model_id)
                    check_once = 1
                    product_links.append(prod_link)
                    model_ids.append(model_id)


                print(model_ids)
           
                total_models = len(model_ids)
                counter = 0
                prod_i = 0 
                for each_model in model_ids: 
                    
                    if each_model.upper().find(models) != -1:
                        output_df = output_df.append({
                                "Model":models,
                                "Teknosa": "o",
                                "Product Link": product_links[prod_i]
                        },ignore_index=True)
                        print(models,"Found")
                        break
                    counter+=1
                    prod_i+=1

                if counter == total_models:
                    output_df = output_df.append({
                            "Model":models,
                            "Teknosa": "x",
                            "Product Link": ""
      
                    },ignore_index=True)
                    print(models,"Not Found")
                
                # Compare here now

        with pd.ExcelWriter("output.xlsx",mode="a",if_sheet_exists='replace') as writer:
            output_df.to_excel(writer,sheet_name="Teknosa")



def Teknosa_WebT20(driver,list_of_categories,data,Sharaf_DG):
        output_df = pd.DataFrame(columns=['Model','Teknosa'])
        for cate in list_of_categories:
            df = data[data['Category'] == cate]
            # print(df)
            list_of_models = df["Models"]
            # We got the models of one category
            check_once = 0
            for models in list_of_models:
                if check_once == 0:
                    print("Model: ",models)
                    df_link = Sharaf_DG[Sharaf_DG['Category'] == cate]
                    keyword = models
                    # print(df_link["Links"])
                    dyno_link = df_link["Links"].iloc[0]
                    # print(dyno_link)
           
                    model_ids :list = []
                    driver.get(dyno_link)
                    # # Get scroll height
                    # InfiniteScrolling(driver)
                    
                    # driver.get(dyno_link)
                    # time.sleep(5)
                    time.sleep(5)
                    ids = driver.find_element(By.CSS_SELECTOR,".products")
                    all_divs  = ids.find_elements(By.CSS_SELECTOR, ".prd")
    
                    print(len(all_divs))
                    
                    while len(all_divs) < 20:
                        try:
                            btn_next = driver.find_element(By.CSS_SELECTOR,".plp-paging-current-btn")
                            label_BtnNext=driver.find_element(By.CSS_SELECTOR,".btn.btn-extra.plp-paging-load-more")
                            driver.execute_script("arguments[0].scrollIntoView();", label_BtnNext)
                            # Click the element
                            action = ActionChains(driver)
                            for i in range(0,5):
                                action.send_keys(Keys.UP).perform() 

                            time.sleep(5)
                            
                            action.move_to_element(btn_next).click().perform()
                            
                            print("Clicked button")
                            time.sleep(10)
                            # element.click()
                            ids = driver.find_element(By.CSS_SELECTOR,".products")
                            all_divs  = ids.find_elements(By.CSS_SELECTOR, ".prd")

                        except:
                            print("Its breaking")
                            # time.sleep(15)
                            break
                        ids = driver.find_element(By.CSS_SELECTOR,".products")
                        all_divs  = ids.find_elements(By.CSS_SELECTOR, ".prd")
                        # print(len(all_divs))
                    counter = 0
                    # print(len(all_divs))
                    # Compare product name with model name 
                    x=0 
                    for div in all_divs:
                        
                        title = div.find_element(By.CSS_SELECTOR,".prd-title.prd-title-style")
                        if title.text.find("LG") != -1:
                            model_id = title.text
                            print(model_id)
                            check_once = 1
                            # Save this model id in the list and use it later 
                            # 
                            model_ids.append(model_id)
                        x+=1
                        if x>20:
                            break


                print(model_ids)
           
                total_models = len(model_ids)
                counter = 0
                for each_model in model_ids: 
                    if each_model.find(models) != -1:
                        output_df = output_df.append({
                                "Model":models,
                                "Teknosa": "O",
                                "Old Models": total_models
                        },ignore_index=True)
                        print(models,"Found")
                        break
                    counter+=1

                if counter == total_models:
                    output_df = output_df.append({
                            "Model":models,
                            "Teknosa": "X",
                            "Old Models": total_models
                    },ignore_index=True)
                    print(models,"Not Found")
                
                # Compare here now

        with pd.ExcelWriter("output.xlsx",mode="a",if_sheet_exists='replace') as writer:
            output_df.to_excel(writer,sheet_name="TeknosaTop20")


def Run_Teknosa():




    
    data = pd.read_excel("models.xlsx",sheet_name="Models")
    Sharaf_DG = pd.read_excel("models.xlsx",sheet_name="Teknosa")
    
    
    
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    list_of_categories = data["Category"].unique()

    Teknosa_Web(driver,list_of_categories,data,Sharaf_DG)
    
def Run_TeknosaT20():




    # 0------------------------------------------------------------------------------
    # df_sharaf_dg_categories_keywords = pd.read_excel("search_keywords.xlsx")
    # df_sharaf_dg_brands = pd.read_excel("input.xlsx")
    data = pd.read_excel("models.xlsx",sheet_name="Models")
    Sharaf_DG = pd.read_excel("models.xlsx",sheet_name="TeknosaTop20")
    # LULU = pd.read_excel("models.xlsx",sheet_name="LULU")
    # Jumbo = pd.read_excel("models.xlsx",sheet_name="Jumbo")
    # output_df = pd.DataFrame(columns=['Model','Sharaf_DG'])
    # print(data["Model"])
    
    # print(data["Category"].unique())
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    list_of_categories = data["Category"].unique()

    Teknosa_WebT20(driver,list_of_categories,data,Sharaf_DG)
   
      

# Main App 
class App:

    def __init__(self, root):
        #setting title
        root.title("Turkey Model Check")
        ft = tkFont.Font(family='Arial Narrow',size=13)
        #setting window size
        width=640
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='black')

        ClickBtnLabel=tk.Label(root)
       
      
        
        ClickBtnLabel["font"] = ft
        
        ClickBtnLabel["justify"] = "center"
        ClickBtnLabel["text"] = "Turkey Model Check"
        ClickBtnLabel["bg"] = "black"
        ClickBtnLabel["fg"] = "white"
        ClickBtnLabel.place(x=120,y=190,width=150,height=70)
    

        
        Lulu=tk.Button(root)
        Lulu["anchor"] = "center"
        Lulu["bg"] = "#009841"
        Lulu["borderwidth"] = "0px"
        
        Lulu["font"] = ft
        Lulu["fg"] = "#ffffff"
        Lulu["justify"] = "center"
        Lulu["text"] = "START"
        Lulu["relief"] = "raised"
        Lulu.place(x=375,y=190,width=150,height=70)
        Lulu["command"] = self.start_func




  

    def ClickRun(self):

        running_actions = [
            Run_Teknosa,          
            # Run_TeknosaT20,          
           
        ]

        thread_list = [threading.Thread(target=func) for func in running_actions]

        # start all the threads
        for thread in thread_list:
            thread.start()

        # wait for all the threads to complete
        for thread in thread_list:
            thread.join()
    
    def start_func(self):
        thread = threading.Thread(target=self.ClickRun)
        thread.start()

    
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# Run()



