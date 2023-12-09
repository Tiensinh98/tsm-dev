import subprocess as sp
import threading

def run_server():
    sp.run("python ./manage.py runserver", shell=True, check=True)

def run_client():
    sp.run("npm start", shell=True, check=True)

def run_build():
    sp.run("cd tsm_react_app && npm run build", shell=True, check=True)
    sp.run("python ./manage.py runserver", shell=True, check=True)


t1 = threading.Thread(target=run_build, args=(), daemon=True)
t1.start()

# t2 = threading.Thread(target=run_client, args=(), daemon=True)
# t2.start()

t1.join()
# t2.join()
print('Killed server and client!')

