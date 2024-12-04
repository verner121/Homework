def filter_by_state(user_dictionary, state = "EXECUTED"):
  new_dictionary = []
  for i in user_dictionary:
    if i["state"] == state:
      new_dictionary.append(i)
  return print(new_dictionary)

