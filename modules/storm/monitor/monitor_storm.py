# -*- coding: utf-8 -*-
import logging
import sys
import requests
import pdb
import json
import socket

send_to = 'peng.tao@whaley.cn,xu.tong@whaley.cn,lian.kai@whaley.cn'


def log_init():
    logging.basicConfig(level=logging.INFO,  # 定义输出到文件的log级别，
                        format='%(asctime)s  %(filename)s : LINE %(lineno)-4d %(levelname)s  %(message)s',  # 定义输出log的格式
                        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
                        filename="{0}.log".format(sys.argv[0]),  # log文件名
                        filemode='a')  # 写入模式“w”或“a”
    # Define a Handler and set a format which output to console
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter(
        '%(asctime)s  %(filename)s : LINE %(lineno)-4d  %(levelname)s  %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    # Create an instance
    logging.getLogger().addHandler(console)  # 实例化添加handler


def send_alter_mail(sub, body):
    mail_content = dict()
    mail_content["sub"] = sub
    mail_content["content"] = body
    mail_content["sendto"] = send_to
    mail_url = 'http://10.19.15.127:5006/mail/api/v1.0/send'

    heads = {'content-type': 'application/json'}
    r = requests.post(url=mail_url, headers=heads, data=json.dumps(mail_content))
    if r.status_code == 200:
        logging.info("send mail success")
    else:
        err_msg = "send mail failed ,output was %s" % r.content
        logging.error(err_msg)


def check_topology(url_topology):
    r = requests.get(url_topology)
    if r.status_code == 200:
        data = json.loads(r.content)
        for item in data['topologies']:
            if item['status'] != 'ACTIVE':
                sub = "{0} topology  check Failed".format(socket.gethostname())
                msg = "{0} status Failed, status was {1}".format(item['name'], item['status'])
                logging.error(sub + '\n' + msg)
                send_alter_mail(sub=sub, body=msg)
        logging.info("check topology complete!")
    else:
        logging.error("connect {0} Failed {1} error code {2}".format(url_topology, r.content, r.status_code))


def check_supervisor(url_supervisor):
    r = requests.get(url_supervisor)
    all_host = ['bigdata-cmpt-128-2', 'bigdata-cmpt-128-3', 'bigdata-cmpt-128-14', 'bigdata-cmpt-128-15',
                'bigdata-cmpt-128-26', 'bigdata-cmpt-128-27', 'bigdata-cmpt-128-38', 'bigdata-cmpt-128-39',
                'bigdata-cmpt-128-50', 'bigdata-cmpt-128-51', 'bigdata-cmpt-128-4', 'bigdata-cmpt-128-5',
                'bigdata-cmpt-128-16', 'bigdata-cmpt-128-17', 'bigdata-cmpt-128-28', 'bigdata-cmpt-128-29',
                'bigdata-cmpt-128-40', 'bigdata-cmpt-128-41', 'bigdata-cmpt-128-52', 'bigdata-cmpt-128-53']
    active_host = list()
    if r.status_code == 200:
        data = json.loads(r.content)
        for item in data['supervisors']:
            active_host.append(item['host'])
    else:
        logging.error("connect {0} Failed {1} error code {2}".format(url_supervisor, r.content, r.status_code))

    ret_list = list(set(all_host) ^ set(active_host))
    if ret_list:
        msg = "{0} supervisor not found!".format(json.dumps(ret_list))
        logging.error(msg)
        sub = "Storm supervisor monitor error"
        send_alter_mail(sub=sub, body=msg)
    else:
        logging.info("check url_supervisor success!")


def main():
    url_topology = 'http://bigdata-cmpt-128-25:6060/api/v1/topology/summary'
    url_supervisor = 'http://bigdata-cmpt-128-25:6060/api/v1/supervisor/summary'
    check_topology(url_topology)
    check_supervisor(url_supervisor)


if __name__ == "__main__":
    """
    本工具用于监控storm状态，部署在管理机每2小时执行一次
    如发现异常，邮件通知相关人
    """

    log_init()
    main()
