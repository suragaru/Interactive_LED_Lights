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

This web application allows users to control LEDs connected to a microcontroller via serial communication. The app is built using the [Flask](https://flask.palletsprojects.com/) framework and communicates with the microcontroller using the `pyserial` library.<br>

<img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/theapp.png" width="500"/>

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
<img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/curcuit.png" width="500"/>

### Installation

1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/Interactive_Bed_Lights.git
   cd Interactive_Bed_Lights
   
2. Install Dependencies
   ```bash
   pip install Flask pyserial
   
3. Run the Application
   ```bash
   python app.py

5. Tunnel the Server with Cloudflare
- Download and install Cloudflare from the <a href="https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/">official guide</a>.

5. Configure Cloudflare Tunnel
- Open Command Prompt (Cmd) and navigate to the directory where cloudflare.exe is located.
- Run the following command:
  ```bash
  clouldflare.exe tunnel -url localhost:80
  ```

## Usage
Setting Up the COM Port
Navigate to the /s route or click on the setup link from the home page.
Enter the COM port number (e.g., 3 for COM3) and click "connect."

## Controlling LEDs
Once the COM port is set, you can control the LEDs:

Turn Off LED: Select "off" and submit.
Change LED Color: Select a color (e.g., "red", "green", "blue", etc.) and submit.

## File Structure
- `app.py:` The main application file containing the Flask routes and serial communication logic.
- `templates/index.html:` The HTML template for the main control interface.

### Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## License
>You can check out the full license [here](https://github.com/suragaru/Interactive_Bed_Lights/blob/main/LICENSE.md)

This project is licensed under the terms of the **MIT** license.
