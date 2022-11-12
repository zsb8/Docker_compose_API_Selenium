from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json


def main(expiry_date, birthday, effective_date):
        with open("/home/config.txt", "r") as f:
            credentials = f.readline().split(" ")
        driver = webdriver.Remote(
            command_executor="http://192.168.88.100:4444/wd/hub",
            options=webdriver.FirefoxOptions()
        )
        print("connected")
        web = credentials[2].strip()
        web_url_main = "https://" + web + "/user/login"
        driver.get(web_url_main)
        email = driver.find_element(By.ID, "username")
        passw = driver.find_element(By.ID, "password")
        email.send_keys(credentials[0])
        passw.send_keys(credentials[1])
        click_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/form/div[3]/div/input")
        click_button.click()
        web_url2 = "https://" + web + "/plan/add?product_short=TOP"
        driver.get(web_url2)
        csrf_test_name = driver.find_element(By.NAME, "csrf_test_name").get_attribute("value")
        cookie = driver.get_cookies()
        ci_session = cookie[1]['value']
        my_cookie = 'ci_session=' + ci_session+'; csrf_cookie_name=' + csrf_test_name
        headers = {'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'Cookie': my_cookie}
        request_url = "https://" + web + "/plan/gettoppremium"
        data = {
            "expiry_date": expiry_date,
            "birthday": birthday,
            "package": "all_inclusive",
            "effective_date": effective_date,
            "csrf_test_name": csrf_test_name
        }
        print(f"Send the post is :{data}")
        res = requests.post(url=request_url, headers=headers, data=data)
        json_res = json.loads(res.text)
        web_url_quit = "https://" + web + "/user/logout"
        driver.get(web_url_quit)
        print("Quit the website.")
        driver.quit()
        print(f"The result is :{json_res}")
        dict_result = {}
        if json_res['status'] == "Fail":
            dict_result['Result'] = "Fail"
            dict_result['Content'] = json_res
        if json_res['status'] == "OK":
            dict_result['Result'] = "Success"
            dict_result['Content'] = {'Price': float(json_res['premium'])}
            print(f"Price is : {json_res['premium']}")
        if not bool(dict_result):
            dict_result['Result'] = "Fail but don't know why"
            dict_result['Content'] = json_res
        result = dict_result
        return result


if __name__ == "__main__":
    expiry_d = '2023-12-25'
    birthday_d = '2011-01-01'
    effective_d = '2023-10-20'
    response = main(expiry_d, birthday_d, effective_d)
    print(response)
