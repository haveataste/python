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
