import subprocess
import shutil
import git
import json

def install_go():
    subprocess.run("wget https://go.dev/dl/go1.19.2.linux-amd64.tar.gz", check=True)
    subprocess.run("sudo rm -rf /usr/local/go && tar -C /usr/local -xzf go1.19.2.linux-amd64.tar.gz", check=True)
    subprocess.run("echo \"export PATH=$PATH:/usr/local/go/bin\" >> $HOME/.profile", check=True)

def install_go_package(repo, package_name):
    subprocess.run(f"go install github.com/{repo}/{package_name}@latest".format(), check=True)

def git_clone(git_url):
    git.Repo.clone_from(git_url)  

def check_sys():
    return shutil.which("apt") != None

def install_apt_package(package_name):
    subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)

def get_private_ip():
    import socket
    ip = "127.0.0.1"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    return ip

def install(self):
    with open("packages.json", "r") as f:
        self.packages = json.load(f)
    install_go()
    for pm in self.packages:
        if pm == "apt":
            for package in self.packages[pm]:
                install_apt_package(package)
        elif pm == "go":
            for k,v in self.packages[pm].items():
                install_go_package(k, v)
        elif pm == "git":
            for package in self.packages[pm]:
                git_clone(package)
        else:
            print("Cannot recognize package manager")
            pass