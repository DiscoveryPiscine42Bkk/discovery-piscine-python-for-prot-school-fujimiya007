import sys

def main():
  """
  เปรียบเทียบพารามิเตอร์กับคำที่ผู้ใช้ป้อน
  """
  if len(sys.argv) != 2:
    print("none")
    return

  parameter = sys.argv[1]
  user_input = input("What was the parameter? ")

  if user_input == parameter:
    print("Good job!")
  else:
    print("Nope, sorry...")

if __name__ == "__main__":
  main()