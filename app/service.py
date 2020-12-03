from . import models
from datetime import datetime
from django.db import transaction


# 第二题
def query(start_time,end_time):

	# 先将指定时间段内交易金额最大的前三名获取到
	ret = models.User_transaction.objects.filter(
		date__gt=start_time,
		date__lt=end_time,
	).order_by('-price')[0:3]

	lst = []
	# 遍历重组数据结构以返回
	for item in ret:
		id = item.associated_user.id
		price = item.price
		data = {'id':id,'price':price}
		lst.append(data)

	return lst


# 第三题
# 开启事务确保出错自动回滚
@transaction.atomic
def transfer(user_a, user_b, money):
	# 设置保存点
	sid = transaction.savepoint()

	# 校验账户是否存在, 以及金额是否足够
	A = models.User_account.objects.filter(account_number=user_a,balance__gt=money)
	B = models.User_account.objects.filter(account_number=user_b)

	# 假定交易金额为300
	money = 300

	# 当两个账户存在时, 交易才能开始
	if A and B:
		try:
			A.balance -= money
			B.balance += money
		except Exception as e:
			print(e)
			# 回滚到保存点
			transaction.savepoint_rollback(sid)
			return '交易失败!'

		# 添加交易记录
		obj = models.User_transaction.objects.create(
			associated_user=user_a,
			date=datetime.now(),
			price=money
		)
		A.save()
		B.save()
		obj.save()

	return 'OK'


# 第五题
class Get_Bookings:

	def __init__(self):
		self.bookings = []
		self.current_page = 1

	# def get_booking_list(page_size -> int):
	# 	# 调用过程已省略，假设我们每次都调用成功，所以你调用这个函数肯定能拿到return的数据
	# 	return {
	# 		bookings: [],  # booking 列表，具体内容请忽略，不影响逻辑，此次返回的booking数据，
	# 		page_size: 50,  # page_size，此处50只是举例，数值应与传入的page_size值一致，
	# 		# 但不一定与len(bookings)的数值一致，因为存在 总量是30，page_size是50 的情况，即总量比指定page_size小的情况
	# 		current_page: 1  # 当前页码
	# 	}

	def get_bookings(self):
		sign = True
		bookings = self.bookings
		page_size = 100
		while sign:
			res = self.get_booking_list(page_size)
			if res:
				bookings.append(res)
				page_size += 100
			else:
				sign = False

		return bookings