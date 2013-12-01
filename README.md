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
  
Little More Details
-------------------
<code>CollectionApi</code> has <code>ipaddress, port, username, password, http</code> for initialization.
After initialization call method. Method internally calls REST api and returns response object.

Parameters for each method are, <code>url_params and flow </code>
* <code>url_params</code> inside a raw url for e.g <code>/controller/nb/v2/topology/{containerName}/userLinks</code>
You have to specify <code>containerName</code> in dict format <code>{'containerName':'default'}<code>.
* <code>flow</code> If request type is <code>put/post</code> and some places <code>delete</code>, you have to specify json parameter. flow type is dict. Internally flow is converted to json.
