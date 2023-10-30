def getData() -> (float, float):
    """get base and height fo triangle from user, and returns them"""
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Enter the height of your triangle: "))

    return base , height


def trigArea(base : float , height : float) -> float:
    """calculate area of triangle"""
    area = base * height / 2
    return area


def displayData(base: float , height : float , area : float):
    """Displays the triangle's measurements"""
    print("The base, height and area are" , format(base , '.2f') , "," , format(height , '.2f') , "," , format(area , '.2f'))


def main():
    base, height = getData()
    area = trigArea(base , height)
    displayData(base , height , area)


if __name__ == "__main__":
    main()


## Test Run 1
## Enter the base of your triangle: 10
## Enter the height of your triangle: 5
## The base, height and area are 10.00 , 5.00 , 25.00
##
## Test Run 2
## Enter the base of your triangle: 2
## Enter the height of your triangle: 3
## The base, height and area are 2.00 , 3.00 , 3.00
##
##Test Run 3
## Enter the base of your triangle: 8
## Enter the height of your triangle: 16
## The base, height and area are 8.00 , 16.00 , 64.00
