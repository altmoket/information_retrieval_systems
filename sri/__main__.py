from .containers import SriContainer



if __name__ == "__main__":
    app = SriContainer()
    app.config.from_ini('./config.ini', required=True)


