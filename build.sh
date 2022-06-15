#!/bin/bash
python3 -m build
PKG=$(ls dist | grep .whl)
pip3 install dist/$PKG
rm /usr/local/bin/fup || true
printf "#!/bin/bash\npython3 -m fup" >> /usr/local/bin/fup
chmod +x /usr/local/bin/fup