import argparse
import sys

from String import String


def main():
    parser = argparse.ArgumentParser(description="High E simulator")

    parser.add_argument(
        "--material",
        "-m",
        help="Material, can be Nylon, Steel or Bronze",
        required=True,
    )
    parser.add_argument(
        "--tension",
        "-t",
        help="String tension rating, can be Low, Medium or High",
        default="Medium",
    )

    args = parser.parse_args()

    try:
        string = String.parse(args)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(string)


if __name__ == "__main__":
    main()
