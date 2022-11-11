# Docker_compose_API
Create an API for providing insurance price. 
Technical environment: Docker compose, FastAPI, Selenium

# docker compose file
## Code
Define the network as 192.168.1.x
~~~
networks:
  api_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.1.0/24
          gateway: 192.168.1.1
~~~

Define the contain IP address as 192.168.1.200
~~~
    networks:
       api_network:
         ipv4_address: 192.168.1.200
~~~

Map the local folder `/home/cert/` to the contain folder `/home/`.
~~~
    volumes:
      - '/home/cert/:/home/'
~~~

## Netwrok
![image](https://user-images.githubusercontent.com/75282285/201433414-38fd095f-0b56-4359-8302-8254c8e773ee.png)


# Connet with Selenium container
~~~
        with open("/home/config.txt", "r") as f:
            credentials = f.readline().split(" ")
        driver = webdriver.Remote(
            command_executor="http://192.168.1.100:4444/wd/hub",
            options=webdriver.FirefoxOptions()
        )
~~~


# Use this API
Input the JSON format message and POST it. For example: 
~~~
{
    "expiry_date":"2023-12-25",
    "birthday":"2011-01-01",
    "effective_date":"2023-10-20"
}
~~~

![image](https://user-images.githubusercontent.com/75282285/201432969-a170bde7-6686-4516-a6e2-efb290900954.png)
****
