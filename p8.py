def string_reversal(value):
    try:
      if type(value).__name__=="str":
        return value[::-1]
      return "only excepted string"

    except Exception as e:
        print(e)
print(string_reversal("the quick brown fox jumps over the lazy dog"))
print(string_reversal(10.5))