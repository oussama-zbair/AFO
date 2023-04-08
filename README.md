## Automatic File Organizer
This is a Python script that can automatically organize files in a specified folder based on their file type. The script uses a dictionary to map each file type to its respective folder name and moves files to the corresponding folder.

### Installation
To use the automatic file organizer script, you need to have Python 3 installed on your system. You can download Python from the official website here.

You also need to have the following Python modules installed:

- os
- shutil

You can install these modules using pip by running the following command in your terminal:

```bash
pip install os shutil
```
### Usage
To use the automatic file organizer script, follow these steps:

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/<username>/<repository-name>.git
```

2. Navigate to the directory containing the script using the following command:

```bash
cd <repository-name>
```

3. Edit the script to specify the folder path that you want to organize.
4. Run the script using the following command:

```bash
python organizer.py
```

5. The script will automatically organize the files in the specified folder based on their file type.

### Customization
You can customize the automatic file organizer script to suit your needs by modifying the following:

- **File types:** You can add or remove file types from the **file_types** dictionary in the **move_file()** function.
- **Folder names:** You can modify the folder names in the **file_types** dictionary to match your preferred folder names.

### Contributing:
If you find any issues with the automatic file organizer script or have suggestions for improvement, feel free to open an issue or create a pull request.

### License:
This project is licensed under the MIT License - see the LICENSE file for details.
