#!/usr/bin/env python

import argparse
import code
from fabric.api import task
from app import app, db, user_datastore, Role, User

def build():
  db.create_all()
  user_role = user_datastore.create_role(name="user")
  admin_role = user_datastore.create_role(name="admin")

  admin_user = user_datastore.create_user(email="admin@sup.io", password="password")
  user_datastore.add_role_to_user(admin_user, admin_role)

  test_user1 = user_datastore.create_user(email="test@sup.io", password="password")
  test_user2 = user_datastore.create_user(email="test2@sup.io", password="password")

  user_datastore.add_role_to_user(test_user1, user_role)
  user_datastore.add_role_to_user(test_user2, user_role)

  db.session.add(admin_user)
  db.session.add(test_user1)
  db.session.add(test_user2)

  db.session.commit()

def console():
  context = locals()
  context['app'] = app
  context['db'] = db
  context['user_datastore'] = user_datastore
  context['Role'] = Role
  context['User'] = User
  code.interact(local=locals())

def run():
  app.run(host='127.0.0.1', debug=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if args.action == 'build':
        build()
    elif args.action == 'console':
        console()
    elif args.action == 'run':
        run()
