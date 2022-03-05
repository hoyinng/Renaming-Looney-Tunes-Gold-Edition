This script helps rename your Looney Toon Gold Collection into [Collection with correct format] (https://www.reddit.com/r/jellyfin/comments/s6pino/looney_tunes_golden_collection_scraped_data_fix/)

Change src to where your collection is located and dst to where the collection folder skeleton is located.

Test run can be done by ```python main.py```. Uncomment ```os.replace(i,r)``` to perform the move.

Example :
> python main.py
....
Y:\Movies\Temp\Looney.Tunes.S01-S24.Golden.Collection.DVDRip\Looney Tunes Season 9\914 Hillbilly Hare.mkv > Y:\Movies\Temp\Looney Tunes Golden Collection\Volume 3\S03E14 Hillbilly Hare (1950).mkv
Y:\Movies\Temp\Looney.Tunes.S01-S24.Golden.Collection.DVDRip\Looney Tunes Season 9\915 Duck! Rabbit, Duck!.mkv > Y:\Movies\Temp\Looney Tunes Golden Collection\Volume 3\S03E15 Duck! Rabbit, Duck! (1953).mkv
>
