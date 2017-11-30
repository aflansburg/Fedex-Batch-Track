import track as t

tracker = t.BatchTracker('data/nov-fedex-ebay.csv', 'Tracking Number')

output = tracker.track()
print(output)

tracker.write_results()
