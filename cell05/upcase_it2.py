import sys

def main():
  """
  แปลงสตริงที่รับมาเป็นตัวพิมพ์ใหญ่และแสดงผลลัพธ์
  """
  if len(sys.argv) == 2:
    input_string = sys.argv[1]
    print(input_string.upper())
  else:
    print("none")

if __name__ == "__main__":
  main()