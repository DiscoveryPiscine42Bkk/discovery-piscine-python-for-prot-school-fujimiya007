def swap_case(text):
    """
    สลับตัวพิมพ์ใหญ่และตัวพิมพ์เล็กในสตริง

    Args:
      text: สตริงที่ต้องการสลับตัวพิมพ์

    Returns:
      สตริงที่สลับตัวพิมพ์แล้ว
    """
    return text.swapcase()

# รับข้อมูลสตริงจากผู้ใช้
text = input("Enter a string: ")

# แสดงผลลัพธ์
print(swap_case(text))