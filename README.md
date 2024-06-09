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
4)Download Clouldflare [u can use ngrok if u like]<br>
Link: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation<br>
5)Open Cmd > Go to where ur cloudflare.exe place and enter "clouldflare.exe tunnel -url localhost:80" <br>

<br><b>The App:</b><br><img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/theapp.png" width="500"/>

<br><b>Curcuit:</b><br><img src="https://github.com/mrrpickle/Interactive-Bed-Lights/blob/main/extra/curcuit.png" width="500"/>
