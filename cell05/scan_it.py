import sys

def main():
  """
  นับจำนวนครั้งที่คีย์เวิร์ดปรากฏในสตริง
  """
  if len(sys.argv) != 3:
    print("none")
    return

  keyword = sys.argv[1]
  text = sys.argv[2]

  count = text.count(keyword)
  if count == 0:
    print("none")
  else:
    print(count)

if __name__ == "__main__":
  main()