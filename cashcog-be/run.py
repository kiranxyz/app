class Application:
    def __init__(self):
        self._app = None

    def init(self):
        from xcnt.cashcog import init_app

        self._app = init_app()

    def app(self, environ, start_response):
        if self._app is None:
            self.init()

        return self._app(environ, start_response)


application = Application().app


if __name__ == '__main__':
    from xcnt.cashcog.cli import cli

    cli()