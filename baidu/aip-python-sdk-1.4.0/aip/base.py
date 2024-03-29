# -*- coding: utf-8 -*-

"""
    AipBase
"""
import hmac
import json
import hashlib
import datetime
import base64
import time
import sys
import requests
from PIL import Image
from requests import session
requests.packages.urllib3.disable_warnings()

from .bceutil import get_canonical_querystring

if sys.version_info.major == 2:
    from urllib import urlencode
    from urllib import quote
    from urlparse import urlparse
    from StringIO import StringIO
else:
    from urllib.parse import urlencode
    from urllib.parse import quote
    from urllib.parse import urlparse
    from io import BytesIO as StringIO

class AipBase(object):
    """
        AipBase
    """

    __accessTokenUrl = 'https://aip.baidubce.com/oauth/2.0/token'

    __scope = 'brain_all_scope'

    def __init__(self, appId, apiKey, secretKey):
        """
            AipBase(appId, apiKey, secretKey)
        """

        self._appId = appId.strip()
        self._apiKey = apiKey.strip()
        self._secretKey = secretKey.strip()
        self._authObj = {}
        self._isCloudUser = None
        self.__client = session()
        self.__connectTimeout = 60.0
        self.__socketTimeout = 60.0

    def setConnectionTimeoutInMillis(self, ms):
        """
            setConnectionTimeoutInMillis
        """

        self.__connectTimeout = ms / 1000.0

    def setSocketTimeoutInMillis(self, ms):
        """
            setSocketTimeoutInMillis
        """

        self.__socketTimeout = ms / 1000.0

    def _request(self, url, data):
        """
            self._request('', {})
        """
        try:
            result = self._validate(url, data)
            if result != True:
                return result

            authObj = self._auth()
            params = self._getParams(authObj)
            headers = self._getAuthHeaders('POST', url, params)

            response = self.__client.post(url, data=data, params=params, 
                            headers=headers, verify=False, timeout=(
                                self.__connectTimeout,
                                self.__socketTimeout,
                            )
                        )
            obj = self._proccessResult(response.content)

            if not self._isCloudUser and obj.get('error_code', '') == 110:
                authObj = self._auth(True)
                params = self._getParams(authObj)
                response = self.__client.post(url, data=data, params=params, 
                                headers=headers, verify=False, timeout=(
                                    self.__connectTimeout,
                                    self.__socketTimeout,
                                )
                            )
                obj = self._proccessResult(response.content)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
            return {
                'error_code': 'SDK108',
                'error_msg': 'connection or read data timeout',
            }
 
        return obj

    def _validate(self, url, data):
        """
            validate
        """

        return True

    def _proccessResult(self, content):
        """
            formate result
        """

        if sys.version_info.major == 2:
            return json.loads(content) or {}
        else:
            return json.loads(content.decode()) or {}

    def _auth(self, refresh=False):
        """
            api access auth
        """

        #未过期
        if not refresh:
            tm = self._authObj.get('time', 0) + int(self._authObj.get('expires_in', 0)) - 30
            if tm > int(time.time()):
                return self._authObj

        obj = self.__client.get(self.__accessTokenUrl, verify=False, params={
            'grant_type': 'client_credentials',
            'client_id': self._apiKey,
            'client_secret': self._secretKey,
        }, timeout=(
            self.__connectTimeout,
            self.__socketTimeout,
        )).json()

        self._isCloudUser = not self._isPermission(obj)
        obj['time'] = int(time.time())
        self._authObj = obj

        return obj

    def _isPermission(self, authObj):
        """
            check whether permission
        """

        scopes = authObj.get('scope', '') 

        return self.__scope in scopes.split(' ')

    def _getParams(self, authObj):
        """
            api request http url params
        """

        params = {
            'aipSdk': 'python',
            'aipVersion': '1_4_0',
        }

        if self._isCloudUser == False:
            params['access_token'] = authObj['access_token']

        return params

    def _getAuthHeaders(self, method, url, params=None):
        """
            api request http headers
        """
        if self._isCloudUser == False:
            return {}

        # UTC timestamp
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        urlResult = urlparse(url)
        host = urlResult.hostname
        path = urlResult.path
        version, expire, signatureHeaders = '1', '1800', 'host'

        # 1 Generate SigningKey
        val = "bce-auth-v%s/%s/%s/%s" % (version, self._apiKey, timestamp, expire)
        signingKey = hmac.new(self._secretKey.encode('utf-8'), val.encode('utf-8'),
                        hashlib.sha256
                    ).hexdigest()

        # 2 Generate CanonicalRequest
        # 2.1 Genrate CanonicalURI
        canonicalUri = quote(path)
        # 2.2 Generate CanonicalURI: not used here
        # 2.3 Generate CanonicalHeaders: only include host here
        canonicalHeaders = 'host:%s' % quote(host).strip()
        # 2.4 Generate CanonicalRequest
        canonicalRequest = '%s\n%s\n%s\n%s' % (
            method.upper(),
            canonicalUri,
            get_canonical_querystring(params),
            canonicalHeaders
        )

        # 3 Generate Final Signature 
        signature = hmac.new(signingKey.encode('utf-8'), canonicalRequest.encode('utf-8'),
                        hashlib.sha256
                    ).hexdigest()
        authorization = 'bce-auth-v%s/%s/%s/%s/%s/%s' % (version, self._apiKey, timestamp,
                            expire, signatureHeaders, signature
                        )

        return {
            'Host': host,
            'x-bce-date': timestamp,
            'accept': '*/*',
            'authorization': authorization,
        }
