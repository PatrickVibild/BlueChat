import bluetooth
import traceback

app_port = 5577


class BlueChatter:
    @staticmethod
    def send_message(text: str, mac: str):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((mac, app_port))

        print('connecting to another pair')
        try:
            sock.send(text)
        except:
            traceback.print_exc()
        finally:
            sock.close()
