def check_number_type(number):
    """
    ตรวจสอบว่าตัวเลขที่ป้อนเป็นเลขทศนิยมหรือเลขจำนวนเต็ม

    Args:
      number: ตัวเลขที่ต้องการตรวจสอบ

    Returns:
      ข้อความระบุประเภทของตัวเลข
    """
    if number.is_integer():
        return "This number is an integer."
    else:
        return "This number is a decimal."

# รับข้อมูลตัวเลขจากผู้ใช้
number = float(input("Give me a number: "))

# แสดงผลลัพธ์
print(check_number_type(number))