
import sys

def count_and_print_zs(text):
    """
    นับและพิมพ์ 'z' ตามจำนวนที่พบในสตริง
    """

    if len(sys.argv) != 2:
        print("none")
        return

    count = text.count('z')

    if count == 0:
        print("none")
        return

    for _ in range(count):
        print("z")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = sys.argv[1]
        count_and_print_zs(text)
    else:
        print("none")