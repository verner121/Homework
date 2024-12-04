def filter_by_state(user_dictionary, state = "EXECUTED"):
  new_dictionary = []
  for i in user_dictionary:
    if i["state"] == state:
      new_dictionary.append(i)
  return print(new_dictionary)

def sort_by_date(user_dictionary, reverse = True):
  new_date = sorted(user_dictionary, key = lambda i: i["date"], reverse = reverse)
  return print(new_date)