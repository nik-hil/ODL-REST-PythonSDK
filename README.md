ODL-REST-PythonSDK
==================

Python SDK for OpenDaylight Controller Rest API

All REST api are collected from <code>https://wiki.opendaylight.org/view/OpenDaylight_Controller:REST_Reference_and_Authentication</code>

This SDK requires <code>'requests'</code>. Install it by using <code>'pip install requests'</code>

This is easy to use, 

  ```
  #Intialize controller ip-address
  collection = CollectionApi(ipaddress='192.168.56.101')
  #Pass the parameter at URL
  url_params = {'containerName':'default'}
  #collect the result from REST api
  result = collection.statistics_get_all_node(url_params)
  print result.json()
  ```
