import sys

def main():
  """
  แสดงพารามิเตอร์ในลำดับย้อนกลับ หรือ "none" หากมีพารามิเตอร์น้อยกว่า 2 ตัว
  """
  if len(sys.argv) < 3:
    print("none")
  else:
    for i in range(len(sys.argv) - 1, 0, -1):
      print(sys.argv[i])

if __name__ == "__main__":
  main()