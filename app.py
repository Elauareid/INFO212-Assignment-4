from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
from flask import Flask, render_template, redirect, request

URI = "neo4j+s://1d9eb7a2.databases.neo4j.io:7687"
AUTH = ("neo4j", "GB2CSsX2B-dgthvoGxcaStQD1t1AoO0vVClJeSuh0rI")

app = Flask(__name__)

