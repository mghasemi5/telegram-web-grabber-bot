from selenium import webdriver
import pickle
import gc
import time



while True:

    try:

        Price_list = []
        driver1 = webdriver.Chrome('chromedriver.exe')
        driver1.get('https://arzmodern.net/')
        Price_list.append(["https://arzmodern.net/", driver1.find_element_by_xpath(
            "/html/body/div[1]/section[3]/div/div/div/div[2]/div/section[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div[3]/span[2]").text.split(
            ' ')[0]])
        driver1.execute_script("window.open('about:blank', 'tab2');")
        driver1.switch_to.window('tab2')

        driver1.get('https://nobitex.ir/tether/')
        Price_list.append(["https://nobitex.ir/tether/",
                           driver1.find_element_by_xpath(
                               "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/div[2]/span[2]").text])

        driver1.execute_script("window.open('about:blank', 'tab3');")
        driver1.switch_to.window('tab3')
        driver1.get('https://tetherland.net/buy')
        Price_list.append(["https://tetherland.net/buy/", driver1.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/span").text.split(' ')[0]])

        driver1.execute_script("window.open('about:blank', 'tab4');")
        driver1.switch_to.window('tab4')
        driver1.get('https://wallex.ir/markets/usdt-tmn/')
        Price_list.append(["https://wallex.ir/markets/usdt-tmn/",
                           driver1.find_element_by_xpath(
                               '/html/body/div[1]/main/div/div[1]/table/tbody/tr/td[3]/span[1]').text])

        driver1.execute_script("window.open('about:blank', 'tab4');")
        driver1.switch_to.window('tab4')
        driver1.get('https://tabdeal.org/panel/trade/USDT_IRT')
        Price_list.append(["https://tabdeal.org/panel/trade/USDT_IRT",
                           driver1.find_element_by_xpath(
                               '/html/body/div[1]/div/div/div/main/div/div[5]/div/div/div[2]/div/div[2]/div[1]/p[2]').text])



        sum = 0
        max = 0
        min = 100000
        for i in Price_list:
            if int(i[1].split(',')[0] + i[1].split(',')[1]) > max:
                max = int(i[1].split(',')[0] + i[1].split(',')[1])

            if int(i[1].split(',')[0] + i[1].split(',')[1]) < min:
                min = int(i[1].split(',')[0] + i[1].split(',')[1])

            sum = sum + int(i[1].split(',')[0] + i[1].split(',')[1])
        Price_list.append([sum,sum])
        Price_list.append([min, min])
        Price_list.append([max,max])
        driver1.quit()
        file = 'tether_price.pkl'
        pickle_file = open(file,'wb')
        pickle.dump(Price_list,pickle_file)
        pickle_file.close()
        n = gc.collect()
        print(n , '    ', gc.garbage)
        time.sleep(20)

    except:
        driver1.quit()
        continue