from app.main import app
import fastwsgi

if __name__ == "__main__":
  fastwsgi.run(wsgi_app=app, host='0.0.0.0', port=5000)
