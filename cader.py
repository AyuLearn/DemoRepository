from decouple import config

cader_username = config('cader_username')
cader_password = config('cader_password')

print(cader_username)
print(cader_password)