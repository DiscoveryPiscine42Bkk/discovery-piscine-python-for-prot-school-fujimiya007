def array_of_names(persons):
  """
  สร้างอาร์เรย์ของชื่อเต็มจากพจนานุกรม

  Args:
    persons: พจนานุกรมที่เชื่อมโยงชื่อต้นกับนามสกุล

  Returns:
    อาร์เรย์ของชื่อเต็ม โดยชื่อเต็มจะขึ้นต้นด้วยตัวพิมพ์ใหญ่
  """
  full_names = []
  for first_name, last_name in persons.items():
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    full_names.append(full_name)
  return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))