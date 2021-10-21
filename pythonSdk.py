
from jose import jwk, jwt
import requests
res=requests.get("http://localhost:5000/tokens/jwks")
data=res.json()
token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2OWZiMDQ3Mi0yZGQyLTRmMWQtYjdlMy1hZDFmNTk3ZjY0NGEiLCJhdWQiOiI5MmFkYWFjZC1kMjUyLTQ3NTctOWFjMi0yZDQ4ZDdlYzM3YmIiLCJpc3MiOiJodHRwczovL3d3dy5zZWN1dXRoLmlvIiwiZXhwIjoxNjM0NzkzNjY3MjUyLCJqdGkiOiI3NTgzNTEyNi02ZDFkLTRlYzctYmY0Yi1iZTY5ODNhYTk2MjgiLCJ0eXAiOiJBY2Nlc3NfdG9rZW4iLCJzaWduSW5Nb2RlIjoxLCJ1c2VySWQiOiJ2aXZlay5uYXJhbmdAc2VjdXV0aC5pbyIsInNjb3BlIjoiYWNjZXNzIiwiaWF0IjoxNjM0NzkwMDY3fQ.ILw68X_YqwrOEX5o-eZn0DeHuFi6afTiDv3SnxqCrr-LRBGUgG_Jdf7SzXvKJAwuxYBq0Y4QC7xnq0GqLWaVz1d0DoAiQt_qsvlcNmL3oapXWLxMLvlG725rsMXucQaZVHRvmPnD7hE0Z8cSyKldsiHMgDCjY0QYBZT50V0eOvtM_VAJ6Yb6N-5Ua0Zu6viqiZATQiaPXQq4lCCEl_TOOi5hN-MGNzuibIZy6wOOPPX_fMfEaAb5snMeT_r3J4OIYRMYv_i5jvALIVdzYVVQXbfUmB9Er7VygLz06fThe6iarcuxlTQC36bamPXAeT9ztpFuCaLS7hXP2HNaLCkwAQ"
try:
    payload = jwt.decode(
                token,
                data,
                options = {'verify_exp':False,'verify_aud': False,})
    print("verified and Decoded")
except:
    print("signature invalid and not decoded")

print (payload)















