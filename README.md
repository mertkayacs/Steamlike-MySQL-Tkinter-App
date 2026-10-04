# Steamlike-MySQL-Tkinter-App

A Steam-like game store desktop app built as a database course project. It is a Tkinter GUI on top of a MySQL database, with separate pages for users, game developers, admins, and a raw SQL query console.

Users can sign up, buy games from a store page (with discounts applied), add credit, rate games, track playtime, and install or uninstall mods. Developers can add games, achievements, and mods, and see their revenue. Admins can ban users permanently or until a selected date.

## How to run

Dependencies: Python 3 with `mysql-connector-python`, `Pillow`, and `tkcalendar` installed (Tkinter ships with most Python installs). There is no requirements file in the repo.

```
pip install mysql-connector-python Pillow tkcalendar
```

The app expects a MySQL server on localhost with a database named `steamdb`, user `root`, and the password read from the `STEAMDB_PASSWORD` environment variable. The schema is not included as SQL DDL in the repo (the only `.sql` file is a sample INSERT), so the tables must be recreated before the app can connect. The scanned project report under `Steamlike App/project report/` describes the table design.

With the database in place:

```
export STEAMDB_PASSWORD=your_mysql_root_password
cd "Steamlike App/src"
python application.py
```

Running from the `src` directory is required because the app loads `steama.jpg` by relative path.

## Screenshots

![Main window](Steamlike%20App/screenshots/unknown.png)

![Store page](Steamlike%20App/screenshots/unknown%20(3).png)

![User signup](Steamlike%20App/screenshots/unknown%20(7).png)

![Developer game adding page](Steamlike%20App/screenshots/unknown%20(10).png)

![Admin page](Steamlike%20App/screenshots/unknown%20(13).png)

## Tech used

- Python 3
- Tkinter (GUI)
- MySQL via mysql-connector-python
- Pillow (image loading)
- tkcalendar (date picker on the admin page)

## Status

Coursework, 2020. Not maintained.
