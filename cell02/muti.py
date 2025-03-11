
def main():


  try:
    num1 = float(input("ป้อนตัวเลขแรก: "))
    num2 = float(input("ป้อนตัวเลขที่สอง: "))
  except ValueError:
    print("ป้อนตัวเลขที่ไม่ถูกต้อง")
    return

  result = num1 * num2

  if result > 0:
    print("ผลลัพธ์เป็นบวก")
  elif result < 0:
    print("ผลลัพธ์เป็นลบ")
  else:
    print("ผลลัพธ์เป็นศูนย์")

  print(f"ผลลัพธ์ของการคูณคือ: {result}")

if __name__ == "__main__":
  main()