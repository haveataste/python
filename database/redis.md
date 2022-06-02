--- 20190425 ---  

    Redis 字符串（string）命令：
    set, mset, setnx, append, setex
    get, mget, getrange, strlen
    incr, decr

    参考链接：
    http://www.runoob.com/redis/redis-strings.html
    https://www.jianshu.com/p/8c1b2b39deb0
---

--- 20210223 ---  

    redis (remote dictionary server): string, hash, list, set, sorted set

    set a 1
    get a
    mset k1 v1 k2 v2
    mget k1 k2
    
    hmset b f1 v1 f2 v2 f3 v3
    hget b f1
    
    lpush c 1 2 3
    rpush c 4 5 6
    lrange c 0 -1
    
    sadd d 1 2 3
    sadd d 3
    smembers d
    sismember d 3   # 匹配成功返回 1，匹配失败返回 0
    
    zadd e 0 1
    zadd e 0 2
    zadd e 0 3
    zadd e 0 3
    zrangebyscore e 0 3
    zrange e 0 -1 [withscores]
    zrevrange e 0 -1
---

--- 20210224 ---

    pip install redis
    $ redis-server # 启动redis服务
    >import redis
    >r = redis.StrictRedis(host='localhost', port=6379, db=0[, password=''])
    >r = redis.StrictRedis(host='redistributionpublic.redis.rds.aliyuncs.com', port=6379, db=0, password='xxoo1234@')
    >r.set('a', '1')
    >r.get('a')
    # ConnectionPool 管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
    # redis 取出的结果默认是字节，我们可以设定 decode_responses=True 改成字符串。
    >pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    >r = redis.Redis(connection_pool=pool)
---

--- 20210225 ---

    r.keys()
    r.delete(key)
    r.set(name, value, ex=None, px=None, nx=False, xx=False)
        在 Redis 中设置值，默认不存在则创建，存在则修改。参数：
        ex - 过期时间（秒）
        px - 过期时间（毫秒）
        nx - 如果设置为True，则只有name不存在时，当前set操作才执行
        xx - 如果设置为True，则只有name存在时，当前set操作才执行
    r.setex(name, time, value)
    r.psetex(name, time_ms, value)
    r.setrange(name, offset, value)
        修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
    r.getrange(key, start, end)
        获取子序列（根据字节获取，非字符）
    r.strlen(name)
    r.incr(self, name, amount=1)
    r.decr(self, name, amount=1)
    r.append(key, value)
---

--- 20210314 ---

    购买阿里云云数据库KVStore版（包月）
    实例名称：r-7xv0ea1d7c547674
    有效期：2021-03-14 19:02:42--2022-03-15 00:00:00
    费用：19.9元
    
    先要设置白名单，才能连接redis实例；
---

--- 20210316 ---

    redis-cli -h host -p port [-d db0 -a password]
    > auth [user:]password
    > ping
    > keys *
    > dbsize                        # 返回当前数据库的 key 的总数
    > type key
    > exists key
    > del key
    > randomkey                     # 随机获得一个已经存在的 key，如果当前数据库为空，则返回空字符串
    > clear                         # 清除界面
    > rename oldname newname        # 更改 key 的名字，新键如果存在将被覆盖
    > renamenx oldname newname      # 更改 key 的名字，新键如果存在则更新失败
    > expire key time               # 设置某个 key 的过期时间（秒）
    > ttl key                       # 查找某个 key 还有多长时间过期，返回时间单位为秒
    > flushdb                       # 清空当前数据库中的所有键
    > help save
    
    > config get requirepass            # 用来读取运行 Redis 服务器的配置参数，查看密码
    > config set requirepass test123    # 设置密码为 test123
    > config get requirepass            # 报错，没有认证
    > auth test123                      # 认证密码
    > config get requirepass
    > config get *max-*-entries*        # 查询数据类型的最大条目，以 list 的 key-value 对显示
    > config resetstat                  # 重置数据统计报告，通常返回值为“OK”
    
    > info [server | clients | memory | persistence | stats | replication | cpu | cluster | keyspace | all | default]
---

--- 20210805 ---

    hmset key field1 value1 field2 value2 ...       # 按照hash进行存值
    hmget key field                                 # 得到hash的key中某一个field的值
    hgetall key                                     # 返回哈希表key的所有field值和所有的value值
    hkeys key                                       # 返回哈希表key的所有filed的值
    hvals key                                       # 返回哈希表key的所有的value值
    hdel key field                                  # 删除哈希表key的某一个field值和对应的value值
    expire key time | expireat key time             # 设置key的过期时间
    ttl key                                         # 查看key的到期时间或剩余的剩余的生存时间
    persist key                                     # 删除key的过期时间
---

--- 20211125 ---
    
    with open('some.jpg', 'rb') as f:
        s = f.read()
    # 将文件写入集合
    r.sadd('pic', s)
    # 获取集合中元素个数
    r.scard('pic')
    # 获取集合中所有的成员--元组形式
    a = r.sscan('pic')
    type(a)  # <class 'tuple'>
    # 获取集合中所有的成员--set形式
    b = r.smembers('pic')
    type(b)  # <class 'set'>
---

--- 20211127 ---

    SORTED SET
    zadd xl 1 a 2 b 3 c
    zcard xl
    zcount xl 0 3
    zincrby xl 2 b
    zrange xl 0 3
    zrank xl b
    zrem xl b
    zremrangebyscore xl 0 3
    zrevrange xl 3 0
    zscore xl c
---

--- 20220321 ---
    
    ./redis-cli.exe -h redis-19073.c289.us-west-1-2.ec2.cloud.redislabs.com -p 19073 -d memdb -a memdb
---

--- 20220529 ---
    
    主从复制：为了分担服务器压力，会在特定情况下部署多台服务器分别用于缓存的读和写操作，用于写操作的服务器称为主服务器，用于读操作的服务器称为从服务器。从服务器通过 psync 操作同步主服务器的写操作，并按照一定的时间间隔更新主服务器上新写入的内容。
    主从复制的过程：
      1. Slave 与 Master 建立连接，发送 psync 同步命令。
      2. Master 会启动一个后台进程，将数据库快照保存到文件中，同时 Master 主进程会开始收集新的写命令并缓存。
      3. 后台完成保存后，就将此文件发送给 Slave。
      4. Slave 将此文件保存到磁盘上。
    主从复制特点：
      1. 可以拥有多个 Slave。
      2. 多个 Slave 可以连接同一个 Master 外，还可以连接到其它的 Slave。（当 Master 宕机后，相连的 Slave 转变为 Master）。
      3. 主从复制不会阻塞 Master，在同步数据时， Master 可以继续处理 Client 请求。
      4. 提高了系统的可伸缩性。
      5. 非阻塞式的同步只能应用于对读数据延迟接受度较高的场景。
    建立这样一个主从关系的缓存服务器，只需要在 Slave 端执行命令：
      > slaveof 127.0.0.1 6379
      > config set masterauth <password>  # 如果主服务器设置了连接密码，就需要在从服务器中事先设置好
      
    事务处理:Redis 的事务处理比较简单。只能保证 client 发起的事务中的命令可以连续的执行，而且不会插入其它的 client 命令，当一个 client 在连接中发出 multi 命令时，这个连接就进入一个事务的上下文，该连接后续的命令不会执行，而是存放到一个队列中，当执行 exec 命令时，redis 会顺序的执行队列中的所有命令。
      > multi
      > set name a
      > set name b
      > exec
      > get name

    数据持久化：
      1. snapshotting（快照）：将数据存放到文件里，默认方式。是将内存中的数据以快照的方式写入到二进制文件中，默认文件 dump.rdb，可以通过配置设置自动做快照持久化的方式。可配置 Redis 在 n 秒内如果超过 m 个 key 被修改就自动保存快照。save 命令是将数据写入磁盘中。比如： save 300 10：300 秒内如果超过 10 个 key 被修改，则快照保存。 
      2. AOF(Append-only file)。配置文件中的可配置参数：
        appendonly yes          //启用 aof 持久化方式
        #appendfsync always     //收到写命令就立即写入磁盘，最慢，但是保证了数据的完整持久化
        appendfsync everysec    //每秒钟写入磁盘一次，在性能和持久化方面做了很好的折中
        
    虚拟内存：Redis 的虚拟内存是暂时把不经常访问的数据从内存交换到磁盘中，从而腾出内存空间用于其它的访问数据，尤其对于 redis 这样的内存数据库，内存总是不够用的。除了分隔到多个 redis server 外，提高数据库容量的方法就是使用虚拟内存，把那些不常访问的数据交换到磁盘上。虚拟内存管理在 2.6 及之上版本取消了，由 redis 软件自身管理。
---

--- 20220602 ---
        
    lpush key value1 [value2 ...]                  # 将一个或多个值插入到列表头部。如果key值不存在，会先创建再执行lpush命令，如果key值存在但不是列表类型时，返回一个错误
    rpush key value1 [value2 ...]                  # 将一个或多个值插入到列表尾部。如果key值不存在，会先创建再执行lpush命令，如果key值存在但不是列表类型时，返回一个错误
    lpop key                                       # 用于移除并返回列表的第一个元素
    rpop key                                       # 用于移除并返回列表的最后一个元素
    llen key                                       # 返回列表长度，如果key不存在，返回0，如果key不是列表列表类型，返回错误
    lrange key start stop                          # 获取列表中指定区间的元素，0表示列表中第一个元素，-1表示列表中最后一个元素
    lindex key index                               # 用于通过索引获取列表中的元素，0表示第一个元素，-1表示最后一个元素，如果指定索引值不在列表的区间范围内，返回nil
    lset key index value                           # 通过索引来设置元素的值，当指定索引超出范围，或者列表不存在时，返回错误
    linsert key before|after pivot value           # 用于在指定的元素之前或之后插入指定的元素，value为待插入的元素，pivot为列表中的元素
    ltrim key start stop                           # 对列表进行修剪，只保留指定区间内的元素，不在区间内的元素都删除，0表示列表中第一个元素，-1表示列表中最后一个元素
    rpoplpush source distination                   # 将source列表中最后一个元素移除，并将该元素添加到destination列表中，可简单理解为“尾删头插”
    brpoplpush source destination timeout          # 从列表中取出最后一个元素并插入到另一个元素的头部（尾删头插），如果列表没有元素会阻塞知直到超时会发现可弹出元素为止，timeout的单位为秒
    blpop key1 [key2] timeout                      # 移除列表中的第一个元素，如果列表没有元素会阻塞直到超时或者发现可弹出元素为止，timeout的单位为秒
    brpop key1 [key2] timeout                      # 移除列表中的最后一个元素，如果列表没有元素会阻塞直到超时或者发现可弹出元素为止，timeout的单位为秒
    lrem key count value                           # 移除列表中与指定元素相等的元素，count>0：从头到尾搜索，移除与value相等的元素，数量为count；count<0：从尾到头搜索，移除与value相等的元素，数量为count的绝对值；count=0：移除列表中所有与value相等的元素
---
