import json
import base64


def ali():
	sd=input("inter nem file ")
	with open(sd,"r") as file:
		df=file.read()
	we=df.encode("utf-8")
	b16=base64.b16encode(we)
	print(b16)
	
	er=input("enter nem file ")
	with open(er,"wb") as fe:
		ddd=fe.write(b16)
	



def ahmad():
	sd=input("inter nem file ")
	with open(sd,"rb") as d:
		er=d.read()
		
		
	decod=base64.b16decode(er).decode("utf-8")
	
	print(decod)
	sds=input("enter nem file ")
	with open(sds,"w") as ere:
		ere.write(decod)
		ere.close()
ahmad()