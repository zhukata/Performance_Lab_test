import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    return (args.file)


def read_file(file_path: str):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(int(line.strip()))
    return data

    
def get_min_steps():
    file_path = parse()
    nums = read_file(file_path)
    mediana = sorted(nums)[len(nums) // 2]
    steps = sum(abs(num - mediana) for num in nums)
    return steps


def main():
    print(get_min_steps())


if __name__ == '__main__':
    main()