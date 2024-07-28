import sqlite3



def main():
    db_path = "tracked_files.db"
    table_name = "tracked_files"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    create_tracked_files_table(cursor, table_name=table_name)

    conn.commit()
    conn.close()


def create_tracked_files_table(cursor, table_name="tracked_files"):
    try:
        cursor.execute(
            """
            CREATE TABLE tracked_files (
                inode INTEGER PRIMARY KEY,
                file_path TEXT NOT NULL,
                alias TEXT
            );
            """
        )
        print("Table 'tracked_files' was successfully created.")
    except sqlite3.Error as e:
        if 'already exists' in str(e):
            print(f"Table '{table_name}' already exists.")
        else:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
