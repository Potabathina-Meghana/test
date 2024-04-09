import unittest

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

class TestPrimeNumbers(unittest.TestCase):
    
    def test_prime_numbers_within_interval(self):
        lower = 900
        upper = 1000
        primes_within_interval = [907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        for num in primes_within_interval:
            self.assertTrue(is_prime(num))
    
    def test_non_prime_numbers_within_interval(self):
        lower = 900
        upper = 1000
        non_primes_within_interval = [900, 901, 902, 903, 904, 905, 906, 908, 909, 910, 912, 913, 914, 915, 916, 917, 918, 920, 921, 922, 923, 924, 925, 926, 927, 928, 930, 931, 932, 933, 934, 935, 936, 938, 939, 940, 942, 943, 944, 945, 946, 948, 949, 950, 951, 952, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 968, 969, 970, 972, 973, 974, 975, 976, 978, 979, 980, 981, 982, 984, 985, 986, 987, 988, 989, 990, 992, 993, 994, 995, 996, 998, 999, 1000]
        for num in non_primes_within_interval:
            self.assertFalse(is_prime(num))

if __name__ == '__main__':
    unittest.main()
