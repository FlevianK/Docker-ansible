from behave import given, when, then, step, use_step_matcher
from subprocess import Popen, PIPE

use_step_matcher("re")

@given('I have a running ubuntu docker container')
def step_impl(context):
  context.container_name = "scotty-mysql-devops-image"
  proc = Popen(["docker", "run", "-i", "-d", "--name", context.container_name, "setup-mysql"], stdout=PIPE, stderr=PIPE)
  container_id, err = proc.communicate()
  exitcode = proc.returncode

  assert exitcode == 0
  assert container_id is not False
  context.container_id = container_id

@when('I run my config scripts')
def step_impl(context):
  proc = Popen(["docker", "exec", context.container_name, "ansible-playbook", "-i", "/tmp/ansible/inventory.ini", "/tmp/ansible/playbook.yml"], stdout=PIPE, stderr=PIPE)
  out, err = proc.communicate()

  context.ansible_returncode = proc.returncode

@then('It should succeed')
def step_impl(context):
  assert context.ansible_returncode == 0
                                                             
@then('(mysql|nginx) should be running on port {port:d}')
def step_impl(context, port):
  proc = Popen(["docker", "exec", context.container_name, "bash", "-c", "exec 7<>/dev/tcp/127.0.0.1/" + port], stdout=PIPE, stderr=PIPE)
  out, err = proc.communicate()
  print(out)
  print(err)
  assert proc.returncode == 0

@given('We have a docker container running')
def step_impl(context):
  context.container_name = "scotty-mysql-devops-image"
  proc = Popen(["docker", "run", "-i", "-d", "--name", context.container_name, "setup-mysql"], stdout=PIPE, stderr=PIPE)
  container_id, err = proc.communicate()
  exitcode = proc.returncode
  assert exitcode == 0

@when('I run the scripts')
def step_impl(context):
  proc = Popen(["docker", "exec", context.container_name, "ansible-playbook", "-i", "/tmp/ansible/inventory.ini", "/tmp/ansible/playbook.yml"], stdout=PIPE, stderr=PIPE)

  out, err = proc.communicate()
  context.ansible_returncode = proc.returncode

@then('nginx should be installed')
def step_impl(context):
  assert context.ansible_returncode == 0

@then('nginx should be running on port 80')
def step_impl(context):
  proc = Popen(["docker", "exec", context.container_name, "bash", "-c", "exec 7<>/dev/tcp/127.0.0.1/80"], stdout=PIPE, stderr=PIPE)

  out, err = proc.communicate()
  exitcode = proc.returncode
  print(out)
  print(err)
  assert exitcode == 0

