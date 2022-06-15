#!/usr/bin/env python

import os, json, sys, hashlib, pathlib, random
import boto3, pyperclip

config_path = os.path.expanduser('~/.fup')

if not os.path.exists(config_path):
    print("Please create a ~/.fup file.")
    sys.exit()

with open(config_path) as file:
    config = json.loads(file.read())

if "CUSTOM_DOMAIN" in config:
    base_url = config["CUSTOM_DOMAIN"]
else:
    bucket = config["AWS_BUCKET"]
    endpoint = config["AWS_ENDPOINT"].split('//')[1]
    base_url = f"https://{bucket}.{endpoint}"

def get_hashname(file_path):
    created_at = os.stat(file_path).st_birthtime
    user_id = config["ID"]
    file_string = f"{created_at}{user_id}"
    file_hash = hashlib.sha1(file_string.encode()).hexdigest()
    file_suffix = pathlib.Path(file_path).suffix
    hash_name = f"{file_hash}{file_suffix}"
    return hash_name

def handle_file(file_path, force=False, delete=False):
    session = boto3.Session()
    client = session.client('s3',
        endpoint_url=config["AWS_ENDPOINT"],
        aws_access_key_id=config["AWS_KEY"],
        aws_secret_access_key=config["AWS_SECRET"]
    )

    hashname = get_hashname(file_path)

    try:
        client.head_object(Bucket=config["AWS_BUCKET"], Key=hashname)
        obj_exists = True
    except:
        obj_exists = False
    
    if obj_exists and delete:
        client.delete_object(Bucket=config["AWS_BUCKET"], Key=hashname)
        print(f"🗑  Remote file deleted: {hashname}")
        sys.exit()
    elif obj_exists and not force:
        file_url = f"{base_url}/{hashname}"
        pyperclip.copy(file_url)
        print(f"✨ File exists. Copied to clipboard!")
        print(f"🔗 {file_url}")
        sys.exit()
    elif not obj_exists and delete:
        print("🤷 Nothing to delete: file not uploaded.")
        sys.exit()

    print(f"🚀 Uploading {file_path}")
    client.upload_file(file_path, config["AWS_BUCKET"], hashname, ExtraArgs={'ACL':'public-read'})

    file_url = f"{base_url}/{hashname}"
    pyperclip.copy(file_url)
    print(f"✨ File uploaded & copied to clipboard!\n🔗 {file_url}")


def abort():
    fail_message = random.choice([
        "Sorry, I don't quite follow you.",
        "I beg your pardon? I don't get it.",
        "Sorry, I don't understand your banter.",
        "Um...... no. Don't know what you're on about."
    ])
    print(fail_message)
    sys.exit()

if len(sys.argv) < 2: abort()

valid_args = False
args = sys.argv[1:]
for arg in args:
    if os.path.isfile(arg):
        valid_args = True
        file_path = os.path.abspath(os.path.expanduser(arg))
        if '-f' in args or '--force' in args:
            handle_file(file_path, force=True)
        elif '-d' in args or '--delete' in args:
            handle_file(file_path, delete=True)
        else:
            handle_file(file_path)

if not valid_args: abort()