from website import create_app

if __name__ == "__main__":
    app = create_app() #function from __init__.py
    app.run(debug=True)