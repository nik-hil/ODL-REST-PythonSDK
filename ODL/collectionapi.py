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
        raw_url = ' /controller/nb/v2/hosttracker/{containerName}/hosts/inactive'
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
        
        
if __name__=='__main__':
    collection = CollectionApi(ipaddress='192.168.56.101')
    url_params = {'containerName':'default'}
    result = collection.statistics_get_all_node(url_params)
    print result.json()