import ampule, socketpool, wifi
from board import GP0, GP1, GP2, GP3, GP15
from digitalio import DigitalInOut, Direction

in1 = DigitalInOut(GP0)
in1.direction = Direction.OUTPUT

in2 = DigitalInOut(GP1)
in2.direction = Direction.OUTPUT

in3 = DigitalInOut(GP2)
in3.direction = Direction.OUTPUT

in4 = DigitalInOut(GP3)
in4.direction = Direction.OUTPUT

eye = DigitalInOut(GP15)
eye.direction = Direction.OUTPUT

def static_file():
    with open('index.html', "r") as local_file:
        content = local_file.read()
    return content

@ampule.route("/home")
def index(request):
    return (200, {}, static_file())

@ampule.route("/forward")
def forward(request):
    in1.value = False
    in2.value = True
    in3.value = False
    in4.value = True
    return (200, {}, static_file())

@ampule.route("/backward")
def backward(request):
    in1.value = True
    in2.value = False
    in3.value = True
    in4.value = False
    return (200, {}, static_file())

@ampule.route("/stop")
def stop(request):
    in1.value = False
    in2.value = False
    in3.value = False
    in4.value = False
    return (200, {}, static_file())

@ampule.route("/left")
def left(request):
    in1.value = False
    in2.value = True
    in3.value = True
    in4.value = False
    return (200, {}, static_file())

@ampule.route("/right")
def right(request):
    in1.value = True
    in2.value = False
    in3.value = False
    in4.value = True
    return (200, {}, static_file())

@ampule.route("/on")
def on(request):
    eye.value = True
    return (200, {}, static_file())

@ampule.route("/off")
def off(request):
    eye.value = False
    return (200, {}, static_file())

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets not found in secrets.py")
    raise

try:
    print("Connecting to %s..." % secrets["ssid"])
    print("MAC: ", [hex(i) for i in wifi.radio.mac_address])
    wifi.radio.connect(secrets["ssid"], secrets["password"])
except:
    print("Error connecting to WiFi")
    raise

pool = socketpool.SocketPool(wifi.radio)
socket = pool.socket()
socket.bind(['0.0.0.0', 80])
socket.listen(1)
socket.setblocking(True)
print("Connected to %s, IPv4 Addr: " % secrets["ssid"], wifi.radio.ipv4_address)

while True:
    ampule.listen(socket)
