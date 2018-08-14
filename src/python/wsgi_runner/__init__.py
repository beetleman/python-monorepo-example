import gunicorn.app.base
import multiprocessing


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


DEFAULT_OPTIONS = {
    'bind': '%s:%s' % ('127.0.0.1', '8080'),
    'workers': number_of_workers(),
}


def run(app, options=None):
    if options is None:
        options = {}
    options = dict(DEFAULT_OPTIONS, **options)
    StandaloneApplication(app, options).run()
