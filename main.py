#! /bin/env python3


def main() -> None:
    print("hello world")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("ctrl+c: exiting...")