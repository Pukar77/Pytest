import requests
database = {
     1:"Pukar",
     2:"Rimal",
     3:"Hero"
}

def get_user_from_db(userid):
    return database.get(userid)


#For API
def get_user():
    responses = requests.get("https://jsonplaceholder.typicode.com/users")
    if responses.status_code == 200:
       
        return responses.json()
    
    raise requests.HTTPError

if __name__ == '__main__':
    get_user()
        
   
    







