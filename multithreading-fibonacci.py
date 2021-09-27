import os 
import concurrent.futures
import time
import threading
import multiprocessing

print(f"Total CPU: {os.cpu_count()}\n")

start = time.perf_counter()

def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    a = 1
    b = 1
    while True: #Looping sampai ketemu return
      if x == 0:
        return True
      elif b <= x:
        if b == x:
          return True
        else:
          temp = b
          b = b + a
          a = temp
      else:
        return False
        
threads = []
for num in range(1, 101):
  t = threading.Thread(target=find_fibonacci, args=[num])
  t.start()
  threads.append(t)
  print(find_fibonacci(num), num) #untuk show hasil exec find_fibonacci

for thread in threads:
  thread.join()

finish = time.perf_counter()
executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")