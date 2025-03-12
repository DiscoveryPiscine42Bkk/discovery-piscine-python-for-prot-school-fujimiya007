#!/usr/bin/env python3
import sys

def count_and_measure_parameters(parameters):
    """
    นับและวัดความยาวของพารามิเตอร์ที่ได้รับ
    """

    if not parameters:
        print("none")
        return

    print(f"parameters: {len(parameters)}")

    for param in parameters:
        print(f"{param}: {len(param)}")

if __name__ == "__main__":
    # รับพารามิเตอร์จาก command line arguments (ไม่รวมชื่อไฟล์)
    parameters = sys.argv[1:]

    # เรียกใช้ฟังก์ชัน
    count_and_measure_parameters(parameters)