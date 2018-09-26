import subprocess

def gitAddAll(repoDir):
    cmd = ['git', 'add', '.']
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

def gitCommit(repoDir, message):
    cmd = ['git', 'commit', '-m', message]
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

def gitPush(repoDir):
    cmd = ['git', 'push']
    p = subprocess.Popen(cmd, cwd=repoDir)
    p.wait()

def doItAll(repoDir, message):
    gitAddAll(repoDir)
    gitCommit(repoDir, message)
    gitPush(repoDir)

    