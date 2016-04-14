def filter_list(list, key, value):
  return filter(lambda t: t[key] == value, list)

def filter_list_not(list, key, value):
  return filter(lambda t: t[key] != value, list)

class FilterModule(object):
  def filters(self):
    return {
      'byattr': filter_list,
      'notbyattr': filter_list_not
    }
