# !/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 25, 2021
# This program calculates the area of a triangle.
def calc_area(base, height):
    area = (1/2)*base*height
    print("If base is {}cm and height is {}cm the area is {}cm^2"
          .format(base, height, area))
    area = (1/2)*base*height <= 0
    print("Invalid input")


def main():
    user_base = input("Enter the base(cm): ")
    user_height = input("Enter the height(cm): ")

    try:
        base_from_user = float(user_base)
        height_from_user = float(user_height)

    except Exception:
        print("Invalid input")

    else:

        calc_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
