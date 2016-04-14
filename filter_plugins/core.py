def byattr(list, key, value):
  return filter(lambda t: t[key] == value, list)

def notbyattr(list, key, value):
  return filter(lambda t: t[key] != value, list)

class FilterModule(object):
  def filters(self):
    return {
      'byattr': byattr,
      'notbyattr': notbyattr
    }
