#!/usr/bin/python3
import sys
import socket
import time

def solve_round(round, sock):
    res = sock.recv(1024).decode().strip()

    # Get range
    rng = res[res.find('between'):]
    rng = rng[rng.find('[')+1:rng.find(']')].split(',')
    min = int(rng[0].strip())
    max = int(rng[1].strip())

    # Get chances
    chances = int(res[res.find("with"):].split()[1])

    print("=" * 10)
    print("Round: " + str(round+1))
    print("Range: [" + str(min) + ", " + str(max) + "]")
    print("Chances: " + str(chances))

    # Initial values
    win = 2
    inf = 2
    sup = inf + win
    near = False

    for chance in range(chances):
        print("[Q("+str(chance+1)+"/"+str(chances)+")] "+str(inf)+" "+str(sup)+": ", end='')
        sock.send(('q ' + str(inf) +' '+ str(sup)).encode())
        time.sleep(1.5)
        res = sock.recv(1024).decode().strip()
        try:
            aux = res.split('\n')[0]
            ans = int(aux[len(aux)-1])
            print(ans)

            if win == 1 and ans == 1:
                print("[A] "+str(sup))
                sock.send(("a "+str(sup)).encode())
                time.sleep(1.5)
                break
            if win == 1 and ans == 0:
                print("[A] "+str(sup+1))
                sock.send(("a "+str(sup+1)).encode())
                time.sleep(1.5)
                break
            elif ans == 0 and not near:
                win = win * 2 
                inf = sup
                sup = inf + win
                if sup > max:
                    sup = max
            elif ans == 0 and near:
                win = int(win/2)
                inf = sup
                sup = inf + win
            elif ans == 1:
                near = True
                win = int(win / 2)
                sup = inf + win

        except:
            print("\n[!] " + res)
            break


if __name__ == '__main__':
    # Setup
    host = "142.93.113.55"
    port = 31086

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.recv(8192).decode().strip()

    sock.send('start'.encode())
    time.sleep(1.5)

    for round in range(10):
        solve_round(round, sock)

    res = sock.recv(8192).decode().strip()
    print(res)
    print("Connection closed.")
    sock.close()
