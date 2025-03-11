def main():
  """
  รับตัวเลขจากผู้ใช้และแสดงตารางสูตรคูณของตัวเลขนั้น
  """

  try:
    num = int(input("Enter a number\n"))
  except ValueError:
    print("Invalid input. Please enter a number.")
    return

  for i in range(10):
    print(f"{i} x {num} = {i * num}")

if __name__ == "__main__":
  main()

