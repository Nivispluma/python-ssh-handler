from fabric import Connection

def hello():
    print("hello World")

def test_func():
    print(f"input IP")
    host_ip = input()

    print(f"input Username")
    host_username = input()

    print(f"input Password")
    host_pw = input()

    # print(f"input Port")
    host_port = 22

    # create  a connection
    # con = Connection(host=host_ip, connect_kwargs={"password"=sys_password })

    conn = Connection(
        "{username}@{ip}:{port}".format(
            username=host_username,
            ip=host_ip,
            port=host_port,
        ),
        connect_kwargs={"password": host_pw},
    )

    conn.run('ls')

# ---------------------------------------------------------

def standard_connect(host_ip, host_username, host_password, host_port):
    conn = Connection(
        "{username}@{ip}:{port}".format(
            username=host_username,
            ip=host_ip,
            port=host_port,
        ),
        connect_kwargs={"password": host_password},
    )

    conn.run('ls')