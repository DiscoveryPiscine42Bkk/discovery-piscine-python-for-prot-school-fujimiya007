import sys

def main():
  """
  แปลงสตริงที่รับมาเป็นตัวพิมพ์เล็กและแสดงผลลัพธ์
  """
  if len(sys.argv) == 2:
    input_string = sys.argv[1]
    print(input_string.lower())
  else:
    print("none")

if __name__ == "__main__":
  main()