ta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
	s = input().strip()
	if s == '0':
		break

	s = s.upper()
	ans = 0
	for c in s:
		if c not in ta:
			print('Fail')
			break

		ans += ta.find(c)+1
