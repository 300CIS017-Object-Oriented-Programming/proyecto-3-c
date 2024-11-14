# firebase_config.py
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBb56zEaGWMy1yRz0hwtFaZs-uWnKMFVN8",
  "authDomain": "proyectweb-1c925.firebaseapp.com",
  "databaseURL": "",  # Agrega la URL de la base de datos si es necesaria
  "projectId": "proyectweb-1c925",
  "storageBucket": "proyectweb-1c925.appspot.com",  # Cambiar firebasestorage.app a appspot.com
  "messagingSenderId": "1067849312119",
  "appId": "1:1067849312119:web:397ad0d3ff8b5c346de372",
  "measurementId": "G-75BYLPX6M5"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()