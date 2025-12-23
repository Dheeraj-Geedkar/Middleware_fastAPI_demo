from fastapi import FastAPI , Request

app = FastAPI()

# http  middleware 
@app.middleware("http")
async def my_middleware (request : Request , call_next ) :
    print("Middleware before handling request")
    response = await call_next(request)
    print("Middleware after handling request but before returning response")
    return response 

# a request created for testing middleware functionality 
@app.get("/users")
async def get_users():
    print("Inside get user endpoint")
    return {"msg" : "All users"} 

# middleware will be called and executed for every requsest 
# see output at terminal

# order of execution will be  

#  => without api call  (output)

# 1   print("Middleware before handling request")

# 2   print("Middleware after handling request but before returning response")


#  => with api call     (output)

# 1    print("Middleware before handling request")

# 2    print("Inside get user endpoint") => because of  call_next(request)

# 3    print("Middleware after handling request but before returning response")

# 4    return {"msg" : "All users"}  =>  it gets printed at screen at last as , it is response also awaits 
