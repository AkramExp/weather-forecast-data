# Weather Forecast App



## Description
This app is used to get the information about how's weather gonna be in upcoming days upto 5 days.

The API i used in this app is from [operweathermap.org](operweathermap.org)

I made it using **Python** with **streamlit** package to make frontend web design and **plotly** package to plot a beautiful graph on the website.

The **dockerfile** in the repo can be used to build the **docker image** of the application and run.



## Run Locally

Install requirements

```bash
  pip install --no-cache-dir -r requirements.txt
```

Run the streamlit command

```bash
  streamlit run main.py
```

### Run with Docker
Build the docker image
```bash
  docker build -t weather-forecast:1.0 .
  ```

Run the Docker Image
```bash
  docker run -p 8501:8501 weather-forecast:1.0
```


## Screenshots

![Screenshot1](https://github.com/AkramExp/weather-forecast-data/blob/main/screenshots/ss1.png)

![Screenshot2](https://github.com/AkramExp/weather-forecast-data/blob/main/screenshots/ss2.png)

![Screenshot3](https://github.com/AkramExp/weather-forecast-data/blob/main/screenshots/ss3.png)

