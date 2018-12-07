
# Retrieve Weather Information

## Computer Networks project (06-88-556-1) -- Dr. Kemal Tepe

## Team Members:
## 1. Maryam Hanna , 103996154, hanna11@uwindsor.ca
## 2. Maryam Eshaghi, 104726325, eshaghim@uwindsor.ca

<img src="http://geography.name/wp-content/uploads/2016/03/Weather-1.gif" align="right"
title="Weather-1" width="140" height="240">


## Abstract

This project retrieves weather information from http://www.timeanddate.com/weather webstie and display it on the screen for the user who works with the software. It asks from the user to enter the desired country name and the city, then the system will provide the information about the weather in the requested city such as current temperature (in Celsius),  weather condition (sunny, rainy, windy, etc.). In addition, this code is designed in a way not to crash easily.


## Prerequisites

This project is written in Python3 programming language and you can run this code on any python3 compiler. 


## Running the program

When you compile the codes file, you will be asked to enter the name of the desired country, followed by the name of the desired city. The first response that is displayed is the web status. If the web status is 200, it indicates  that it was successful in finding the website, and will be successful in extracting desired information. If the web status is 404, it means that the website was not found. Other common website status include 301 (moved permanently), 400 (bad request), 401 (unauthorized), 403 (forbidden), and many more. If the webstatus is anything except 200, the code will notify you and request for you to input a new country and city for input data. Along with successful web status, then it gives you the temperature and then shows the weather condition.In the next step,  when the user got the desired result, the program ask from users what they would like to do next; the user has three options: refresh, restart, or quit. If the user inputs refresh, it will give refreshed data of the  temperature of the same city. If the user inputs restart, they will be able to input a new location they want to the temperature for. If the user inputs quit, the program will be ended.


## Extraction of Data from Website

Most websites are written in html format. Through functions provided from libraries like BeautifulSoup, the server sents us html document of the website. "Developer Tools"(Chrome) or "DevTools"(Firefox and Safari) allows for us to view the current html of a website in a browser. The html document is full of tags like 'div', 'p', 'snap', etc.; each with their own disctinct meaning and usage. In addition to tags, each tag has a unique title, which makes it easier to naviage and find a specific one. Shown below is the specific tag and title used for this project to retrieve the desired data. In the div tag called h2 contains the tepmerature and in the next p tag contains the weather condition. 

```html
    <div class="h2">7&nbsp;°C</div> 
    <p>Mostly cloudy.</p>
```
        
## Code Explanation

The following libraries are utilized in this program to be able to access HTML skeleton of the websites: "requests -- get", "bs4 -- BeautifulSoup", and "requests". BeautifulSoup library is python library which is used to extract the data of HTML and XML files. The library requests is made specifically HTTP1.1 protocols, allowing us to attain data from the site. 
  
```python
    from requests import get
    from bs4 import BeautifulSoup
    import requests
```    
    
A quick trace through the program is as follows below. 

Initiallized is the "quit_flag" which is set to 0 (false). The code enters a while loop, which loops while "quit_flag" is set to 0. Then initiallized is the "restart_flag" which is set to 0. the url is attained from 'main_code()' defined function. The program will enter second while loop, which loops while "restart_flag" is set to 0. Using 'get_tem()' defined function which takes url as the input data, the program will get the data, which is a table of two strings. The first string of data is the current temperature and the second string is the weather conditions; which is printed. Later the 'refresh_flag' is set to 0, and the program enters a third while loop; that loops as long as 'refresh_flag' is set to 0. The program will then ask the user to input what they want to happen next (refresh, restart, quit); which is inputed using input() function that is buildin python. Depending on the user's input, the program will go through a set of if statements. If the user inputs 'refresh', the 'refresh_flag' will be set to 1 to exit the third while loop; this allows the program to run through the second while loop again, and attaining fresh set of data about the same city, and entering the third loop again. If the user inputs 'restart', the 'refresh_flag' and the 'restart_flag' will be set to 1 to exit the second and third while loops; which allows for the user to input a new country and city and attain their data, by going into the second and third loop again. Finally, if the user inputs 'quit', all three flags, 'quit_flag', 'restart_flag', and 'refresh_flag', will be set to 1 to exit all three while loops; which will completely end the program.   

```python
    quit_flag = 0
    while quit_flag == 0:
        restart_flag = 0
        url = main_code()
        while restart_flag == 0:
            data = get_temp(url)
            print ("\ncurrent temperature: ", data[0])
            print ("\nweather conditions: ", data[1])
            refresh_flag = 0
            while refresh_flag == 0:
                user_input = input('\nPlease type what next (refresh, restart, quit): ')
                if user_input == 'refresh':
                    refresh_flag = 1
                elif user_input == 'restart':
                    restart_flag = 1
                    refresh_flag = 1
                elif user_input == 'quit' :
                    quit_flag = 1
                    restart_flag = 1
                    refresh_flag = 1 
```
     
The next defined function which is used 'main_code()'. Its has no input and its output string URL. This function calls 'input_cc()' defined function to attain location the user wants the data from. The setup URL is from www.timeanddate.com website; provided data like weather and time of cities all over the world. It covers most cities, but not all. In addition, in this function, it will attain the url status code using 'head().status_code' which is provided from requests library. The code will display status code to the user, incase there is an error, the user could understand what it is. Usind a while loop, of when response is not 200, it will print error statement, and ask the user to input a new location. This while loop prevents the program from crashing from an unstable site. This function and the scripts to execute this function are as follows:
    
```python
    def main_code():
    location = input_cc()
    url = 'https://www.timeanddate.com/weather/' + location
    response = requests.head(url).status_code
    print('\nweb status:', response)
    while response != 200:
        print('Error, please input country and city again')
        location = input_cc()
        url = 'https://www.timeanddate.com/weather/' + location
        response = requests.head(url).status_code
        print('\nweb status:', response)
    return url
```
    
The following defined function is 'input_cc()'. It has no inputs, and it outputs a string named location. The 'input()' is a python buildin function and is used to allow the user to input the name of the country and the city. Buildin python functions 'lstrip()', 'lower()', rstrip()' are used to make the input be all lower cased and remove any leading or following spaces from the user's input. This way, the code will not be crash bye entering the names with these such a differences. This function and the scripts to execute this function are as follows:

```python
    def input_cc():
    country = input('\n\nEnter country: ')
    country = country.lstrip().lower().rstrip()
    city = input('Enter city: ')
    city = city.lstrip().lower().rstrip()
    location = str(country) + "/" + str(city)
    print(location)
    return location
``` 
    
The next function which is used is 'get_temp()'. It's input is a string called url, and the output is an array of strings called data. From the given URL, it attains the website's HTML text using function 'get()' from request library. The attained website will be given to function 'BeautifulSoup' with 'html.parser' to attain text html of the website. Using beautifulSoup4, it finds the "tree-branch" that contains the weather data, function called 'soup.find()'. In addition, in the same branch, it contains the weather-conditions, which it saves, using a function alled findNext(). The temperature and weather-conditions are saved into variables as a string, which is later saved into the data array.This function and the scripts to execute this function are as follows:
    
```python
    def get_temp(url):
        data = []
        web_html = get(url)
        soup = BeautifulSoup(web_html.text, 'html.parser')
        temp = soup.find('div', class_= 'h2')
        weather_condition = temp.findNext('p')
        temp = temp.text
        data.append(temp)
        weather_condition = weather_condition.text
        data.append(weather_condition)
        return data
```

     
## Application and Conclusion

The application of this project is to provide the user with weather forecast information of the a city that user wants by using packages like beautifulSoup to access the websites HTML. Through the HTML, we find keywords like "div" and "snap" where it has titles like "weather" and "forecast".


## Refrences

[1] https://www.dataquest.io/blog/web-scraping-beautifulsoup/

[2] https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3  

[3] http://docs.python-requests.org/en/master/user/quickstart/

[4] https://beautiful-soup-4.readthedocs.io/en/latest/

