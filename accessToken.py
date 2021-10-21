import json
from jose import jwt
from jose.jwt import decode
import requests


class accessToken:
    def __init__(self,token):
        self.token=token;
       
       
    def decodePayload(self):
        
        res=requests.get("http://localhost:5000/tokens/jwks")

        data=res.json()

        try:
            payload = jwt.decode(self.token,data,options= {'verify_exp':True,'verify_aud': False,})
            return payload
        except:
            print("not verified")
            return {}

    def getSub(self):
        payload=self.decodePayload();
        return payload.get('sub')
    def getAud(self):
        payload=self.decodePayload();
        return payload.get('aud')
    def getIss(self):
        payload=self.decodePayload();
        return payload.get('iss')
    def getExp(self):
        payload=self.decodePayload();
        return payload.get('exp')
    def getJti(self):
        payload=self.decodePayload();
        return payload.get('jti')
    def getTyp(self):
        payload=self.decodePayload();
        return payload.get('typ')
    def getSignInMode(self):
        payload=self.decodePayload();
        return payload.get('signInMode')
    def getUserId(self):
        payload=self.decodePayload();
        return payload.get('userId')
    def getScope(self):
        payload=self.decodePayload();
        return payload.get('scope')
    def getIat(self):
        payload=self.decodePayload();
        return payload.get('iat')
    
    
        
        
  

    