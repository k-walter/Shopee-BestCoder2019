from collections import defaultdict, deque

usr_ba = defaultdict(set)
ba_usr = defaultdict(set)
with open("bank_accounts.csv",) as f:
	f.readline()
	for line in f:
		line = line.strip().split(',')
		user, bank = line
		ba_usr[bank].add(user)
		usr_ba[user].add(bank)

usr_cc = defaultdict(set)
cc_usr = defaultdict(set)
with open("credit_cards.csv",) as f:
	f.readline()
	for line in f:
		line = line.strip().split(',')
		user, bank = line[0], line[1]
		cc_usr[bank].add(user)
		usr_cc[user].add(bank)

usr_d = defaultdict(set)
d_usr = defaultdict(set)
with open("devices.csv",) as f:
	f.readline()
	for line in f:
		line = line.strip().split(',')
		user, bank = line[0], line[1]
		d_usr[bank].add(user)
		usr_d[user].add(bank)

def isfraud(user,sell,usr_dd,dd_usr,visited,q):
	for ba in usr_dd[user]:
		for usr in dd_usr[ba]:
			if usr == sell:
				return True
			if usr not in visited:
				q.append(usr)
				visited.add(usr)
	return False

out_file = "orderid,is_fraud\n"
with open("orders.csv") as f:
	f.readline()
	for line in f:
		line = line.strip().split(',')
		order, buy, sell = line

		q = deque()
		q.append(buy)
		visited = {buy}

		fraud = False
		out_file += order + ","
		while len(q) > 0:
			user = q.popleft()
			if isfraud(user,sell,usr_ba,ba_usr,visited,q) or isfraud(user,sell,usr_cc,cc_usr,visited,q) or isfraud(user,sell,usr_d,d_usr,visited,q):
				fraud = True
				break

		out_file += "1" if fraud else "0"
		out_file += "\n"

with open("out.csv", "w", encoding="utf8") as f:
	f.write(out_file)
print("done")