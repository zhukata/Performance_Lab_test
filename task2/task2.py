import argparse
import math


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_circle")
    parser.add_argument("file_dot")
    args = parser.parse_args()
    return (args.file_circle, args.file_dot)


def read_file_circle(file_path: str):
    with open(file_path, 'r') as file:
        x, y = map(int, file.readline().split())
        radius = int(file.readline())
    return x, y, radius


def read_file_dot(file_path: str):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            points.append(tuple(map(int, line.split())))
    return points


def find_point():
    file_1, file_2 = parse()
    cirlce = read_file_circle(file_1)
    points = read_file_dot(file_2)
    x, y, radius = cirlce

    result = []
    for point_x, point_y in points:
        distance = math.sqrt((point_x - x) **2 + (point_y - y)**2)

        if math.isclose(distance, radius):
            result.append(0)
        elif distance < radius:
            result.append(1)
        else:
            result.append(2)
    
    return result


def main():
    print(find_point())


if __name__ == '__main__':
    main()
