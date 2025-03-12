import sys

def main():
  """
  แสดงพารามิเตอร์แรกที่ส่งไปยังโปรแกรม หรือ "none" หากไม่มีพารามิเตอร์
  """
  if len(sys.argv) > 1:
    print(sys.argv[1])
  else:
    print("min")

if __name__ == "__main__":
  main()