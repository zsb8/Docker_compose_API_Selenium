#!/bin/bash
host="$1"
port="$2"
WaitFor () {
        while ! nc -z $1 $2;
        do
                echo "!!Wait for selenium";
                sleep 1;
        done;
}
WaitFor $host $port
echo "!!Selenium is running!";
echo "!!Start web service from here";
exec uvicorn main:app --reload --host 0.0.0.0 --port 8000
