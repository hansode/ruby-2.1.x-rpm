# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define :centos6 do |centos|
    centos.vm.box = 'chef/centos-6.6'
    centos.cache.scope = :box if Vagrant.has_plugin? 'vagrant-cachier'
  end

  config.vm.define :centos7 do |centos|
    centos.vm.box = 'chef/centos-7.1'
    centos.cache.scope = :box if Vagrant.has_plugin? 'vagrant-cachier'
  end
end
