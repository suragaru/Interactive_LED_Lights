# Flask LED Control App

<!-- Badges -->
<p>
  <a href="https://github.com/suragaru/Interactive_Bed_Lights/network/members">
    <img src="https://img.shields.io/github/forks/suragaru/Interactive_Bed_Lights" alt="forks" />
  </a>
  <a href="https://github.com/suragaru/Interactive_Bed_Lights/stargazers">
    <img src="https://img.shields.io/github/stars/suragaru/Interactive_Bed_Lights" alt="stars" />
  </a>
  <a href="https://github.com/suragaru/Interactive_Bed_Lights/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/suragaru/Interactive_Bed_Lights" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/suragaru/Interactive_Bed_Lights" alt="last update" />
  </a>
  <a href="https://github.com/suragaru/Interactive_Bed_Lights/issues/">
    <img src="https://img.shields.io/github/issues/suragaru/Interactive_Bed_Lights" alt="open issues" />
  </a>  
  <a href="https://github.com/suragaru/Interactive_Bed_Lights/blob/main/LICENSE.md">
    <img src="https://img.shields.io/github/license/suragaru/Interactive_Bed_Lights" alt="open issues" />
  </a>  
</p>

This web application allows users to control LEDs connected to a microcontroller via serial communication. The app is built using the [Flask](https://flask.palletsprojects.com/) framework and communicates with the microcontroller using the `pyserial` library.

---

## Buy me a coffee

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<!---<a href="https://www.buymeacoffee.com/igorantun" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>--->

<a href="https://ko-fi.com/suragarucoffee"> <img src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" alt="Buy Me A Coffee" height="40" width="auto"/></a>

---

## Features
- **Com Port Setup**: Set the COM port for serial communication with the microcontroller.
- **LED Control**: Turn on/off LEDs and change their colors through the web interface.


## :toolbox: Setup

## Requirements
- Python 3.8+
- [Flask](https://pypi.org/project/Flask/) library
- [pyserial](https://pypi.org/project/pyserial/) library
- Microcontroller with LEDs connected and accessible via a serial port


### Wiring

### Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/flask-led-control.git
   cd flask-led-control

2. Install dependencies:
   ```bash
   pip install Flask pyserial
   ```
   
3. Run the Application:
  ```bash
  python app.py
  ```

4. To Tunnel the server: 
- Download Clouldflare
  ```bash
  https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation<br>
  ```
  
5)Open Cmd > Go to where your cloudflare.exe at place and enter:
  ```bash
  clouldflare.exe tunnel -url localhost:80" 
  ```

<br><b>The App:</b><br><img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/theapp.png" width="500"/>

<br><b>Curcuit:</b><br><img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/curcuit.png" width="500"/>

### Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## License
>You can check out the full license [here](https://github.com/suragaru/Interactive_Bed_Lights/blob/main/LICENSE.md)

This project is licensed under the terms of the **MIT** license.










# Interactive-Bed-Light
Design for you to control your bed lights anywhere!<br>
You can modify the script to control various of lights in your room and have someone to control it for fun. <br>
Inspired by Big Bang Theory. <br>

<b>How:</b> <br>
<b>Requirements:</b> Python installed, Flask and Pyserial library.<br>
1)To setup, in led_strip.ino upload this code to arduino uno ,view the code and change the variable if you like. <br>
2)Complete the following curcuit in breadboard that connects led strips to Arduino. <br>
3) Run the app.py <br>
<br>
<b>To Tunnel the server app [this is to access the web page anywhere]:</b> <br>
4)Download Clouldflare [you can use ngrok if u like]<br>
Link: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation<br>
5)Open Cmd > Go to where ur cloudflare.exe place and enter "clouldflare.exe tunnel -url localhost:80" <br>

<br><b>The App:</b><br><img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/theapp.png" width="500"/>

<br><b>Curcuit:</b><br><img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/curcuit.png" width="500"/>
