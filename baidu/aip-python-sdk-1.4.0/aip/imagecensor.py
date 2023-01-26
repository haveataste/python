# -*- coding: utf-8 -*-

import re
import sys
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote
from .base import Image
from .base import StringIO

class AipImageCensor(AipBase):
    """
        Aip ImageCensor
    """

    __antiPornUrl = 'https://aip.baidubce.com/rest/2.0/antiporn/v1/detect'

    __antiPornGifUrl = 'https://aip.baidubce.com/rest/2.0/antiporn/v1/detect_gif'

    __antiTerrorUrl = 'https://aip.baidubce.com/rest/2.0/antiterror/v1/detect'
    
    def antiPorn(self, image):
        """
            antiporn
        """

        data = {}
        data['image'] = image

        return self._request(self.__antiPornUrl, data)

    def _validate(self, url, data):
        """
            validate
        """

        img = Image.open(StringIO(data['image']))
        data['image'] = base64.b64encode(data['image'])

        format = img.format.upper()
        width, height = img.size

        # gif
        if url == self.__antiPornGifUrl:
            if format != 'GIF':
                return {
                    'error_code': 'SDK109',
                    'error_msg': 'unsupported image format',
                }
            return True

        # 图片格式检查
        if format not in ['JPEG', 'BMP', 'PNG', 'GIF']:
            return {
                'error_code': 'SDK109',
                'error_msg': 'unsupported image format',
            }


        # 编码后小于4m
        if len(data['image']) >= 4 * 1024 * 1024:
            return {
                'error_code': 'SDK100',
                'error_msg': 'image size error',
            }

        return True

    def antiPornGif(self, image):
        """
            antiporn gif
        """

        data = {}
        data['image'] = image

        return self._request(self.__antiPornGifUrl, data)

    def antiTerror(self, image):
        """
            antiterror
        """

        data = {}
        data['image'] = image

        return self._request(self.__antiTerrorUrl, data)
