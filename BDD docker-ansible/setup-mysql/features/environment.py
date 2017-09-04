from subprocess import Popen, PIPE
import os

def before_all(context):
  root_dir = os.path.dirname(os.path.dirname(__file__))

  proc = Popen(["docker", "rm", "-f", "scotty-mysql-devops-image"], stdout=PIPE, stderr=PIPE)
  out, err = proc.communicate()
  exitcode = proc.returncode

  proc = Popen(["docker", "build", root_dir, "-t", "setup-mysql"], stdout=PIPE, stderr=PIPE)
  out, err = proc.communicate()
  exitcode = proc.returncode

  assert exitcode == 0

#def after_all(context):
#  proc = Popen(["docker", "rm", "-f", "scotty-mysql-devops-image"], stdout=PIPE, stderr=PIPE)
#  out, err = proc.communicate()
#  exitcode = proc.returncode
#
#  assert exitcode == 0
