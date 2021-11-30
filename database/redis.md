--- 20190425 ---  
Redis 字符串（string）命令

    set  
    setnx  
    append  
    setex  

    get  
    mget  
    getrange  
    strlen  

    incr  
    decr

    参考链接：
    http://www.runoob.com/redis/redis-strings.html
    https://www.jianshu.com/p/8c1b2b39deb0
---

--- 20210223 ---  
redis (remote dictionary server): string, hash, list, set, sorted set

    set a 1
    get a
    
    hmset b 1 2 3 4
    hget b 1
    hget b 3
    
    lpush c 1
    lpush c 2
    lpush c 3
    lrange c 0 2
    
    sadd d 1
    sadd d 2
    sadd d 3
    sadd d 3
    smembers d
    
    zadd e 0 1
    zadd e 0 2
    zadd e 0 3
    zadd e 0 3
    zrangebyscore e 0 3
---

--- 20210224 ---

    pip install redis
    $ redis-server
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
        在 Redis 中设置值，默认不存在则创建，存在则修改。
        参数：
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

    redis-cli -h host -p port
    > auth [user:]password
    > ping
    > keys *
    > lpush list a b c d e
---

--- 20210805 ---

    1. redis按照hash进行存值
        hmset key field1 value1 field2 value2 ...
    2. redis得到hash的key中某一个field的值
        hmget key field
    3. redis返回哈希表key的所有field值和所有的value值
        hgetall key
    4. redis返回哈希表key的所有filed的值
        hkeys key
    5. redis返回哈希表key的所有的value值
        hvals key
    6. redis删除哈希表key的某一个field值和对应的value值
        hdel key field
    7. redis设置key的过期时间
        expire key time | expireat key time
    8. redis查看key的到期时间或剩余的剩余的生存时间
        ttl key
    9. redis删除key的过期时间
        persist key
---

--- 20211125 ---

    import redis
    r = redis.StrictRedis(host='redistributionpublic.redis.rds.aliyuncs.com', port=6379, db=0, password='xxoo1234@')
    
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

    sorted set
    
    ZADD xl 1 a 2 b 3 c
    ZCARD xl
    ZCOUNT xl 0 3
    ZINCRBY xl 2 b
    ZRANGE xl 0 3
    ZRANK xl b
    ZREM xl b
    ZREMRANGEBYSCORE xl 0 3
    ZREVRANGE xl 3 0
    ZSCORE xl c
