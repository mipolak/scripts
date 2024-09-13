import os
import sys

def create_ansible_role(role_name):
    # Define the structure of the Ansible role
    directories = {
        'vars': os.path.join(role_name, 'vars'),
        'tasks': os.path.join(role_name, 'tasks'),
        'handlers': os.path.join(role_name, 'handlers'),
        'files': os.path.join(role_name, 'files')
    }
    
    # Create the directories and main.yml files
    for subfolder, path in directories.items():
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")
        
        # Create main.yml file for specific subfolders
        if subfolder in ['vars', 'tasks', 'handlers']:
            main_yml_path = os.path.join(path, 'main.yml')
            with open(main_yml_path, 'w') as main_yml_file:
                main_yml_file.write(f"---\n# {subfolder} - {role_name}\n")
                print(f"Created file: {main_yml_path}")
    
    # Create the README.md file
    readme_path = os.path.join(role_name, 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(f"# {role_name} Role\n\nThis role is used to...\n")
        print(f"Created file: {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_ansible_role.py <role_name>")
        sys.exit(1)

    role_name = sys.argv[1]
    create_ansible_role(role_name)
