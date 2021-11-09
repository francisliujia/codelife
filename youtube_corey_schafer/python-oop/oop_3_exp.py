@classmethod
def fromtimestamp(cls, t):
	"construct a date from a POSIX timestamp (like time.time())."
	y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
	return cls(y, m ,d)


@classmethod
def today(cls):
	"construct a date from time.time()."
	t = _time.time()
	return cls.fromtimestamp(t)

