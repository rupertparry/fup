# FUP – A simple tool for putting files up.

**fup** is a simple command-line tool for sharing links to files. It uses a
hash of a file's creation date & your email address to act as a unique, permanent file
ID and keep everything in sync.

- ✨ Share a unique URL to a file by running `fup myfile.png`
- 🔗 If the file's already up, `fup myfile.png` copies the link
- 🔥 Replace the same link with a newer version by running `fup -f myfile.png`
- 🗑 Delete the remote version of a file with `fup -d myfile.png`

If you change service providers, all your file IDs will stay the same, just with a new base URL.

## Setup

You'll need an AWS S3-compatible object storage bucket. I recommend using
Digital Ocean Spaces for ease of use.

Build and install with `./build.sh`.

Before running, create a `~/.fup` file with the following in JSON format:

```
{
  "ID": <your email address>,
  "AWS_KEY": <your aws key>,
  "AWS_SECRET": <your aws secret>,
  "AWS_ENDPOINT": <your aws endpoint as an https:// url>,
  "AWS_BUCKET": <your aws bucket name>,
  "CUSTOM_DOMAIN": <custom domain for your bucket (optional)>
}
```

## Roadmap

- Ability to open local or remote files, based on a local register of hashes
- A storage service for those that don't want to set up an S3 back-end
- Links that display files (e.g. pretty markdown display for `.md` or `.txt` files)
- Apps (including mobile) for more general user-friendly interaction
- Better hashing algorithm to eliminate possible collisions (though extremely unlikely)

## Disclaimer

This is early-stage development software, and has only been tested on macOS. Use at your own risk.
