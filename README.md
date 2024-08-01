
# 📁 File System Monitor

This project provides useful scripts to keep track of files (moved, renamed, deleted) in a filesystem. It can be extended with sqlite3 to gain database superpowers and keep track of a selection of files only in the most efficient way.

## Features
- 🔍 Monitors file system changes such as moves, renames, and deletions.
- 🗂️ Tracks file metadata using an SQLite database.
- ⚡ Efficiently updates file paths in the database when files are moved or renamed.
- 🛠️ Can be configured to monitor specific directories.

## Requirements
- Python 3.x
- sqlite3
- inotify_simple

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Initialize the Database:**

   Before running the monitor script, you need to initialize the SQLite database and create the necessary table for tracking files. Run the following command:
   ```sh
   python database_utils.py
   ```

2. **Start Monitoring:**

   To start monitoring the file system for changes, run the monitor script:
   ```sh
   python monitor_files.py
   ```

   By default, this will monitor the directory where the script is located. You can change the directory by modifying the `root` parameter in the `monitor_files` function.

## Script Details

- **database_utils.py:**
  - Responsible for setting up the SQLite database and creating the table for tracking files.

- **monitor_files.py:**
  - Monitors the filesystem for changes using inotify and updates the database accordingly.

## Notes
- ⚠️ Ensure that the directory you want to monitor has the necessary read/write permissions.
- 🛠️ You can modify the `DATABASE_PATH` and `TABLE_NAME` variables in the scripts to customize the database location and table name.

## License
This project is licensed under the MIT License.
