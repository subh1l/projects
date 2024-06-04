from . import database
from .util import random_string
import time
import os

def delete(book_num):
    try:
        with open(database.DB_NAME, "r") as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == book_num - 1:
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database error")

    os.rename("data_temp.txt", database.DB_NAME)

def update(book_num, pk, data_add, year, title, writer):
    data = database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] =  data_add
    data["writer"] = writer + database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'

    data_length = len(data_str)

    try:
        with open(database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(data_length*(book_num-1))
            file.write(data_str)
    except:
        print("Error while updating")
        
def create(year, title, writer):
    data = database.TEMPLATE.copy()

    data["pk"] = random_string(5)
    data["date_add"] =  time.strftime("%Y-%m-%d-%h-%M-%S%z",time.gmtime())
    data["writer"] = writer + database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'
    try:
        with open(database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed saving")


def create_first_data():
    writer = input("Writer: ")
    title = input("Title: ")
    while(True):
        try:
            year = int(input("Year\t: "))
            if len(str(year)) == 4:
                break
            else:
                print("Year only support 4 number")
        except:
            print("Year must in number, please re-enter year data")

    data = database.TEMPLATE.copy()

    data["pk"] = random_string(5)
    data["date_add"] =  time.strftime("%Y-%m-%d-%h-%M-%S%z",time.gmtime())
    data["writer"] = writer + database.TEMPLATE["writer"][len(writer):]
    data["title"] = title + database.TEMPLATE["title"][len(title):]
    data["year"] = str(year)

    data_str = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'
    print(data_str)
    try:
        with open(database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed saving")

def read(**kwargs):
    try:
        with open(database.DB_NAME,"r") as file:
            content = file.readlines()
            book_amount = len(content)
            if "index" in kwargs:
                book_index = kwargs["index"]-1
                if book_index < 0 or book_index > book_amount:
                    return False
                else:
                    return content[book_index]
            else:
                return content
    except:
        print("Failed reading database")
        return False
