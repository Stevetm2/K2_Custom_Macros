# Simulate Happy Hare MMU tray/slot variables from box variables on K2
#
# DUMP_VARIABLES NAME='mmu' VALUE='' SHOW_CFG=0
# DUMP_VARIABLES NAME='gcode_macro FIL_VARS' VALUE='' SHOW_CFG=0
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import time
import json, logging
        
class mmu:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command("FIL_SET_CFS", self.cmd_FIL_SET_CFS, desc=self.cmd_FIL_SET_CFS_help)
        self.box = self.printer.lookup_object('box')
        self.id = config.getfloat("id", default=0.0)
        pass

    def get_status(self, eventtime):
        responseMat = self.box.get_status(eventtime)["same_material"]
        status = []
        material = []
        color = []
        temp = []
        for mat in responseMat:
           status.append(1) 
           matType = mat[3]
           matType = "PLA HIGH SPEED" if "PLA" in matType.upper() else matType
           material.append(matType)# Type "PLA"/"PETG"
           color.append(mat[1][1:])# ColorHex "0FFFFFF" etc to "FFFFFF"
           nozzleTemp = 222 if "PLA" in matType else 245
           temp.append(nozzleTemp)# NozzleTemp 220
        num_gates = len(color)# self.printer.lookup_object('gcode_macro _FIL_VARS').variables['num_gates']
        mmu_status = {
            'num_gates': num_gates, 
            'gate_status': status,
            'gate_material': material,
            'gate_color': color,
            'gate_temperature': temp,
            'box': responseMat,
            'id': self.id
        }
        return mmu_status

    cmd_FIL_SET_CFS_help = "Select using CFS temperature"
    def cmd_FIL_SET_CFS(self, gcmd):
        # TODO start print with CFS enabled
        #self.temp = gcmd.get_float('EXTRUDER_TEMP', default=self.temp, minval=180.0, maxval=320.0)
        #self.gcode.run_script_from_command('NOZZLE_CLEAR HOT_MIN_TEMP=%d HOT_MAX_TEMP=%d BED_MAX_TEMP=%d' % (self.temp, self.temp - 20, self.bed_temp))
        gcmd.respond_info("[FIL_SET_CFS] self={}".format("ok"))
        try:
            print_stats = self.printer.lookup_object('print_stats')
            if True:#print_stats.state == "printing":
               gcmd.respond_info("[FIL_SET_CFS] print_state={}".format(print_stats.state))
        except Exception as err:
            err_msg = "cmd_FIL_SET_CFS err %s" % str(err)
            logging.error(err_msg)
        pass

def load_config(config):
    return mmu(config)
    
    