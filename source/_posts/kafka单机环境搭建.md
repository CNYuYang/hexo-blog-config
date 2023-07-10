---
title: kafka单机环境搭建
categories:
- kafka
- zookeeper
---

# 软件版本

- jdk-8u271-linux-x64.tar.gz
- apache-zookeeper-3.8.1-bin.tar.gz
- kafka_2.12-3.4.0.tgz

> 解压添加`PATH`等步骤忽略，不进行记录。`java`安装过程跳过

# zookeeper安装

1. 先进入`conf`目录

2. 复制一份`zoo.cfg`:

```shell
cp zoo_sample.cfg zoo.cfg
```

3. 修改`zoo.cfg`，修改数据目录：`dataDir=../tmp/zookeeper`

4. 先进入`bin`目录

5. 执行`./zkServer.sh start`

6. 使用jps查看是否启动成功，`QuorumPeerMain`便是`zookeeper`入口类：

```shell
[root@localhost bin]# jps
8550 QuorumPeerMain
17046 Jps
```

# kafka

## 配置

编辑`server.properties`文件，能够被内网访问：

```properties
listeners=PLAINTEXT://192.168.3.14:9092
```

关闭防火墙：

```shell
service firewalld stop
```

## Shell命令

### 启动

1. 非后台启动

当启动失败时，可以看报错：

```shell
./kafka-server-start.sh  ../config/server.properties
```

2. 后台启动

```shell
./kafka-server-start.sh -daemon ../config/server.properties
```

启动成功后，使用jps查看，存在`Kafka`：

```shell
[root@localhost bin]# jps
17890 Jps
8550 QuorumPeerMain
17818 Kafka
```

### 主题

1. 创建

```shell
kafka-topics.sh --bootstrap-server 192.168.3.14:9092 --create --partitions 1 --replication-factor 1 --topic first
```

2. 查看

```shell
kafka-topics.sh --bootstrap-server 192.168.3.14:9092 --describe --topic first
```

3. 列表

```shell
kafka-topics.sh --bootstrap-server 192.168.3.14:9092 --list
```

### 消费者

```shell
./kafka-console-consumer.sh --bootstrap-server 192.168.3.14:9092 --topic first
```

### 生产者

```shell
kafka-console-producer.sh --broker-list 192.168.3.14:9092 --topic first
```