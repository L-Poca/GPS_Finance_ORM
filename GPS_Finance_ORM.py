import requests
import tkinter as tk

def get_github_version(repo_url):
    api_url = f"{repo_url}/releases/latest"
    response = requests.get(api_url)
    if response.status_code == 200:
        version = response.json()["tag_name"]
        return version
    else:
        return None

def check_version():
    repo_url = entry.get()
    version = get_github_version(repo_url)

    if version:
        result_label.config(text=f"La version la plus récente de votre programme est : {version}")
    else:
        result_label.config(text="Impossible de récupérer la version depuis GitHub.")

# Create the GUI window
window = tk.Tk()
window.title("GitHub Version Checker")

# Create a label and an entry field for the repository URL
url_label = tk.Label(window, text="Repository URL:")
url_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to check the version
check_button = tk.Button(window, text="Check Version", command=check_version)
check_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()