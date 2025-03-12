
import sys

def append_ism(parameters):
    """
    เพิ่ม "ism" ต่อท้ายแต่ละพารามิเตอร์ที่ไม่ลงท้ายด้วย "ism"
    """

    if not parameters:
        print("none")
        return

    for param in parameters:
        if not param.endswith("ism"):
            print(param + "ism")

if __name__ == "__main__":
    
    parameters = sys.argv[1:]
    append_ism(parameters)