MAIN_PATH='/home/vagrant/LINGI2142_Group1_Project'
for i in DHCP1 DHCP2
do
  sudo mkdir -p $MAIN_PATH/ucl_minimal_cfg/$i/dhcp/
  cp $MAIN_PATH/dhcp/src/* $MAIN_PATH/ucl_minimal_cfg/$i/dhcp/
done

