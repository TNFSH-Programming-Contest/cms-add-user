import argparse
import csv
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('users', help='filename of users list, contains 4 columns: first_name (class), last_name (real name), username, plaintext password')
parser.add_argument('-c', '--contest', dest='contests', action='append')
parser.add_argument('--dry-run', action='store_true', help="don't run any commands, but display them")
parser.add_argument('--no-user', action='store_true', help="don't run cmsAddUser")
parser.add_argument('--no-participation', action='store_true', help="don't run cmsAddParticipation")
parser.set_defaults(
    contests=[],
)
args = parser.parse_args()
print(args)


users = []
with open(args.users, 'r', encoding='utf8') as f:
    reader = csv.reader(f, )
    for row in reader:
        users.append(row)

for u in users:
    if not args.no_user:
        cmd = ['cmsAddUser', u[0], u[1], u[2], '-p', u[3]]
        print(' '.join(cmd))
        if not args.dry_run:
            subprocess.run(cmd)

    if not args.no_participation:
        for c in args.contests:
            cmd = ['cmsAddParticipation', u[2], '-c', c]
            print(' '.join(cmd))
            if not args.dry_run:
                subprocess.run(cmd)
