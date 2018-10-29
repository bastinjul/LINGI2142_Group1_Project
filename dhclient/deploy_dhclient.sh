MAIN_PATH='/home/vagrant/LINGI2142_Group1_Project'
for i in Ca0 Ca1 Ca2 Ca5 Ha0 Ha1 Ha2 Ha5 Mi0 Mi1 Mi2 Mi5 Py0 Py1 Py2 Py5 SH0 SH1 SH2 SH5 St0 St1 St2 St5
do
  sudo mkdir -p $MAIN_PATH/ucl_minimal_cfg/$i/dhcp/
  cp -r $MAIN_PATH/dhclient/src/* $MAIN_PATH/ucl_minimal_cfg/$i/dhcp/
  cp -r $MAIN_PATH/dhclient/resolv/* $MAIN_PATH/ucl_minimal_cfg/$i/
done

