import sqlite3

def create_superhero_calendar():
    conn = sqlite3.connect('superhero_calendar.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS superhero_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        hero_name TEXT NOT NULL,
        event_name TEXT NOT NULL,
        universe TEXT NOT NULL,
        description TEXT
    );
    ''')

    events = [
        # DC Comics
        ('1938-06-01', 'Superman', 'First Appearance in Action Comics #1', 'DC',
         'Superman debuted in Action Comics #1, marking the start of the superhero genre.'),
        ('1940-05-01', 'Batman', 'First Appearance of The Joker and Catwoman', 'DC',
         'The Joker and Catwoman made their first appearances in Batman #1.'),
        ('1940-07-01', 'Robin', 'First Appearance in Detective Comics #38', 'DC',
         'Dick Grayson debuted as Robin, Batman’s sidekick.'),
        ('1941-12-01', 'Wonder Woman', 'First Appearance in All Star Comics #8', 'DC',
         'Wonder Woman made her first appearance, introducing one of the first female superheroes.'),
        ('1956-10-01', 'The Flash (Barry Allen)', 'First Appearance in Showcase #4', 'DC',
         'Barry Allen debuted as The Flash, ushering in the Silver Age of Comics.'),
        ('1960-03-01', 'Justice League', 'First Appearance in The Brave and the Bold #28', 'DC',
         'The Justice League of America debuted, featuring DC’s greatest heroes.'),
        ('1985-04-01', 'Crisis on Infinite Earths', 'Start of DC Universe Redefinition', 'DC',
         'Crisis on Infinite Earths began, rebooting the DC Universe.'),
        ('1993-11-18', 'Superman', 'The Death of Superman', 'DC',
         'Superman died in the iconic story "The Death of Superman".'),
        # Marvel Comics
        ('1961-11-01', 'Fantastic Four', 'First Appearance in Fantastic Four #1', 'Marvel',
         'The Fantastic Four debuted, launching the Marvel Universe.'),
        ('1962-08-01', 'Spider-Man', 'First Appearance in Amazing Fantasy #15', 'Marvel',
         'Spider-Man debuted in Amazing Fantasy #15, created by Stan Lee and Steve Ditko.'),
        ('1963-07-01', 'X-Men', 'First Appearance in X-Men #1', 'Marvel',
         'The X-Men debuted as Marvel’s team of mutants.'),
        ('1963-09-01', 'Iron Man', 'First Appearance in Tales of Suspense #39', 'Marvel',
         'Iron Man debuted in Tales of Suspense #39.'),
        ('1963-09-01', 'The Avengers', 'First Appearance in The Avengers #1', 'Marvel',
         'The Avengers debuted, bringing together Marvel’s greatest heroes.'),
        ('1966-07-01', 'Black Panther', 'First Appearance in Fantastic Four #52', 'Marvel',
         'Black Panther debuted as the first major Black superhero in comics.'),
        ('1974-10-01', 'Wolverine', 'First Appearance in The Incredible Hulk #180', 'Marvel',
         'Wolverine made his first appearance in The Incredible Hulk #180.'),
        ('2006-07-01', 'Civil War', 'Marvel Comics Civil War Begins', 'Marvel',
         'Civil War divided the Marvel Universe, pitting hero against hero.'),
        # Cross-Media Events
        ('1978-12-15', 'Superman', 'Superman: The Movie Premiere', 'DC',
         'The first major superhero film, starring Christopher Reeve, premiered.'),
        ('2008-05-02', 'Iron Man', 'Iron Man Movie Premiere', 'Marvel',
         'Iron Man premiered, launching the Marvel Cinematic Universe.'),
        ('2012-05-04', 'The Avengers', 'The Avengers Movie Premiere', 'Marvel',
         'The Avengers premiered, uniting Marvel’s heroes on the big screen.')
    ]

    cursor.executemany('''
    INSERT INTO superhero_events (date, hero_name, event_name, universe, description)
    VALUES (?, ?, ?, ?, ?);
    ''', events)

    conn.commit()
    conn.close()

    print("Database created and populated with superhero events!")


#databases for each superhero - recommended + info
def create_database(hero_name, comics):
    db_name = f"{hero_name}_comics.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {hero_name}_reading_order (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        issue INTEGER,
        year INTEGER NOT NULL,
        description TEXT
    );
    ''')

    cursor.executemany(f'''
    INSERT INTO {hero_name}_reading_order (title, issue, year, description)
    VALUES (?, ?, ?, ?);
    ''', comics)

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created with reading order for {hero_name.capitalize()}.")

def create_hero_info_database(hero_name, hero_info):
    db_name = f"{hero_name}_info.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {hero_name}_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        studio TEXT NOT NULL,
        first_appearance TEXT NOT NULL,
        main_villains TEXT NOT NULL,
        abilities TEXT NOT NULL
    );
    ''')

    cursor.execute(f'''
    INSERT INTO {hero_name}_info (studio, first_appearance, main_villains, abilities)
    VALUES (?, ?, ?, ?);
    ''', hero_info)

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created with info for {hero_name.capitalize()}.")


def create_batman():
    comics = [
        ("Detective Comics", 27, 1939, "First appearance of Batman."),
        ("Batman", 1, 1940, "First issue of Batman's solo series."),
        ("The Dark Knight Returns", None, 1986, "Frank Miller's iconic reimagining of Batman."),
        ("Year One", None, 1987, "The definitive origin story of Batman."),
        ("The Killing Joke", None, 1988, "Exploration of the Joker's backstory.")
    ]
    create_database("batman", comics)

    hero_info = (
        "DC",
        "Detective Comics #27 (1939)",
        "Joker, Riddler, Bane",
        "Peak human physical and mental abilities, martial arts, detective skills"
    )
    create_hero_info_database("batman", hero_info)

def create_superman():
    comics = [
        ("Action Comics", 1, 1938, "First appearance of Superman."),
        ("Superman", 1, 1939, "First issue of Superman's solo series."),
        ("For All Seasons", None, 1998, "A heartfelt look at Superman's life."),
        ("All-Star Superman", None, 2005, "Grant Morrison's acclaimed take on Superman."),
        ("Red Son", None, 2003, "What if Superman landed in the Soviet Union?")
    ]
    create_database("superman", comics)

    hero_info = (
        "DC",
        "Action Comics #1 (1938)",
        "Lex Luthor, General Zod, Doomsday",
        "Super strength, flight, invulnerability, heat vision"
    )
    create_hero_info_database("superman", hero_info)

def create_spiderman():
    comics = [
        ("Amazing Fantasy", 15, 1962, "First appearance of Spider-Man."),
        ("The Amazing Spider-Man", 1, 1963, "First issue of Spider-Man's solo series."),
        ("The Night Gwen Stacy Died", None, 1973, "One of the most pivotal Spider-Man stories."),
        ("Kraven's Last Hunt", None, 1987, "Dark and intense Spider-Man tale."),
        ("Ultimate Spider-Man", 1, 2000, "Modern retelling of Spider-Man's origin.")
    ]
    create_database("spiderman", comics)

    hero_info = (
        "Marvel",
        "Amazing Fantasy #15 (1962)",
        "Green Goblin, Doctor Octopus, Venom",
        "Super strength, agility, spider-sense, web-shooting"
    )
    create_hero_info_database("spiderman", hero_info)

def create_ironman():
    comics = [
        ("Tales of Suspense", 39, 1963, "First appearance of Iron Man."),
        ("Iron Man", 1, 1968, "First issue of Iron Man's solo series."),
        ("Demon in a Bottle", None, 1979, "Exploration of Tony Stark's struggles with alcoholism."),
        ("Extremis", None, 2005, "Reimagining of Iron Man for the modern era."),
        ("The Invincible Iron Man", 1, 2008, "New series after the success of the Iron Man movie.")
    ]
    create_database("ironman", comics)

    hero_info = (
        "Marvel",
        "Tales of Suspense #39 (1963)",
        "Mandarin, Obadiah Stane, Justin Hammer",
        "Genius intellect, powered armor suit, advanced weaponry"
    )
    create_hero_info_database("ironman", hero_info)

def create_avengers():
    comics = [
        ("The Avengers", 1, 1963, "First appearance of The Avengers."),
        ("Avengers: Under Siege", None, 1986, "The Masters of Evil nearly destroy the Avengers."),
        ("Infinity Gauntlet", None, 1991, "Epic crossover featuring Thanos."),
        ("Civil War", None, 2006, "Avengers are divided over the Superhuman Registration Act."),
        ("Avengers: Endgame Prelude", None, 2019, "Prelude comic to the MCU's epic finale.")
    ]
    create_database("avengers", comics)

    hero_info = (
        "Marvel",
        "The Avengers #1 (1963)",
        "Thanos, Loki, Ultron",
        "Team of superheroes with diverse powers and abilities"
    )
    create_hero_info_database("avengers", hero_info)

def create_justice_league():
    comics = [
        ("The Brave and the Bold", 28, 1960, "First appearance of the Justice League."),
        ("Justice League of America", 1, 1960, "First issue of JLA's solo series."),
        ("Crisis on Infinite Earths", None, 1985, "Multiverse-altering crossover."),
        ("The New Frontier", None, 2004, "Reimagining of the Justice League's early days."),
        ("Justice League", 1, 2011, "Rebooted series from The New 52.")
    ]
    create_database("justice_league", comics)

    hero_info = (
        "DC",
        "The Brave and the Bold #28 (1960)",
        "Darkseid, Brainiac, Starro",
        "Team of superheroes with diverse abilities, united to protect Earth"
    )
    create_hero_info_database("justice_league", hero_info)


'''
if __name__ == "__main__":
    create_batman()
    create_superman()
    create_justice_league()
    create_spiderman()
    create_ironman()
    create_avengers()
    create_superhero_calendar()
'''
