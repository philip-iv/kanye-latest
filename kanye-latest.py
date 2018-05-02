import twitter
import argparse
import sys
from datetime import datetime

class KanyeTwitter:
	def __init__(self, consumer_key=None, consumer_secret=None, access_token_key=None, access_token_secret=None):
		self.api = twitter.Api(consumer_key='XHkIgyVELfNSPbxTUk9QPTCo4', consumer_secret='ihwVvAdP4P5VnxgGrun3eduwGgaJE8FovGpF4T0DLHfzj7PwkI', access_token_key='74303273-LhIEm5tCLC79nqabylKn3gxrhIMWsJLJNxAELQRc5', access_token_secret='fZVx4Mb2KpQc2kyi39ud8WYYfxqBBTU9xo74FdPQFcZcd')

	def get_latest(self, old=0):
		return self.api.GetUserTimeline(screen_name="kanyewest", count=old+1)[old].AsDict()

def parse():
	parser = argparse.ArgumentParser(description="Get Kanye West's latest tweets")
	parser.add_argument('--date', '-d', const='%H:%M', nargs='?', help="Show the date the tweet was posted.")
	parser.add_argument('--favorites', '-f', action='store_true', help="Show the number of favorites.")
	parser.add_argument('--old', '-n', default=0, type=int, help="If you want an older tweet, use --old n to get the nth tweet older that current. --old 0 will return the newest tweet.")
	parser.add_argument('--emoji', action='store_true', help="Enable emoji in output")
	return parser.parse_args()

flags = parse()

ye = KanyeTwitter()
tweet = ye.get_latest(old=flags.old)

out = tweet['text']
if flags.date:
	dt = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
	out = out + ' ' + dt.strftime(flags.date)
if flags.favorites:
	out = out + ' ' + ('❤️ ' if flags.emoji else '') + str(tweet['favorite_count'])

print(out)