#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0  # pylint: disable=invalid-name
ips: list[str] = []

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi", encoding="utf-8") as kfile:
    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1  # this is the same as loginfail = loginfail + 1
            splits = line.split(" ")
            ips.append(splits[-1])


print("The number of failed log in attempts is", loginfail)
print(f"Failed IPs: {ips}")
