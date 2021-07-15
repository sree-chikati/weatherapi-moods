
# Weather Moods
[⛅️WeatherAPI Moods Website⛅️](http://weatherapi-moods.dev.schikati.me/)

A simple application that shows the user the weather of thier desired location. Upon seeing the weather, the use can enter thier mood based on the weather. 

## ✨Environment Variables✨

To run this project, you will need to add the following environment variables to your .env file

- Your own `API_KEY` from Openweathermap

  
## ❄️Run Locally❄️

> ❗️<b>IMPORTANT</b>❗️ To run locally, only ```CLONE``` the project

In a terminal window, navigate to your newly created folder and clone:
```bash
git clone git@github.com:sree-chikati/weatherapi-moods.git
```

Deploy virtual environment.
```
python3 -m venv env
source env/bin/activate
```

Run the following commands from your virtual environment to install the needed packages
```bash 
pip3 install -r requirements.txt
```

On a development server
```bash 
# run
python3 app.py
```
  
## ☀️Docker Container Local Deployment☀️

> ❗️<b>IMPORTANT</b>❗️ To run docker locally, you MUST [IMPORT this repo](https://github.com/new/import)

#### Variables and Description
| Insert Variable | Description                |
| :-------------- | :------------------------- |
| ```IMAGE NAME``` | Has to have same name as the Repo |
| ```CONTAINER NAME``` | Has to have same name as the ```IMAGE NAME``` |

First, build the image:
```bash
  docker build -t <IMAGE NAME> .
```

Then, build the container and run it on localhost::5000
```bash
  docker run -p 5000:5000 --rm --name <CONTAINER NAME> <IMAGE NAME>
```

  
## ⚡️Lessons Learned⚡️

The hardest part about this project was Dockerizing it. Since this was something we were just learning in out BEW 2.2 class, it was challange trying to build the image, then running the container locally, and making sure that the Dockerfile was ready to be run by anyone. Not only that, but once we built got our container running locally, we had to host this on our domain website using DigitalOcean and CapRover. I think I found these hard only because this is the first time we had used any of these applications. However, the more I used these applications, the more I understood it. Thus in the end it became a little easier to host my container and images on my domain by using all these platforms.

  
