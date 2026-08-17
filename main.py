import sys

METHODS = {"GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"}

for raw in sys.stdin:
    line = raw.rstrip("\r\n")
    if not line:
        continue
    parts = line.split(" ")
    # TODO: must be exactly 3 parts; method must be in METHODS;
    # path must start with "/"; version must look like "HTTP/<digit>.<digit>".
    # If any check fails, print "INVALID" and continue.
    if len(parts) != 3:
        print("INVALID")
        continue
    # TODO: validate method, path, version
    print(f"METHOD={parts[0]} PATH={parts[1]} VERSION={parts[2]}")
