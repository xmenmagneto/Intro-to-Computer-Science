def when_offered(courses, course):
	offered = []
	for hexamester in courses:
		if course in courses[hexamester]:
			offered.append(hexamester)
	return offered