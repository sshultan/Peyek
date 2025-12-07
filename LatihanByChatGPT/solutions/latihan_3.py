def validation_username(username):
    """
    memvalidasi spasi pada username
    """
    if username.isspace():
        result ={
            "status": True,
            "message": "ini message apabila benar",
            "data": username
        }
        return result
    
    print(username)

username = validation_username("shultan gunawan")
print(username)


magnum = "           "
print(magnum.isspace())