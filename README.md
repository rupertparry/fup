# FUP – A simple command-line tool for putting files up.

✨ Share a file via a unique URL with one command.

`fup` is a simple command-line tool for sharing links to files. It uses a unique
hash of a file based on the creation date & your username to act as a unique file
ID and keep everything in sync.

- ✨ Share a unique URL for a file by running `fup myfile.png`
- 🔗 If the file's already up, `fup myfile.png` copies the link
- 🗑 Delete the remote version of a file with `fup -d myfile.png`

DISCLAIMER: This is not production software, and has only been tested on macOS.
Use at your own risk.

## Setup

You'll need an AWS S3-compatible object storage bucket. I recommend using
Digital Ocean Spaces for ease of use.

Build and install with `./build.sh`.

Before running, create a `~/.fup` file with the following:

```
{
  "ID": <make up a user ID string>,
  "AWS_KEY": <your aws key>,
  "AWS_SECRET": <your aws secret>,
  "AWS_ENDPOINT": <your aws endpoint as an https:// url>,
  "AWS_BUCKET": <your aws bucket name>,
  "CUSTOM_DOMAIN": <custom domain for your bucket (optional)>
}