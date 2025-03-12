def find_the_redheads(family):
  """
  ค้นหาชื่อต้นของสมาชิกครอบครัวที่มีผมสีแดง

  Args:
    family: พจนานุกรมที่เก็บชื่อต้นและสีผมของสมาชิกครอบครัว

  Returns:
    ลิสต์ของชื่อต้นของสมาชิกที่มีผมสีแดง
  """
  redheads = list(filter(lambda name: family[name] == "red", family))
  return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))