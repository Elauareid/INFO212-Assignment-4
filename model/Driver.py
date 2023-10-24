from neo4j import GraphDatabase, Driver

URI = "neo4j+s://1d9eb7a2.databases.neo4j.io:7687"
AUTH = ("neo4j", "GB2CSsX2B-dgthvoGxcaStQD1t1AoO0vVClJeSuh0rI")

def _get_connection() -> Driver:
    try:
        driver = GraphDatabase.driver(URI, auth=AUTH)
        driver.verify_connectivity()
        return driver
    except Exception as e:
        print(f"Error: ",e)
        return None