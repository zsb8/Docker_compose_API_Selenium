# Docker_compose_API
Create an API for providing insurance price. 
Technical environment: Docker compose, FastAPI, Selenium

# docker compose file
Define the network
~~~
networks:
  api_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.1.0/24
          gateway: 192.168.1.1
~~~

Define the contain IP address
~~~
    networks:
       api_network:
         ipv4_address: 192.168.1.200
~~~
