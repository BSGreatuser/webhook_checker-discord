import time, sys, requests, os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    f = open("./webhooks.txt", 'r')
except FileNotFoundError:
    print("[!] webhhook.txt 파일이 없습니다")
    f = open("./webhooks.txt", 'w')
    f.write('웹훅을 작성해주세요!')
    print("[+] webhooks.txt를 생성하였습니다. 웹훅을 작성해주세요.")
    time.sleep(5)
    sys.exit(1)

try:
    webhooks = f.readlines()
except UnicodeError:
    print("[!] 웹훅이 잘못되었습니다")
    time.sleep(1)
    sys.exit(1)
amount = len(webhooks)

inv = 0
v = 0
er = 0

if os.path.isfile("./invalid.txt") or os.path.isfile("./valid.txt") or os.path.isfile("./error.txt"):
    answ = input("이미 체킹된 웹훅을 초기화 후 체킹을 시작합니다. [y/n]: ")
    if answ == 'y':
        try:
            os.remove("./invalid.txt")
        except FileNotFoundError:
            pass
        try:
            os.remove("./valid.txt")
        except FileNotFoundError:
            pass
        try:
            os.remove("./errors.txt")
        except FileNotFoundError:
            pass
    else:
        print("[-] 체킹이 취소되었습니다")
        time.sleep(2)
        sys.exit()

n = open("./invalid.txt", 'w')
y = open("./valid.txt", 'w')

print("[!] 웹훅 체킹중...")

for i in webhooks:
    if i.strip() == '':
        er += 1
    try:
        r = requests.get(i.rstrip(), verify=False)
    except:
        err = open("./error.txt", 'w')
        err.write(i.rstrip() + "\n")
        er += 1

    try:
        if r.status_code == 200:
            y.write(i.rstrip() + "\n")
            v += 1
        elif :
            n.write(i.rstrip() + "\n")
            inv += 1
    except:
        err = open("./error.txt", 'w')
        err.write(i.rstrip() + "\n")
        er += 1

f.close()
n.close()
print("[+] 웹훅 체킹이 완료되었습니다")
print("{0}개의 웹훅 중\n유효한 웹훅: {1}개\n만료된 웹훅: {2}개\n오류난 웹훅: {3}개".format(amount, v, inv, er))
time.sleep(10)
sys.exit()
