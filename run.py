from app import ProfileApp

def main() -> None:
    ProfileApp().run()
    ProfileApp().init_db()

if __name__ == '__main__':
    main()