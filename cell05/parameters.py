import sys

def main():
  """
  แสดงจำนวนพารามิเตอร์ที่ส่งไปยังโปรแกรม
  """
  num_parameters = len(sys.argv) - 1
  print(f"Number of parameters: {num_parameters}.")

if __name__ == "__main__":
  main()