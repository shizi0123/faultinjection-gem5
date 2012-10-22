# Copyright (c) 2009 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Ali Saidi

from m5.params import *

from System import System

class ArmMachineType(Enum):
    map = {'RealView_EB' : 827,
           'RealView_PBX' : 1901 }

class ArmSystem(System):
    type = 'ArmSystem'
    load_addr_mask = 0xffffffff
    # 0x35 Implementor is '5' from "M5"
    # 0x0 Variant
    # 0xf Architecture from CPUID scheme
    # 0xf00 Primary part number
    # 0x0 Revision
    midr_regval = Param.UInt32(0x350ff000, "MIDR value")
    boot_loader = Param.String("", "File that contains the boot loader code if any")
    boot_loader_mem = Param.PhysicalMemory(NULL,
                          "Memory object that boot loader is to be loaded into")
    gic_cpu_addr = Param.Addr(0, "Addres of the GIC CPU interface")
    flags_addr = Param.Addr(0, "Address of the flags register for MP booting")

class LinuxArmSystem(ArmSystem):
    type = 'LinuxArmSystem'
    load_addr_mask = 0x0fffffff
    machine_type = Param.ArmMachineType('RealView_PBX',
        "Machine id from http://www.arm.linux.org.uk/developer/machines/")

