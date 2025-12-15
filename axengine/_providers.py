# Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
#
# This source file is the property of Axera Semiconductor Co., Ltd. and
# may not be copied or distributed in any isomorphic form without the prior
# written consent of Axera Semiconductor Co., Ltd.
#

import ctypes.util as cutil

providers = []
axengine_provider_name = 'AxEngineExecutionProvider'
axclrt_provider_name = 'AXCLRTExecutionProvider'

_axengine_lib_name = 'ax_engine'
_axclrt_lib_name = 'axcl_rt'


# check if axcl_rt is installed, so if available, it's the default provider
import os

def _lib_exists(lib_name, fallback_path):
    return cutil.find_library(lib_name) is not None or os.path.exists(fallback_path)

if _lib_exists(_axclrt_lib_name, '/opt/lib/libaxcl_rt.so'):
    providers.append(axclrt_provider_name)

# check if ax_engine is installed
if _lib_exists(_axengine_lib_name, '/opt/lib/libax_engine.so'):
    providers.append(axengine_provider_name)


def get_all_providers():
    return [axengine_provider_name, axclrt_provider_name]


def get_available_providers():
    return providers
