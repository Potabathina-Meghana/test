def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(is_float("sf4a"))
print(is_float('1.236'))