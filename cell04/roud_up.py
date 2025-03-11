import math

# รับข้อมูลตัวเลขจากผู้ใช้
number = float(input("Give me a number: "))

# ปัดเศษขึ้นและแสดงผลลัพธ์
rounded_number = math.ceil(number)
print(rounded_number)