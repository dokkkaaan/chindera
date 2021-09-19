## mkdir and mv
import subprocess, sys, os
d_file = "html_list.txt"
d_list = []
with open(d_file, "r") as f:
    f_row = f.read()
    d_list = f_row.split('\n')[:-1]
for d in d_list:
    if os.path.exists(d):
        continue
    mkd = subprocess.run(['mkdir', d])
    if mkd.returncode != 0:
        print('mkdir failed.', sys.stderr)
        sys.exit(1)
    cmd1 = ['find', './', '-type', 'f']
    cmd2 = ['grep', d]
    cmd3 = ['xargs', '-I%', 'mv', '%', d+'/.']
    process1=subprocess.Popen(cmd1,stdout=subprocess.PIPE)
    process2=subprocess.Popen(cmd2, stdin=process1.stdout,stdout=subprocess.PIPE)
    process3=subprocess.Popen(cmd3, stdin=process2.stdout,stdout=subprocess.PIPE)
    mv_cmd = cmd1 + cmd2 + cmd3
    print(' '.join(mv_cmd))

