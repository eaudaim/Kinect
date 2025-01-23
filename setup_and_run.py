import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Helper function to run shell commands."""
    try:
        subprocess.run(command, shell=True, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {command}")
        sys.exit(1)

def install_dependencies():
    """Install dependencies from requirements.txt."""
    print("Installation des dépendances depuis requirements.txt...")
    run_command("pip install -r requirements.txt")

def install_freenect():
    """Install freenect from the local setup.py."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    freenect_path = os.path.join(current_dir, "libfreenect", "wrappers", "python")
    
    if not os.path.exists(freenect_path):
        print(f"Le chemin {freenect_path} n'existe pas. Clonez le dépôt libfreenect dans ce dossier.")
        sys.exit(1)

    print("Installation de freenect via setup.py...")
    run_command("sudo python3 setup.py install", cwd=freenect_path)

def launch_scanner():
    """Launch the main scanner script."""
    print("Lancement du script scanner3D_kinect.py...")
    run_command("python3 scanner3D_kinect.py")

if __name__ == "__main__":
    print("Configuration initiale...")
    install_dependencies()
    install_freenect()
    launch_scanner()

