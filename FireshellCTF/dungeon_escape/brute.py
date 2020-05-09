#!/usr/bin/python3
import sys
import socket
import time

solutions = [11]
range_max = 50
done = False
while not done:
    problem = len(solutions) + 1
    print("[*] Solving problem " + str(problem))

    for guess in range(16, range_max):
        # SETUP
        host = "142.93.113.55"
        port = 31085

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        sock.send('start'.encode())
        time.sleep(0.5)

        res = sock.recv(8192).decode().strip()

        # SOLVE ALREADY KNOWN PROBLEMS
        for solution in solutions:
            sock.send(str(solution).encode())
            time.sleep(1.5)

            res = sock.recv(1024).decode().strip()


        # TRY GUESS FOR NEW PROBLEM
        print("    [-] Trying " + str(guess))
        sock.send(str(guess).encode())
        time.sleep(1.5)

        res = sock.recv(1024).decode().strip()
        print(res)

        # CHECK IF THE GUESS WAS RIGHT
        if "again" not in res:
            print("[+] Answer to problem " + str(problem) + " is " + str(guess))            
            solutions.append(guess)
            print(res)

            # CHECK IF WE GOT THE FLAG
            if "Challenge" not in res:
                done = True

            break

        # CLOSE CONNECTION
        sock.close()
