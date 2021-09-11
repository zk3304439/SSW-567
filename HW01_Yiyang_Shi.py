"""Author:Yiyang Shi
   Program content:HW01: Classify Triangle
   unittest: Write some tests to check the Triangle.
"""


def classifytriangle(a, b, c):
    """ judge the Triangle """
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a + c > b:
            if a == b and b == c:
                return "Equilateral"
            elif a == b or b == c or c == a:
                return "Isosceles"
            elif (a * a + b * b == c * c) or (b * b + c * c == a * a) or (a * a + c * c == b * b):
                return "Right"
            else:
                return "Scalene"
        else:
            return "NotATriangle"


def runclassifytriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifytriangle(a, b, c), sep="")


if __name__ == '__main__':
    """ run the code """
    runclassifytriangle(1, 2, 3)
    runclassifytriangle(1, 1, 1)
    runclassifytriangle(1, 2, 2)
    runclassifytriangle(3, 3, 5)
    runclassifytriangle(5, 5, 5)
    runclassifytriangle(3, 4, 5)
