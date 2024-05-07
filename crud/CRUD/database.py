from . import operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXX",
    "date_add":"yyyy-mm-dd",
    "title":255*" ",
    "writer":255*" ",
    "year":"yyyy",
}

def init_terminal():
    try:
        with open(DB_NAME,"r") as file:
            print("Database found, init done!")
    except:
        print("Database not found, please make a new one!")
        operation.create_first_data()
        