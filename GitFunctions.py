import subprocess

def AddAll(repoDir):
    cmd = ['git', 'add', '.']
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

def Commit(repoDir, message):
    cmd = ['git', 'commit', '-m', message]
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

def Push(repoDir):
    cmd = ['git', 'push']
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

def doItAll(repoDir, message):
    AddAll(repoDir)
    Commit(repoDir, message)
    Push(repoDir)

    