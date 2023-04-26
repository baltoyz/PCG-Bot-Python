import psutil
import os
import time
while True:
  main_running = False
  for process in psutil.process_iter():
    try:
      process_name = process.name()
      if process_name == "python" and "main.py" in process.cmdline():
        main_running = True
        break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass

  if not main_running:
    os.system("python main.py")

  # Tempo de espera para verificar novamente se o main.py está em execução
  time.sleep(5)
