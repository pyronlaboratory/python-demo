try:
 print("Hello")
 raise Exception
 print(1/0)
except Exception as e:
 print(e)
