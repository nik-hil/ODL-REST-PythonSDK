from restapi import RestAPI

class CollectionApi(RestAPI):
    def __init__(self, **kwargs):
        '''Initialize super class 
        '''
        RestAPI.__init__(self, **kwargs)
        self.action = {'get':'get',
                       'put':'put',
                       'post':'post',
                       'delete':'delete',
                       }
    
    #all rest api related to topology
    def topology_get(self,url_params):
        '''Retrieve the Topology'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/topology/{containerName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def topology_get_userlink(self,url_params):
        '''Retrieve the user configured links'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/topology/{containerName}/userLinks'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def topology_add(self,url_params,flow):
        '''Add an User Link
        code    description
        201     User Link added successfully
        404     The Container Name was not found
        409     Failed to add User Link due to Conflicting Name
        500     Failed to add User Link. Failure Reason included in HTTP Error response
        503     One or more of Controller services are unavailable
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/topology/{containerName}/userLink/{name}'
        if url_params:
            return self.get_result(action, raw_url, url_params, flow)
        
    def topology_delete(self,url_params):
        '''delete an User Link
        code    description
        204     User link removed successfully
        404     The Container Name or Link Configuration Name was not found
        503     One or more of Controller services are unavailable
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/topology/{containerName}/userLink/{name}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    
    # all rest api related to host tracker
    def hosttracker_get_host(self,url_params):
        '''Returns a host that matches the IP Address value passed as parameter.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/hosttracker/{containerName}/address/{networkAddress}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def hosttracker_add_host(self,url_params,flow):
        '''Add a Static Host configuration. If a host by the given address already 
        exists, this method will respond with a non-successful status response
        code    description
        201     Static host created successfully
        400     Invalid parameters specified, see response body for details
        404     The container or resource is not found
        409     Resource conflict, see response body for details
        503     One or more of Controller services are unavailable
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/hosttracker/{containerName}/address/{networkAddress}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
    
    def hosttracker_delete_host(self,url_params):
        '''Delete a Static Host configuration.
        code    description
        204     Static host deleted successfully
        404     The container or a specified resource was not found
        406     Cannot operate on Default Container when other Containers are active
        503     One or more of Controller service is unavailable
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/hosttracker/{containerName}/address/{networkAddress}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def hosttracker_get_host_active(self,url_params):
        '''Returns a list of all Hosts : both configured via PUT API and 
        dynamically learnt on the network
        '''
        action = self.action['get']
        raw_url = ' /controller/nb/v2/hosttracker/{containerName}/hosts/active'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def hosttracker_get_host_inactive(self,url_params):
        '''Returns a list of Hosts that are statically configured and are 
        connected to a NodeConnector that is down
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/hosttracker/{containerName}/hosts/inactive'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    #all rest api related to flow programmer
    
    def flow_get_flow_all(self,url_params):
        '''Returns a list of Flows configured on the given container.'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/flowprogrammer/{containerName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def flow_get_flow_onnode(self,url_params):
        '''Returns a list of Flows configured on a Node in a given container'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/flowprogrammer/{containerName}/node/{nodeType}/{nodeId}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def flow_get_flow_onnode_human(self,url_params):
        '''Returns a list of Flows configured on a Node in a given container'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/flowprogrammer/{containerName}/node/{nodeType}/{nodeId}/staticFlow/{name}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def flow_update_flow_onnode_human(self,url_params,flow):
        '''Add or Modify a flow configuration. If the flow exists already, 
        it will replace the current flow.
        code    description
        200     Static Flow modified successfully
        201     Flow Config processed successfully
        400     Failed to create Static Flow entry due to invalid flow configuration
        401     User not authorized to perform this operation
        404     The Container Name or nodeId is not found
        406     Cannot operate on Default Container when other Containers are active
        409     Failed to create Static Flow entry due to Conflicting Name or configuration
        500     Failed to create Static Flow entry. Failure Reason included in HTTP Error response
        503     One or more of Controller services are unavailable
        '''
        
        action = self.action['put']
        raw_url = '/controller/nb/v2/flowprogrammer/{containerName}/node/{nodeType}/{nodeId}/staticFlow/{name}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
    
    def flow_delete_flow_onnode_human(self,url_params,flow):
        '''Delete a Flow configuration.'''
        
        action = self.action['delete']
        raw_url = '/controller/nb/v2/flowprogrammer/{containerName}/node/{nodeType}/{nodeId}/staticFlow/{name}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def flow_toggle_flow_onnode_human(self,url_params,flow):
        '''Toggle a flow configuration
        code    description
        200     Flow Config processed successfully
        401     User not authorized to perform this operation
        404     The Container Name or Node-id or Flow Name passed is not found
        406     Failed to delete Flow config due to invalid operation. Failure details included in HTTP Error response
        500     Failed to delete Flow config. Failure Reason included in HTTP Error response
        503     One or more of Controller service is unavailable
        '''
        
        action = self.action['post']
        raw_url = '/controller/nb/v2/flowprogrammer/{containerName}/node/{nodeType}/{nodeId}/staticFlow/{name}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    
    #all rest api related to static routing
    def staticrouting_get_allroutes(self,url_params):
        '''Get a list of static routes present on the given container.'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/staticroute/{containerName}/routes'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def staticrouting_get_route(self,url_params):
        '''Returns the static route for the provided configuration name on 
        a given container.'''
        action = self.action['get']
        raw_url = '/controller/nb/v2/staticroute/{containerName}/routes/{route}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def staticrouting_add_route(self,url_params,flow):
        '''Add a new Static Route. If a route by the given name already exists, 
        this method will return a non-successful status response.
        code    description
        201     Created Static Route successfully
        404     The Container Name passed is not found
        406     Cannot operate on Default Container when other Containers are active
        409     Failed to create Static Route entry due to Conflicting Name or Prefix.
        '''
        
        action = self.action['put']
        raw_url = '/controller/nb/v2/staticroute/{containerName}/routes/{route}'
        if url_params and flow:
            return self.get_result(action, raw_url, url_params, flow)
        
    def staticrouting_delete_route(self,url_params):
        '''Delete a Static Route'''
        
        action = self.action['delete']
        raw_url = '/controller/nb/v2/staticroute/{containerName}/routes/{route}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    #all rest api related to statistics
    def statistics_get_node_allflow(self,url_params):
        '''Returns a list of all Flow Statistics from all the Nodes.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/statistics/{containerName}/flow'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def statistics_get_node_allport(self,url_params):
        '''Returns a list of all the Port Statistics across all the 
        NodeConnectors on all the Nodes.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/statistics/{containerName}/port'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def statistics_get_node_alltable(self,url_params):
        '''Returns a list of all the Table Statistics on all Nodes.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/statistics/{containerName}/table'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def statistics_get_node_given(self,url_params):
        '''Returns a list of Flow Statistics for a given Node.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/statistics/{containerName}/flow/node/{nodeType}/{nodeId}'
        if url_params:
            return self.get_result(action, raw_url, url_params)

    def statistics_get_node_allport_given(self,url_params):
        '''Returns a list of all the Port Statistics across all the 
        NodeConnectors in a given Node.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/statistics/{containerName}/port/node/{nodeType}/{nodeId}'
        if url_params:
            return self.get_result(action, raw_url, url_params)

    def statisctics_get_node_alltable_given(self,url_params):
        '''Returns a list of all the Table Statistics on a specific node.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/statistics/{containerName}/port/node/{nodeType}/{nodeId}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    #all rest api related to subnet
    def subnet_get(self,url_params):
        '''List all the subnets in a given container.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/subnetservice/{containerName}/subnets'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def subnet_get_all(self,url_params):
        '''List all the subnets in a given container.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/subnetservice/{containerName}/subnet/{subnetName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)

    def subnet_add(self,url_params,flow):
        '''List all the subnets in a given container.
        code    description
        201     Subnet created successfully
        400     Invalid data passed
        401     User not authorized to perform this operation
        409     Subnet name in url conflicts with name in request body
        404     Container name passed was not found or subnet config is null
        500     Internal Server Error: Addition of subnet failed
        503     Service unavailable
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/subnetservice/{containerName}/subnet/{subnetName}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)

    def subnet_delete(self,url_params):
        '''Delete a subnet from the specified container context.
        code    description
        204     No Content
        401     User not authorized to perform this operation
        404     The containerName passed was not found
        500     Internal Server Error : Removal of subnet failed
        503     Service unavailable
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/subnetservice/{containerName}/subnet/{subnetName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def subnet_update(self,url_params,flow):
        '''Modify a subnet. Replace the existing subnet with the new specified one. 
        For now only port list modification is allowed. If the respective subnet 
        configuration does not exist this call is equivalent to a subnet creation.
        code    description
        200     Configuration replaced successfully
        401     User not authorized to perform this operation
        409     Subnet name in url conflicts with name in request body
        404     The containerName or subnetName is not found
        500     Internal server error: Modify subnet failed
        503     Service unavailable

        '''
        action = self.action['post']
        raw_url = '/controller/nb/v2/subnetservice/{containerName}/subnet/{subnetName}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
    
    #rest api relate to switch manager
    def switch_get_network(self,url_params):
        '''Retrieve a list of all the nodes and their properties in the network.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/nodes'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def switch_save_network(self,url_params,flow):
        '''Save the current switch configurations.
        200     Operation successful
        401     User not authorized to perform this operation
        404     The containerName is not found
        500     Failed to save switch configuration. Failure Reason included in 
                HTTP Error response
        503     One or more of Controller Services are unavailable
        '''
        action = self.action['post']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/save'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def switch_get_node(self,url_params):
        '''Retrieve a list of all the nodeconnectors and their properties in a 
            given node.
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/node/{nodeType}/{nodeId}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def switch_delete_node(self,url_params):
        '''Delete a property of a node
        code    description
        204     Property removed successfully
        400     The nodeId or configuration is invalid
        401     User not authorized to perform this operation
        404     The Container Name or nodeId or configuration name is not found
        409     Unable to delete property due to cluster conflict
        503     One or more of Controller services are unavailable
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/node/{nodeType}/{nodeId}/property/{propertyName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def switch_add_node(self,url_params,flow):
        '''Add a Description, Tier and Forwarding mode property to a node. 
        This method returns a non-successful response if a node by that name already exists.

        code    description
        201     Operation successful
        400     The nodeId or configuration is invalid
        401     User not authorized to perform this operation
        404     The Container Name or node or configuration name is not found
        406     The property cannot be configured in non-default container
        409     Unable to update configuration due to cluster conflict or conflicting description property
        503     One or more of Controller services are unavailable
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/node/{nodeType}/{nodeId}/property/{propertyName}/{propertyValue}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def switch_delete_nodeconnector(self,url_params):
        '''Delete a property of a node connector
        code    description
        204     Property removed successfully
        401     User not authorized to perform this operation
        404     The Container Name or nodeId or configuration name is not found
        503     One or more of Controller services are unavailable
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/nodeconnector/{nodeType}/{nodeId}/{nodeConnectorType}/{nodeConnectorId}/property/{propertyName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def switch_add_nodeconnector(self,url_params,flow):
        '''Delete a property of a node connector
        code    description
        201     Operation successful
        401     User not authorized to perform this operation
        404     The Container Name or nodeId or configuration name is not found
        409     Unable to add property due to cluster conflict
        503     One or more of Controller services are unavailable
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/switchmanager/{containerName}/nodeconnector/{nodeType}/{nodeId}/{nodeConnectorType}/{nodeConnectorId}/property/{propertyName}/{propertyValue}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    #all rest api related to user manager
    def user_add(self,url_params,flow):
        '''Delete a property of a node connector
        code    description
        201     User created successfully
        400     Invalid data passed
        401     User not authorized to perform this operation
        409     User name in url conflicts with name in request body
        404     User config is null
        500     Internal Server Error: Addition of user failed
        503     Service unavailable
        '''
        action = self.action['post']
        raw_url = '/controller/nb/v2/usermanager/users'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def user_delete(self,url_params):
        '''Delete a property of a node connector
        code    description
        204     User Deleted Successfully
        401     User not authorized to perform this operation
        404     The userName passed was not found
        500     Internal Server Error : Removal of user failed
        503     Service unavailable
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/usermanager/users/{userName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    #all rest api related to container manager
    def container_get_all(self,url_params):
        '''Get all the containers configured in the system
        200     Operation successful
        401     User is not authorized to perform this operation
        503     One or more of Controller Services are unavailable
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/containermanager/containers'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def container_get(self,url_params):
        '''Get the container configuration for container name requested
        200     Operation successful
        401     User is not authorized to perform this operation
        403     Operation forbidden on default
        404     The container is not found
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/containermanager/container/{container}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def container_create(self,url_params,flow):
        '''Create a container
        code    description
        201     Container created successfully
        400     Invalid Container configuration.
        401     User not authorized to perform this operation
        403     Operation forbidden on default
        404     Container Name is not found
        409     Failed to create Container due to Conflicting Name
        500     Failure Reason included in HTTP Error response
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/containermanager/container/{container}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def container_delete(self,url_params):
        '''Delete a container
        code    description
        204     Container deleted successfully
        401     User not authorized to perform this operation
        403     Operation forbidden on default
        404     The container is not found
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/containermanager/container/{container}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def container_get_flowall(self,url_params):
        '''Get all the flowspec in a given container
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/containermanager/container/{container}/flowspecs'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def container_add_nodeconnector(self,url_params,flow):
        '''Add node connectors to a container
        200     NodeConnectors added successfully
        401     User not authorized to perform this operation
        403     Operation forbidden on default
        404     The Container is not found
        409     Container Entry already exists
        500     Failed to create nodeconnectors. Failure Reason included in HTTP Error response

        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/containermanager/container/{container}/nodeconnector'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
    
    def container_delete_nodeconnector(self,url_params,flow):
        '''Remove node connectors from a container
        204     Container Entry deleted successfully
        400     Invalid Container Entry configuration
        404     The Container is not found
        406     Cannot operate on Default Container when other Containers are active
        500     Failed to delete node connector. Failure Reason included in HTTP Error response

        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/containermanager/container/{container}/nodeconnector'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def container_get_flow(self,url_params):
        '''Get flowspec within a given container
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/containermanager/container/{container}/flowspec/{flowspec}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def container_put_flow(self,url_params,flow):
        '''Add flowspec to a container
        '''
        action = self.action['get']
        raw_url = '/controller/nb/v2/containermanager/container/{container}/flowspec/{flowspec}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def container_delete_flow(self,url_params,flow):
        '''Remove flowspec from a container
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/containermanager/container/{container}/flowspec/{flowspec}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    #All rest api related to connection manager
    def connection_get_all(self,url_params):
        '''Retrieve a list of all the nodes connected to a given controller in the cluster.
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/connectionmanager/nodes'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def connection_delete_(self,url_params):
        '''Disconnect an existing Connection.
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/connectionmanager/node/{nodeType}/{nodeId}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def connection_node_unknown(self,url_params):
        '''If a Network Configuration Service needs a Management Connection and if the Node 
        Type is unknown, use this REST api to connect to the management session.
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/connectionmanager/node/{nodeId}/address/{ipAddress}/port/{port}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    def connection_node_known(self,url_params):
        '''If a Network Configuration Service needs a Management Connection, and if the node 
        Type is known, the user can choose to use this REST api to connect to the management 
        session.
        '''
        action = self.action['put']
        raw_url = '/controller/nb/v2/connectionmanager/node/{nodeType}/{nodeId}/address/{ipAddress}/port/{port}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
    #all rest api related to bridge domain
    def bridge_create(self,url_params,flow):
        '''Create a Bridge.
        Not sure how this works. See documentation for more
        '''
        action = self.action['post']
        raw_url = '/controller/nb/v2/networkconfig/bridgedomain/bridge/{nodeType}/{nodeId}/{bridgeName}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)
        
    def bridge_delete(self,url_params):
        '''Remove a Bridge.
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/networkconfig/bridgedomain/bridge/{nodeType}/{nodeId}/{bridgeName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
    
    def bridge_add_port(self,url_params,flow):
        '''Add a Port to a Bridge
        '''
        action = self.action['post']
        raw_url = '/controller/nb/v2/networkconfig/bridgedomain/port/{nodeType}/{nodeId}/{bridgeName}/{portName}'
        if url_params:
            return self.get_result(action, raw_url, url_params,flow)

    def bridge_delete_port(self,url_params):
        '''Remove a Port to a Bridge
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/networkconfig/bridgedomain/port/{nodeType}/{nodeId}/{bridgeName}/{portName}'
        if url_params:
            return self.get_result(action, raw_url, url_params)

    def bridge_add_port_vlan(self,url_params):
        '''Add a Port,Vlan to a Bridge
        '''
        action = self.action['delete']
        raw_url = '/controller/nb/v2/networkconfig/bridgedomain/port/{nodeType}/{nodeId}/{bridgeName}/{portName}/{vlan}'
        if url_params:
            return self.get_result(action, raw_url, url_params)
        
if __name__=='__main__':
    collection = CollectionApi(ipaddress='192.168.56.101')
    url_params = {'containerName':'default'}
    result = collection.statistics_get_all_node(url_params)
    print result.json()