def invert_dict(d):
	inverse = dict()
	for key in d:
		value = d[key]
		inverse.setdefault(value, []).append(key)
	return inverse