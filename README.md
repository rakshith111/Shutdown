# Shutdownify

## This is an app developed for windows .You can time your pc to shutdown by setting the timer which takes in 3 entries for Hours, Minutes and Seconds

## Currently supported features

- Shuts the pc down after the given time

- If you want to cancel the set timer it can be done by clicking on the cancel button
- Once the timer is set it can be extended 
  - Two modes are available
    - Direct mode : Shuts down the pc for the chosen time immediately  
    - Manual mode : Adds the selected time to the input fields
  

<h3><details>
  <summary>BETA features </summary>
  <h4>Flask webserver which runs locally on your pc and displays an ip and Use the app to remotely control the state of your pc</h4><br>
-> install requirements.txt<br>
-> run the apihandler.py<br>
-> Open the app and input ip and press check <br>
-> If status is green you're good to go else recheck ip <br>

</details></h3>

## Upcoming features
- Updated themes
- Full Android support
  - A security feature
  - Support for simultaneous shutting down of many pc's from app
  - Add names for pcs
 
## Screenshots
![image](https://user-images.githubusercontent.com/36219488/185763136-f971e321-7396-49d1-b5d7-10b7ed8a560e.png)

![image](https://user-images.githubusercontent.com/36219488/182211949-fe9d23b4-e833-48a0-bccf-10628c8a26d3.png)

![image](https://user-images.githubusercontent.com/36219488/182211899-0e86347e-0b63-42de-a946-024b7a9d97d9.png)

### [Releases](https://github.com/rakshith111/Shutdown-timer/releases)

<h4><details>
  <summary>Build it by yourself </summary>
  <code>pip install pyinstaller </code><br>
  Then run <br>
  <code>pyinstaller --onefile -w main.py -i shutdown.ico</code> <br>

</details></h4>

## WHY? 
  I was just tooo frustrated that I didnt have a shutdown timer and couldnt trust the one's I found online so i built one<br>
  Also wanted to see how far i can strech this one simple concept by integrating many features and extend its use for many people
  


