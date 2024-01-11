# Ampule-Pico-W-Robot
This is a Pico W controlled robot that uses the Ampule framework which is currently in Alpha.

## Getting started

Make sure to first build your robot following the wiring diagram below. The robot can have any chassis and can be modified as desired. Then make sure to install the latest CircuitPython UF2 file onto your Pico W. Then go to [this](https://github.com/deckerego/tally_circuitpy) repository and click on the ZIP file to download the required files. Then find the `ampule.mpy` file and copy it into the lib folder of your CIRCUITPY drive (this is the name of the Pico W when CircuitPython is installed). Then go to Mu and go to the serial console and type `import ampule`. If no error shows up then you are ready to go. Copy the `robot-ampule.py` code into `code.py` and then save and then run. Be sure the motor power supply is on and then go to `<ip-address-of-pico>/home` and the app should appear. It's best to use a touch screen for mobility but you can modify it for mouse control as well using `mousedown` and `mouseup` on the JavaScript code embedded in `index.html`.

![picture](https://github.com/sentairanger/Ampule-Pico-W-Robot/blob/main/pico-robot-ampule_bb.png)
