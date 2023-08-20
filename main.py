import os

try:
    SOME_SECRET = os.environ["MY_SECRET_TOKEN"]
except KeyError:
    SOME_SECRET = "Token not available!"
print("Hello")
print(SOME_SECRET)
