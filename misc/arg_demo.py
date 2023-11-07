import argparse


def main(args):
    print("Time for a big glass of", args.drink)
    print("time for a big plate of", args.f)


if __name__ == "__main__":
    # define value of drink

    parser = argparse.ArgumentParser(
        description="Parameters for accessing the GOT API."
    )
    parser.add_argument(
        "-d",
        "--drink",
        type=str,
        required=True,
        default="Water",
        help="What are you drinking?",
    )
    parser.add_argument("-f", type=str, default="Break", help="What are you eating?")

    # combine all accepted arguments into one object
    args = parser.parse_args()

    main(args)
