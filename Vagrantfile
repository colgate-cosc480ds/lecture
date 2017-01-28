$script = <<SCRIPT
echo Provisioning start...
sudo apt-get update -qq  # make it quiet
sudo apt-get install -yq git
sudo apt-get install -yq libsm6 libxrender1 libfontconfig1

export VHOME=/home/vagrant
export MHOME=$VHOME/miniconda

if [ -e "$MHOME/bin/python" ]; then
	echo "conda is already installed; skipping"
else
	if [ -e "$VHOME/miniconda.sh" ]; then
		echo "conda install file already downloaded"
	else
		wget -O $VHOME/miniconda.sh https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
	fi
	bash $VHOME/miniconda.sh -bp $MHOME
fi

export PATH="$MHOME/bin:$PATH"
echo "export PATH=$MHOME/bin:\$PATH" >>  $VHOME/.bash_profile
echo "ubuntu" | sudo tee /etc/hostname


if [[ $(sudo swapon -s | grep '/swapfile' | wc -c) -eq 0 ]]; then
	sudo fallocate -l 4G /swapfile
	sudo chmod 600 /swapfile
	sudo mkswap /swapfile
	sudo swapon /swapfile
	echo "/swapfile   none    swap    sw    0   0" | sudo tee -a /etc/fstab
else
	echo "swap file is already configured"
fi

conda update -yq conda
conda install -yq matplotlib=1.5.1
conda install -yq jupyter=1.0.0
conda install -yq pandas=0.19.2
conda install -yq scikit-learn=0.18.1
conda install -yq beautifulsoup4
conda install -yq html5lib

echo Provisioning end
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, inline: $script, privileged: false
  config.vm.network :forwarded_port, guest: 8888, host: 8888
  config.vm.provider "virtualbox" do |v|
  	v.memory = 2048   # 2GB of memory
  end
end
