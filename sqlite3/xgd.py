import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

create_table_script = '''
/*create_customer*/
create table customer(
Cus_id char(10) primary key,
Cus_name vchar(8) not null,
Cus_sex char(2) null,
Cus_birthday datetime null,
Cus_tel vchar(12) null,
Cus_loc vchar(100) null
);
/*create_commodity*/
create table commodity(
Com_id char(8) primary key,
Com_name vchar(40) not null,
Com_brand vchar(40) not null,
Com_type chart(20) not null,
Com_pricein money not null,
Com_priceout Money not null
);
/*create_purchase*/
create table purchase(
Pur_id int primary key,
Cus_id char(10) not null,
Com_id char(8) not null,
Com_sum int not null,
Pur_date datetime not null
);
'''
c.executescript(create_table_script)
conn.commit()

#---------------------------------------------------------------------------------------

customer_data = [
('ZY20130006','李勇','男','1986-3-25','13023451890','伏牛路12号'),
('GC20121355','刘晨','男','null','13839531178','商城路8号'),
('JS20140031','王敏','女','null','null','null'),
('EQ20001167','张立','男','1973-9-12','18903711511','null'),
('SJ20140002','李晓华','男','null','18503781241','null'),
('JS20110078','牛丽丽','女','1968-2-4','null','东风路34号')
]
c.executemany('insert into customer values (?,?,?,?,?,?)', customer_data)
commodity_data = [
('C1243406','3kg洗衣粉','雕牌','日用品','9.8','16.8'),
('C2035544','5L洗衣液','立白','日用品','18.4','25.7'),
('F2040031','牛角面包','香雪儿','食品','4.6','6.9'),
('F2116733','法式小面包','盼盼','食品','8.7','11.5'),
('F5389001','10kg长粒米','稳健','食品','21.8','24.9'),
('C1111544','5号电池','南孚','日用品','10.3','12.8'),
('W3405007','5L洗衣机','海尔','家用电器','2017','2338')
]
c.executemany('insert into commodity values (?,?,?,?,?,?)', commodity_data)
purchase_data = [
(1,'ZY20130006','C1243406',1,'2014-2-13'),
(2,'ZY20130006','F2116733',2,'2014-2-14'),
(3,'ZY20130006','F5389001',1,'2014-3-17'),
(4,'GC20121355','F2040031',3,'2014-6-27'),
(5,'EQ20001167','F2116733',1,'2015-1-1'),
(6,'ZY20130006','F5389001',2,'2015-1-14'),
(7,'JS20140031','W3405007',1,'2015-1-16'),
(8,'EQ20001167','F2116733',3,'2015-2-11'),
(9,'SJ20140002','C1243406',1,'2015-4-1'),
(10,'JS20110078','F2116733',1,'2016-11-12'),
(11,'EQ20001167','C1111544',10,'2016-11-18')
]
c.executemany('insert into purchase values (?,?,?,?,?)', purchase_data)
conn.commit()

print('customer')
c.execute('select * from customer')
for row in c:
    print(row)
print('commodity')
c.execute('select * from commodity')
for row in c:
    print(row)
print('purchase')
c.execute('select * from purchase')
for row in c:
    print(row)

#---------------------------------------------------------------------------------------

#with open('record.txt','w+') as rec:
while True:
    print('please input the select sentence:');s = input()
    for row in c.execute(s):
        print(row)
