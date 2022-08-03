# Class used to test api functions locally
from FlowchartObjectDetection import detect


def main():
    result = detect('./TestStuff/HelloWorld2.jpg')
    print(result)


if __name__ == "__main__":
    main()

