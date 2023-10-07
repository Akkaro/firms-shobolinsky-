from website import create_app

app = create_app()

if __name__ == '__main__': # run the app only if we inted to run it, if we import don't
    app.run(debug=True) # at every change rerun the webserver
    
