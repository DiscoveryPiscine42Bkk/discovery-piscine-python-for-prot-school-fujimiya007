#!/usr/bin/env python3

def main():
  """
  รับตัวเลขจากผู้ใช้และแสดงตัวเลขจากเลขนั้นไปจนถึง 25
  """

  try:
    num = int(input("Enter a number less than 25\n"))
  except ValueError:
    print("Error")
    return

  if num > 25:
    print("Error")
    return

  for i in range(num, 26):
    print(f"Inside the loop, my variable is {i}")

if __name__ == "__main__":
  main()