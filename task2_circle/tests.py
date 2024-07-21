from Figures import Circle, Triangle


tr = Triangle(2, 3, 4)
circle = Circle(5)

def main():
    assert tr.calculate_area() == 2.905
    assert tr.is_right == False

    assert circle.calculate_area() == 78.5
    assert circle.calculate_area_with_pi() == '25pi'


if __name__ == '__main__':
    main()
