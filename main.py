import subprocess
import os
import time


def read_line(path):
    file = open(path, 'r')
    data = file.readline()
    while data:
        yield data
        data = file.readline()
    file.close()


def brute_force(word_file, cmd):
    num_lines = sum(1 for line in read_line(word_file))
    for i, v in enumerate(read_line(word_file)):
        output = "%d / %d" % (num_lines, i)
        print(output, end='\r')
        try:
            tmp = str(v)
            tmp = tmp.replace("\n", "")
            cmd[4] = tmp
            lines = subprocess.check_output(cmd, stderr=os.devnull)
        except:
            pass
        else:
            password = str(v)
            print()
            return password
    print()
    return None


def main():
    word_file = 'password list.txt'  # file to read passwords
    path = "t.7z"  # file to brute force
    cmd = ['7z', 'x', path, '-p', '']  # command
    # ERROR_MSG = 'Wrong password?'
    password = brute_force(word_file, cmd)
    if password:
        print(password)
    else:
        print(";(")

if __name__ == '__main__':
    main()
