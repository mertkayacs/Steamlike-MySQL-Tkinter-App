<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/svg/steamlike-logo-on-dark.svg">
    <img src="docs/brand/svg/steamlike-logo-on-light.svg" alt="Steamlike" width="260">
  </picture>
</p>

<h1 align="center">A Steam-style game store in Tkinter.<br>Backed by MySQL.</h1>

<p align="center">
  Database course project from 2020: a desktop game store with user, developer and admin pages.<br>
  <b>Python, Tkinter and MySQL in one application file.</b>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white">
  <img alt="GUI: Tkinter" src="https://img.shields.io/badge/GUI-Tkinter-5B2A36?style=flat-square">
  <img alt="Coursework, 2020" src="https://img.shields.io/badge/project-coursework%202020-5B2A36?style=flat-square">
  <a href="https://github.com/mertkayacs/Steamlike-MySQL-Tkinter-App"><img alt="GitHub stars" src="https://img.shields.io/github/stars/mertkayacs/Steamlike-MySQL-Tkinter-App?style=flat-square&logo=github&color=8A6D3B"></a>
</p>

<p align="center">
  <a href="#quick-start"><img alt="Quick start" src="https://img.shields.io/badge/Quick%20start-5B2A36?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNMTIgMTV2NXMzLjAzLS41NSA0LTJjMS4wOC0xLjYyIDAtNSAwLTUiLz48cGF0aCBkPSJNNC41IDE2LjVjLTEuNSAxLjI2LTIgNS0yIDVzMy43NC0uNSA1LTJjLjcxLS44NC43LTIuMTMtLjA5LTIuOTFhMi4xOCAyLjE4IDAgMCAwLTIuOTEtLjA5Ii8%2BPHBhdGggZD0iTTkgMTJhMjIgMjIgMCAwIDEgMi0zLjk1QTEyLjg4IDEyLjg4IDAgMCAxIDIyIDJjMCAyLjcyLS43OCA3LjUtNiAxMWEyMi40IDIyLjQgMCAwIDEtNCAyeiIvPjxwYXRoIGQ9Ik05IDEySDRzLjU1LTMuMDMgMi00YzEuNjItMS4wOCA1IC4wNSA1IC4wNSIvPjwvZz48L3N2Zz4%3D&logoColor=white"></a>
  <a href="Steamlike%20App/project%20report/Database%20Project%20Report.pdf"><img alt="Project report" src="https://img.shields.io/badge/Project%20report-1E2A38?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNNiAyMmEyIDIgMCAwIDEtMi0yVjRhMiAyIDAgMCAxIDItMmg4YTIuNCAyLjQgMCAwIDEgMS43MDQuNzA2bDMuNTg4IDMuNTg4QTIuNCAyLjQgMCAwIDEgMjAgOHYxMmEyIDIgMCAwIDEtMiAyeiIvPjxwYXRoIGQ9Ik0xNCAydjVhMSAxIDAgMCAwIDEgMWg1Ii8%2BPHBhdGggZD0iTTEwIDlIOCIvPjxwYXRoIGQ9Ik0xNiAxM0g4Ii8%2BPHBhdGggZD0iTTE2IDE3SDgiLz48L2c%2BPC9zdmc%2B&logoColor=white"></a>
  <a href="Steamlike%20App/src/application.py"><img alt="Source" src="https://img.shields.io/badge/Source-1E2A38?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNNiAyMmEyIDIgMCAwIDEtMi0yVjRhMiAyIDAgMCAxIDItMmg4YTIuNCAyLjQgMCAwIDEgMS43MDQuNzA2bDMuNTg4IDMuNTg4QTIuNCAyLjQgMCAwIDEgMjAgOHYxMmEyIDIgMCAwIDEtMiAyeiIvPjxwYXRoIGQ9Ik0xNCAydjVhMSAxIDAgMCAwIDEgMWg1Ii8%2BPHBhdGggZD0iTTEwIDEyLjUgOCAxNWwyIDIuNSIvPjxwYXRoIGQ9Im0xNCAxMi41IDIgMi41LTIgMi41Ii8%2BPC9nPjwvc3ZnPg%3D%3D&logoColor=white"></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/hero-dark.webp">
    <img src="docs/assets/readme/hero-light.webp" alt="Steamlike store page listing games with prices and discounts, next to a credit balance and a Buy the Selected Game button" width="960">
  </picture>
</p>

Steamlike is a Steam-style game store built as a database course project in 2020. It is a Tkinter desktop app on top of a MySQL database, with separate pages for users, game developers and admins, plus a raw SQL console. Users buy games with credit, developers publish games and mods, and admins can ban accounts. A scanned project report in the repository describes the table design.

---

## Why Steamlike

Each role in the app maps to a page and a set of tables.

|  |  |
|---|---|
| <img src="docs/assets/readme/icons/store.svg" width="18" height="18" alt=""> **A store with discounts** | Users sign up, add credit and buy games from a store page that applies discounts. |
| <img src="docs/assets/readme/icons/users.svg" width="18" height="18" alt=""> **Three roles** | Users, developers and admins have their own login pages. Admins ban users permanently or until a date picked in the calendar. |
| <img src="docs/assets/readme/icons/gamepad-2.svg" width="18" height="18" alt=""> **Playtime, ratings and mods** | Users track hours played, rate games, install or uninstall mods and share games with friends. |
| <img src="docs/assets/readme/icons/database.svg" width="18" height="18" alt=""> **A real schema** | The app talks to a MySQL database through mysql-connector-python. The report PDF documents the tables. |

## A quick tour

<table>
  <tr>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/tour/mygames-dark.webp">
        <img src="docs/assets/readme/tour/mygames-light.webp" alt="Steamlike My Games page with a list of owned games and buttons for mods, playtime and rating">
      </picture>
      <h3>My games</h3>
      Owned games with mod install and uninstall buttons, hours played and a rating field.
    </td>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/tour/developer-dark.webp">
        <img src="docs/assets/readme/tour/developer-light.webp" alt="Steamlike developer page showing username, revenue and Add Game and My Games buttons">
      </picture>
      <h3>Developer page</h3>
      A developer sees their revenue and can add games or open their own list.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/tour/addgame-dark.webp">
        <img src="docs/assets/readme/tour/addgame-light.webp" alt="Steamlike game adding form with fields for title, RAM, graphics card, OS, platform, series, discount and price">
      </picture>
      <h3>Add a game</h3>
      Developers enter title, hardware requirements, platform, series, discount and price.
    </td>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/tour/sql-dark.webp">
        <img src="docs/assets/readme/tour/sql-light.webp" alt="Steamlike query page showing a select statement and the resulting game table rows">
      </picture>
      <h3>SQL console</h3>
      A query page runs raw SQL against the database and prints the rows.
    </td>
  </tr>
</table>

<p align="center"><sub>Screenshots show the app running against test data from the 2020 course project.</sub></p>

## Features

**Users**

- Sign up, add credit, buy games with discounts.
- My Games page with playtime, ratings and mods.
- Friends list with family share.

**Developers**

- Add games, achievements and mods.
- See revenue.

**Admins**

- Ban users permanently or until a selected date.

**Tools**

- SQL query console for raw statements.

## Quick start

```sh
pip install mysql-connector-python Pillow tkcalendar
```

The app expects a MySQL server on localhost with a database named `steamdb`, user `root` and the password in the `STEAMDB_PASSWORD` environment variable. The schema is not included as SQL in the repository, so recreate the tables from the project report first.

```sh
export STEAMDB_PASSWORD=your_mysql_root_password
cd "Steamlike App/src"
python application.py
```

Run it from the src folder, because the app loads steama.jpg by a relative path.

### Requirements

- Python 3 with Tkinter.
- MySQL on localhost.
- mysql-connector-python, Pillow and tkcalendar.

## FAQ

<details>
<summary><b>Which database do I need?</b></summary>

MySQL on localhost with a database named steamdb. The root password comes from STEAMDB_PASSWORD.
</details>

<details>
<summary><b>Where is the schema?</b></summary>

Only a sample INSERT statement is in the repository. The scanned report describes the tables.
</details>

<details>
<summary><b>Why run it from the src folder?</b></summary>

The logo steama.jpg loads by a relative path.
</details>

<details>
<summary><b>Is it maintained?</b></summary>

No. It is a 2020 database course project.
</details>

If Steamlike is useful to you, a ⭐ helps other people find it.

Photos behind the screenshots are credited in [docs/assets/readme/CREDITS.md](docs/assets/readme/CREDITS.md).

[![views](https://hits.sh/github.com/mertkayacs/Steamlike-MySQL-Tkinter-App.svg?view=today-total&style=flat-square&label=views&color=5B2A36&labelColor=1E2A38)](https://github.com/mertkayacs/Steamlike-MySQL-Tkinter-App)
