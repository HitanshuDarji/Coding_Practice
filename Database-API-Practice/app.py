from fastapi import FastAPI
import cx_Oracle
from pydantic import BaseModel
from typing import Optional
import pandas as pd

app = FastAPI()


def get_db_cursor():
    cs = 'system/Ayy*Homie*1@localhost:1521/xe'
    con = cx_Oracle.connect(cs)
    cur = con.cursor()
    return con, cur


def close_db_cursor(connection, cursor):
    cursor.close()
    connection.close()


class Coffee(BaseModel):
    name: str
    color: Optional[str] = None
    flavor: Optional[str] = None
    origin: Optional[str] = None


class UpdateCoffee(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    flavor: Optional[str] = None
    origin: Optional[str] = None


@app.get("/")
def home():
    return {"message": "Welcome to the Coffee Shop API!"}


@app.get("/coffees")
def list_table_data():
    con, cur = get_db_cursor()
    sqlCmd = "SELECT CID ID, CNAME Name, CCOLOR Color, CFLAVOR Flavor, CORIGIN Origin FROM BVG_COFFEE ORDER BY ID"
    cur.execute(sqlCmd)
    response = cur.fetchall()
    return_dict = {"items": {}}
    for item in response:
        return_dict["items"].update(
            {item[0]: {'Name': item[1], 'Color': item[2], 'Flavor': item[3], 'Origin': item[4]}})
    return return_dict


@app.get("/coffees/{coffee_id}")
def list_coffee_by_id(coffee_id: int):
    con, cur = get_db_cursor()
    cur.execute("SELECT CID FROM BVG_COFFEE WHERE CID=:1", (coffee_id, ))
    if bool(cur.fetchall()):
        return list_table_data()["items"][coffee_id]
    else:
        return {"ERROR": f"Coffee with the ID {coffee_id} does not exist."}


@app.delete("/coffees/delete/{coffee_id}")
def delete_coffee(coffee_id: str):
    con, cur = get_db_cursor()
    cur.execute("SELECT CID FROM BVG_COFFEE WHERE CID=:1", (coffee_id, ))
    if bool(cur.fetchall()):
        sqlCmd = "DELETE FROM BVG_COFFEE WHERE CID=:1"
        cur.execute(sqlCmd, (coffee_id, ))
        con.commit()
        close_db_cursor(con, cur)
        return {"Message": f"The coffee with the ID {coffee_id} has been deleted!"}
    else:
        return {"ERROR": f"Coffee with the ID {coffee_id} does not exist."}


@app.post("/coffees/add/{coffee_id}")
def add_new_row(coffee_id: int, coffee: Coffee):
    """This function adds a new row to the database."""
    con, cur = get_db_cursor()
    cur.execute("SELECT CID FROM BVG_COFFEE WHERE CID=:1", (coffee_id, ))
    if bool(cur.fetchall()):
        sqlCmd = "INSERT INTO BVG_COFFEE VALUES (:1, :2, :3, :4, :5)"
        cur.execute(sqlCmd,  (coffee_id, coffee.name,
                    coffee.color, coffee.flavor, coffee.origin))
        con.commit()
        close_db_cursor(con, cur)
        return {"Message": f"The coffee {coffee.name} has been added!"}
    else:
        return {"ERROR": "A coffee with this ID already exists."}


@app.put("/coffees/update/{coffee_id}")
def update_coffee(coffee_id: int, coffe: UpdateCoffee):
    con, cur = get_db_cursor()
    cur.execute("SELECT CID FROM BVG_COFFEE WHERe CID=:1", (coffee_id, ))
    if bool(cur.fetchall()):
        if coffe.name is not None:
            sqlCmd = "UPDATE BVG_COFFEE SET CNAME=:1 WHERE CID=:2"
            cur.execute(sqlCmd, (coffe.name, coffee_id))
            con.commit()
        elif coffe.color is not None:
            sqlCmd = "UPDATE BVG_COFFEE SET CCOLOR=:1 WHERE CID=:2"
            cur.execute(sqlCmd, (coffe.color, coffee_id))
            con.commit()
        elif coffe.flavor is not None:
            sqlCmd = "UPDATE BVG_COFFEE SET CFLAVOR=:1 WHERE CID=:2"
            cur.execute(sqlCmd, (coffe.flavor, coffee_id))
            con.commit()
        elif coffe.origin is not None:
            sqlCmd = "UPDATE BVG_COFFEE SET CORIGIN=:1 WHERE CID=:2"
            cur.execute(sqlCmd, (coffe.origin, coffee_id))
            con.commit()
        close_db_cursor(con, cur)
        return {"Message": 'The coffee has been updated!'}
    else:
        return {"Error": f"Coffee with the ID {coffee_id} does not exist."}
