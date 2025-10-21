from app import ProfileApp

def main() -> None:
    ProfileApp().init_db()
    ProfileApp().run()

if __name__ == '__main__':
    main()