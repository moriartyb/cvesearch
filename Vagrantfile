Vagrant.configure("2") do |config|
  # use a bit older box for more likely
  config.vm.box = "chef/fedora-19"
  #config.vm.network "forwarded_port",guest: 8080, host: 8080
  config.vm.provider "virtualbox" do |v|
    v.memory = 512
  end
  #config.vm.provider "virtualbox" do |v|
  #  v.gui = true
  #end
end
