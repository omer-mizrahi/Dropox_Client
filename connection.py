import socket, pickle

# like const variable
PATH_ROOT = lambda: 'c:\\'
DOWNLOAD_PATH = lambda: 'c:\\temp\\'

def send(data_for_send):
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 3322  # The port used by the server
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            # send data to server
            s.sendall(pickle.dumps(data_for_send))

            # recived data from server
            data = s.recv(100000)
            # data = []
            # while True:
            #     packet = s.recv(40960)
            #     if not packet: break
            #     data.append(packet)
            # res = pickle.loads(b"".join(data))
            res = pickle.loads(data)
            return res
    except Exception as e:
        err = f"Error with the server:", e
        print(err)
        raise ConnectionError(err)


def send_command():
    position = PATH_ROOT()
    while (True):
        try:
            cmd = input(f"{position}>")
            if (cmd == "cd.." or cmd == "cd .."):
                res = send((cmd, position))
                position = res.position

            elif (cmd.startswith("cd ")):
                res = send((cmd, position))
                if (res.valid):
                    position = res.position
                else:
                    print(res.messages[0])

            elif (cmd == "dir" or cmd == "dirlist"):
                res = send((cmd, position))
                print(res.messages[0] if res.messages else "")

            elif (cmd.startswith("download ")):
                res = send((cmd, position))
                print('Downloading file begins...')
                file_name=DOWNLOAD_PATH()+cmd.split("download ")[1]
                # TODO: check if file is exist and make different name
                with open(file_name, "wb") as out_file:
                    out_file.write(res.messages[0])
                print('File download successfully completed.')

            elif (cmd == "exit"):
                break

            else:
                raise KeyError(f"{cmd} is not recognized as a command.")

        except ConnectionError as e:
            print(e)
        except Exception as e:
            print(e)

send_command()
