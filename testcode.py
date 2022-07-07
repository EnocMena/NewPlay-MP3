# use the code below for the "search by artist" menu item

from youtubesearchpython import VideosSearch
from pprint import pprint

videosSearch = VideosSearch('wonderwall', limit=5)
pprint(videosSearch.result())
