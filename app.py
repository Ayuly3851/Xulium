from application import create_app

sockeio, app = create_app()

if __name__ == '__main__':
	sockeio.run(app, debug = True)
