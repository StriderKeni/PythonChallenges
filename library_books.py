import datetime
import string

def time_delta(t1, t2):
	diff = t1 - t2
	return int(diff.total_seconds()) / 86400

def calculate_fine(return_date, due_date, days):
	fine = 0	

	if return_date[1:] == due_date[1:]:
		fine = 15*days
	elif (return_date[1] > due_date[1]) and (return_date[2] == due_date[2]):
		fine = 500*int((days/30))
	elif return_date[2] > due_date[2]:
		fine = 10000

	return fine


if __name__ == '__main__':

	time_format = '%d-%m-%Y'

	return_date = list(map(str, input().split()))
	due_date = list(map(str, input().split()))

	delta_return = datetime.datetime.strptime('-'.join(return_date), time_format)
	delta_due = datetime.datetime.strptime('-'.join(due_date), time_format)

	days = int(time_delta(delta_return, delta_due))

	if delta_return < delta_due:
		print(0)
	else:
		print(calculate_fine(return_date, due_date, days))






