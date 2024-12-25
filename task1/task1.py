import argparse
import sys


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("n")
    parser.add_argument("m")
    args = parser.parse_args()
    return (int(args.n), int(args.m))


def find_path(n, m):
    path = []
    current_position = 0

    for _ in range(n):
        path.append(current_position + 1)
        current_position = (current_position + m - 1) % n
        if current_position == 0:
            break

    return path


def main():
    result = find_path(*parse())
    print("".join(map(str, result)))
    
if __name__ == "__main__":
    main()
