此项目包括zookeeper相关的部署包及其部署脚本

为了使用hadoop3.0.0的yarn对cgroup的支持，需要在研发环境部署zk
bigdev-cmpt-10
bigdev-cmpt-11
bigdev-cmpt-12

安装
ansible-playbook -i zk_dev3.host install_zookeeper_master_dev3.yml
make_conf.py没有生效，手动改/opt/zookeeper/data/myid 分别对应1，2，3s

启动服务
ansible all -i zk_dev3.host -mshell -a"su - moretv -c 'cd /opt/zookeeper/ && /opt/zookeeper/bin/zkServer.sh start"
查看服务运行情况
ansible all -i zk_dev3.host -mshell -a"su - moretv -c 'cd /opt/zookeeper/ && /opt/zookeeper/bin/zkServer.sh status"

改动hostname
bigtest-cmpt-12 改为 bigdev-cmpt-12
hostnamectl set-hostname bigdev-cmpt-12