import sqlite3

# Connects to the database
def connect_db():
    conn = sqlite3.connect('cat_care.db')
    conn.row_factory = sqlite3.Row  # Access results by column name
    return conn

# Fetches cat data with proper column aliases
def fetch_cats():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Query with column aliases for consistent column names
    query = """
    SELECT 
        cats.name AS name, 
        cat_species.species_name AS species_name, 
        cats.weight AS weight
    FROM cats
    JOIN cat_species ON cats.species_id = cat_species.species_id
    """
    
    print("Running query...")  # Debugging message
    cursor.execute(query)  # Execute SQL query
    cats = cursor.fetchall()  # Fetch results
    
    print(f"Fetched {len(cats)} rows")  # Debugging: Check row count
    
    conn.close()
    return cats


def add_cat():
    conn = connect_db()
    cursor = conn.cursor()

    # User input
    name = input("Enter cat's name: ")
    species = input("Enter cat's species (Maine Coon, Siamese, Persian, Bengal): ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    weight = float(input("Enter weight (kg): "))
    picture = input("Enter profile picture filename: ")

    # Get species_id based on user selection
    cursor.execute("SELECT species_id FROM cat_species WHERE species_name = ?", (species,))
    result = cursor.fetchone()

    if result:
        species_id = result['species_id']
        # Insert new cat
        cursor.execute("""
            INSERT INTO cats (user_id, name, species_id, date_of_birth, weight, profile_picture)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (1, name, species_id, dob, weight, picture))
        conn.commit()
        print(f"{name} has been added successfully!")
    else:
        print("Invalid species name. Please try again.")

    conn.close()

def check_overweight():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    SELECT cats.name, cat_species.species_name, cats.weight, health_metrics.normal_weight_max
    FROM cats 
    JOIN cat_species ON cats.species_id = cat_species.species_id
    JOIN health_metrics ON cats.species_id = health_metrics.species_id
    WHERE cats.weight > health_metrics.normal_weight_max
    """
    cursor.execute(query)
    overweight_cats = cursor.fetchall()
    conn.close()
    return overweight_cats
    
def check_reminders():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    SELECT cats.name, grooming.last_nail_cut 
    FROM cats 
    JOIN grooming ON cats.cat_id = grooming.cat_id
    WHERE grooming.last_nail_cut <= date('now', '-30 days')
    """
    cursor.execute(query)
    reminders = cursor.fetchall()
    conn.close()
    return reminders

# Main execution block
if __name__ == "__main__":
    while True:
        print("\n--- Cat Care Management ---")
        print("1. View All Cats")
        print("2. Add a New Cat")
        print("3. Check Overweight Cats")
        print("4. Check Grooming Reminders")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            cats = fetch_cats()
            for cat in cats:
                print(f"{cat['name']} - {cat['species_name']} - {cat['weight']} kg")
        elif choice == "2":
            add_cat()
        elif choice == "3":
            overweight = check_overweight()
            for cat in overweight:
                print(f"{cat['name']} ({cat['species_name']}) is overweight at {cat['weight']} kg")
        elif choice == "4":
            reminders = check_reminders()
            for reminder in reminders:
                    print(f"{reminder['name']} needs a nail trim (Last done: {reminder['last_nail_cut']})")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

