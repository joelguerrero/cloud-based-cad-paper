'''
client
======

Convenience functions for working with the Onshape API
'''

from onshape import Onshape

import mimetypes
import random
import string
import os


class Client():
    '''
    Defines methods for testing the Onshape API. Comes with several methods:

    - Create a document
    - Delete a document
    - Get a list of documents

    Attributes:
        - stack (str, default='https://cad.onshape.com'): Base URL
        - logging (bool, default=True): Turn logging on or off
    '''

    def __init__(self, stack='https://cad.onshape.com', logging=True):
        '''
        Instantiates a new Onshape client.

        Args:
            - stack (str, default='https://cad.onshape.com'): Base URL
            - logging (bool, default=True): Turn logging on or off
        '''

        self._stack = stack
        self._api = Onshape(stack=stack, logging=logging)

    def new_document(self, name='Test Document', owner_type=0, public=False):
        '''
        Create a new document.

        Args:
            - name (str, default='Test Document'): The doc name
            - owner_type (int, default=0): 0 for user, 1 for company, 2 for team
            - public (bool, default=False): Whether or not to make doc public

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name,
            'ownerType': owner_type,
            'isPublic': public
        }

        return self._api.request('post', '/api/documents', body=payload)

    def rename_document(self, did, name):
        '''
        Renames the specified document.

        Args:
            - did (str): Document ID
            - name (str): New document name

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name
        }

        return self._api.request('post', '/api/documents/' + did, body=payload)

    def del_document(self, did):
        '''
        Delete the specified document.

        Args:
            - did (str): Document ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('delete', '/api/documents/' + did)

    def get_document(self, did):
        '''
        Get details for a specified document.

        Args:
            - did (str): Document ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/documents/' + did)

    def list_documents(self):
        '''
        Get list of documents for current user.

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/documents')

    def create_assembly(self, did, wid, name='My Assembly'):
        '''
        Creates a new assembly element in the specified document / workspace.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - name (str, default='My Assembly')

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name
        }

        return self._api.request('post', '/api/assemblies/d/' + did + '/w/' + wid, body=payload)

    def get_features(self, did, wid, eid):
        '''
        Gets the feature list for specified document / workspace / part studio.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/features')

    def get_partstudio_tessellatededges(self, did, wid, eid):
        '''
        Gets the tessellation of the edges of all parts in a part studio.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''

        return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/tessellatededges')

    def upload_blob(self, did, wid, filepath='./blob.json'):
        '''
        Uploads a file to a new blob element in the specified doc.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - filepath (str, default='./blob.json'): Blob element location

        Returns:
            - requests.Response: Onshape response data
        '''

        chars = string.ascii_letters + string.digits
        boundary_key = ''.join(random.choice(chars) for i in range(8))

        mimetype = mimetypes.guess_type(filepath)[0]
        encoded_filename = os.path.basename(filepath)
        file_content_length = str(os.path.getsize(filepath))
        blob = open(filepath)

        req_headers = {
            'Content-Type': 'multipart/form-data; boundary="%s"' % boundary_key
        }

        # build request body
        payload = '--' + boundary_key + '\r\nContent-Disposition: form-data; name="encodedFilename"\r\n\r\n' + encoded_filename + '\r\n'
        payload += '--' + boundary_key + '\r\nContent-Disposition: form-data; name="fileContentLength"\r\n\r\n' + file_content_length + '\r\n'
        payload += '--' + boundary_key + '\r\nContent-Disposition: form-data; name="file"; filename="' + encoded_filename + '"\r\n'
        payload += 'Content-Type: ' + mimetype + '\r\n\r\n'
        payload += blob.read()
        payload += '\r\n--' + boundary_key + '--'

        return self._api.request('post', '/api/blobelements/d/' + did + '/w/' + wid, headers=req_headers, body=payload)





#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#FUNCTIONS ADDED OR MODIFIED BY JOEGI
#*********************************************************************************
#*********************************************************************************



#*********************************************************************************
#FUNCTION MODIFIED BY JOEGI
#*********************************************************************************

    def part_studio_stl(self, did, wid, eid):
        '''
        Exports STL export from a part studio.
	To modify the the geometry use variables.
	For configurations better use part_studio_stl_conf

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''

        req_headers = {
            'Accept': 'application/vnd.onshape.v1+octet-stream'
        }

	#New query entry
        query = {
            'units': 'meter',
            'scale': 1.0
	    #'mode': 'binary'
        }

        #return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/stl', headers=req_headers)

	#Suppress STL output to terminal - The STL is saved in a STL file
        return self._api.request_no_out('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/stl', query, headers=req_headers)

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def get_features_id(self, did, wid, eid, fid):
        '''
        Gets the feature list for specified document / workspace / part studio.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID
			- fid (str): Feature ID

        Returns:
            - requests.Response: Onshape response data
        '''

        query = {
            'featureId': fid
        }

        return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/features', query)


#This is a restful call:
#https://cad.onshape.com/api/partstudios/d/df79a2e435764ab47ceee2de/w/
#2b0e77fea8b228b0bd1c1e97/e/d2dc8085df08371957891656/features?    ===>   featureId=Fov9g55zEJvW2cI_0

#The question mark at the end of the call means that it can get a query
#To add the query add a json dictionary

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def feature_update(self, did, wid, eid, fid, body_feature):
        '''
        Update a feature in given did/wid/eid.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID
			- fid (str): Feature ID
			- body_feature: dict with the body of the feature to update

        Returns:
            - requests.Response: Onshape response data
        '''

        #payload = { }

        return self._api.request('post', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/features/featureid/' + fid , body=body_feature)

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def copy_workspace(self, did, wid, name):
        '''
        Copy/duplicate the specified document with the given name

        Args:
            - did (str): Document ID
            - wid (str): workspace ID
            - name (str): New document name

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'newName': name
        }

        return self._api.request('post', '/api/documents/' + did + '/workspaces/' + wid + '/copy', body=payload)

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def delete_workspace(self, did, wid):
        '''
        Deletes the specified document.

        Args:
            - did (str): Document ID
            - wid (str): workspace ID

        Returns:
            - requests.Response: Onshape response data
        '''


        return self._api.request('delete', '/api/documents/d/' + did + '/workspaces/' + wid)

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def create_partstudio(self, did, wid, name):
        '''
        Creates a part sutid with the given name.

        Args:
            - did (str): Document ID
            - wid (str): workspace ID
            - name (str): New document name

        Returns:
            - requests.Response: Onshape response data
        '''

        payload = {
            'name': name
        }

        return self._api.request('post', '/api/partstudios/d/' + did + '/w/' + wid, body=payload)
        
#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def delete_partstudio(self, did, wid, eid):
        '''
        Deletes the part studio.

        Args:
            - did (str): Document ID
            - wid (str): workspace ID
            - eid (str): Element ID

        Returns:
            - requests.Response: Onshape response data
        '''


        return self._api.request('delete', '/api/elements/d/' + did + '/w/' + wid + '/e/' + eid)

#https://cad.onshape.com/api/elements/df79a2e435764ab47ceee2de/workspace/2b0e77fea8b228b0bd1c1e97
#https://cad.onshape.com/api/elements/d/df79a2e435764ab47ceee2de/w/2b0e77fea8b228b0bd1c1e97/e/ba8ab8b5298b168a589f5b3d?

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def get_parts_list(self, did, wid):
        '''
        Gets list of parts. in document

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID

        Returns:
            - requests.Response: Onshape response data
        '''


        return self._api.request('get', '/api/parts/d/' + did + '/w/' + wid)

#https://cad.onshape.com/api/parts/d/cde8d732c970c4d9f7b88e5e/w/209ad99760a3f7a6cb3f4dc1?withThumbnails=false&includePropertyDefaults=false
#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def featurescript(self, did, wid, eid, body_feature):
        '''
        Create a new document.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID
	    - body_feature: dict with the body of the feature to update

        Returns:
            - requests.Response: Onshape response data
        '''

        #payload = { }

        return self._api.request('post', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/featurescript', body=body_feature)

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#*********************************************************************************

    def featurescript_conf(self, did, wid, eid, body_feature, configuration):
        '''
        Create a new document.

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID
	    - body_feature: dict with the body of the feature to update

        Returns:
            - requests.Response: Onshape response data
        '''

        #payload = { }

        return self._api.request('post', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/featurescript', body=body_feature, query=configuration)

#*********************************************************************************



#*********************************************************************************
#NEW FUNCTION BY JOEGI
#
#Replaced request for request_no_out
#This is done to avoid writing on screen the STL information
#
#*********************************************************************************

    def part_studio_stl_conf(self, did, wid, eid, configuration):
        '''
        Exports STL export from a part studio using configurations

        Args:
            - did (str): Document ID
            - wid (str): Workspace ID
            - eid (str): Element ID
            - query: dict with the body of input parameters

        Returns:
            - requests.Response: Onshape response data
        '''

        req_headers = {
            'Accept': 'application/vnd.onshape.v1+octet-stream'
        }

        #return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/stl', headers=req_headers)

        #return self._api.request('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/stl', query=configuration)
        return self._api.request_no_out('get', '/api/partstudios/d/' + did + '/w/' + wid + '/e/' + eid + '/stl', query=configuration, headers=req_headers)

#*********************************************************************************


