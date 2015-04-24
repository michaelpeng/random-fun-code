import requests, threading, time

is_done = False
num_of_employees = 0

def waiting_phrase():
  global is_done
  dot_list = []
  while not is_done:
    print("Hold on, this will take a few seconds" + str(''.join(dot_list)), end='\r')
    dot_list.append('.')
    time.sleep(.1)
  print()

def print_employee_count():
  global num_of_employees
  print("Dropbox has " + str(num_of_employees) + " employees!")  

def employee_count():
  url = "http://dropbox.com/about"
  response = requests.get(url)
  data = response.content
  data_string = data.decode('utf-8')

  global num_of_employees
  global is_done
  num_of_employees = data_string.count('bubble-dropdown bottom')
  is_done = True

waiting_thread = threading.Thread(target=waiting_phrase)
counting_thread = threading.Thread(target=employee_count)
printing_thread = threading.Thread(target=print_employee_count)

waiting_thread.start()
counting_thread.start()

counting_thread.join()
waiting_thread.join()

printing_thread.start()