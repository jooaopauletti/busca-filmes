from dotenv import load_dotenv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('OMDB_API_KEY')