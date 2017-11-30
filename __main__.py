from src import track as t


def main():
    tracker = t.BatchTracker('data/nov-fedex-ebay.csv', 'Tracking Number')

    output = tracker.track()
    print(output)

    tracker.write_results()


if __name__ == "__main__":
    main()
