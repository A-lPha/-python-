#汽车的数量是100
cars = 100
#汽车空间等于4
space_in_a_car = 4
#司机的数量等于30
drivers = 30
#乘客的数量等于90
passengers = 90
#汽车和司机数量之差
cars_not_driven = cars - drivers
#司机的数量
cars_driven = drivers
#可以合伙使用汽车的数量
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车的乘客的数量
average_passengers_per_car = passengers / cars_driven

print "There are",cars,"cars available"
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
