from contextlib import contextmanager
import time

@contextmanager
def timer(name:str):
    start = time.time()
    print(f"{name} started...")
    yield
    end =time.time()
    print(f"{name} finished in {end-start:.2f}s")


# Test
with timer("Loading students"):
    time.sleep(1)

with timer("Generating report"):
    time.sleep(0.5)


#---

@contextmanager
def database_connection(db_name:str):
    # Setup -stimulate opening connection
    print(f"opening connection to {db_name}")
    connection = {"db": db_name, "status":"connected"}

    yield connection # here code gets the connection objects

    #Teardown - stimulate closing connection

    connection["status"] = "closed"
    print(f"Connection to {db_name} closed")

with database_connection("institura_db") as conn:
    print(f"Using connection: {conn}")
    print(f"Querying students from {conn["db"]}")