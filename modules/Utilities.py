# -*- coding: utf-8 -*-

import os
from datetime import datetime

def CreateFolder(FolderName):
    if not os.path.exists(FolderName):
        os.makedirs(FolderName)

def MakeConvertDateFormat(SrcFormat,DstFormat):
    def ConvertFormat(s):
        return datetime.strftime(datetime.strptime(s, SrcFormat),DstFormat)
    return ConvertFormat
