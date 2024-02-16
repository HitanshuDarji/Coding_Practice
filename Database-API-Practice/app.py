from fastapi import FastAPI
import cx_Oracle
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)


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
    close_db_cursor(con, cur)
    return_dict = {"items": {}}
    for item in response:
        return_dict["items"].update(
            {item[0]: {'id': item[0], 'Name': item[1], 'Color': item[2], 'Flavor': item[3], 'Origin': item[4]}})
    return return_dict


@app.get("/coffees/{coffee_id}")
def list_coffee_by_id(coffee_id: int):
    con, cur = get_db_cursor()
    cur.execute("SELECT CID FROM BVG_COFFEE WHERE CID=:1", (coffee_id, ))
    if bool(cur.fetchall()):
        return list_table_data()["items"][coffee_id]
    else:
        return {"ERROR": f"Coffee with the ID {coffee_id} does not exist."}


@app.get("/coffees/byname/{coffee_name}")
def list_coffee_by_name(coffee_name: str):
    con, cur = get_db_cursor()
    cur.execute("SELECT CNAME FROM BVG_COFFEE WHERE CNAME=:1", (coffee_name, ))
    if bool(cur.fetchall()):
        cur.execute("SELECT * FROM BVG_COFFEE WHERE LOWER(CNAME)=LOWER(:1) OR LOWER(CNAME)=LOWER(:1) OR LOWER(CNAME)=LOWER(:1) OR LOWER(CNAME)=LOWER(:1)",
                    (coffee_name, ))
        cname = cur.fetchall()
        close_db_cursor(con, cur)
        return {"Name": f"{cname}"}
    else:
        return {"ERROR": f"Coffee with the ID {coffee_name} does not exist."}


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


@app.post("/coffees/add")
def add_new_row(coffee: Coffee):
    """This function adds a new row to the database."""
    con, cur = get_db_cursor()
    sqlCmd = "INSERT INTO BVG_COFFEE VALUES (coffee_seq.NEXTVAL, :1, :2, :3, :4)"
    cur.execute(sqlCmd,  (coffee.name,
                coffee.color, coffee.flavor, coffee.origin))
    con.commit()
    close_db_cursor(con, cur)
    return {"Message": f"The coffee {coffee.name} has been added!"}


@app.put("/coffees/update/{coffee_id}")
def update_coffee(coffee_id: int, coffee: UpdateCoffee):
    con, cur = get_db_cursor()
    cur.execute("SELECT CID FROM BVG_COFFEE WHERE CID=:1", (coffee_id, ))
    if bool(cur.fetchall()):
        sqlCmd = "UPDATE BVG_COFFEE SET CNAME=:1, CCOLOR=:2, CFLAVOR=:3, CORIGIN=:4 WHERE CID=:2"
        cur.execute(sqlCmd, (coffee.name, coffee.color,
                    coffee.flavor, coffee.origin, coffee_id))
        con.commit()
        close_db_cursor(con, cur)
        return {"Message": 'The coffee has been updated!'}
    else:
        return {"Error": f"Coffee with the ID {coffee_id} does not exist."}
