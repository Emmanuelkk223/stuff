from calculator import square


def main():
    test_square()

def test_square():
    try:
        assert square(1) == 1
        assert square(2) == 4
        assert square(3) == 9
        assert square(4) == 16
        assert square(5) == 25
    except AssertionError:
        print("Test failed")



if __name__ == "__main__":
    main()
