def main():
  """
  รับข้อมูลจากผู้ใช้ใน loop และแสดงข้อความตอบกลับจนกว่าผู้ใช้จะป้อน "STOP"
  """

  while True:
    user_input = input("What you gotta say?\n")
    if user_input == "STOP":
      break
    print("I got that! Anything else?")

if __name__ == "__main__":
  main()

