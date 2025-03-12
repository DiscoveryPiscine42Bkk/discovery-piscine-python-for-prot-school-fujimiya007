def play_with_arrays_plus_equals_2(arr):
  """
  รับอาร์เรย์และส่งคืนอาร์เรย์ใหม่ที่มีค่าที่มากกว่า 5 โดยไม่มีค่าซ้ำ
  """
  new_arr = []
  for num in arr:
    if num > 5 and num not in new_arr:
      new_arr.append(num)
  return new_arr

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result_array = play_with_arrays_plus_equals_2(original_array)
print(result_array)


example_array = [2, 8, 9, 48, 8, 22, 12, 2]
example_result = play_with_arrays_plus_equals_2(example_array)
print(example_result)