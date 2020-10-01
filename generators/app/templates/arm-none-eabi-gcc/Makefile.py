import os
from os.path import basename
from pymakelib import git
from pymakelib import MKVARS
from pymakelib import Toolchain as tool

PROJECT_NAME = basename(os.getcwd())
FOLDER_OUT = 'Release/<%= projectName %>/'
TARGET_ELF = FOLDER_OUT + PROJECT_NAME + ".elf"
TARGET_MAP = FOLDER_OUT + PROJECT_NAME + ".map"
TARGET_HEX = FOLDER_OUT + PROJECT_NAME + ".hex"
TARGET_BIN = FOLDER_OUT + PROJECT_NAME + ".bin"
TARGET_SIZE = FOLDER_OUT + PROJECT_NAME + ".size"

def getProjectSettings():
    return {
        'PROJECT_NAME': PROJECT_NAME,
        'FOLDER_OUT':   FOLDER_OUT
    }


def getTargetsScript():
    TARGETS = {
        'TARGET': {
            'LOGKEY':  'OUT',
            'FILE':    TARGET_ELF,
            'SCRIPT':  [MKVARS.LD, '-o', '$@', MKVARS.OBJECTS, MKVARS.LDFLAGS, MKVARS.STATIC_LIBS]
        },
        'TARGET_HEX': {
            'LOGKEY':   'HEX',
            'FILE':     TARGET_HEX,
            'SCRIPT':   [MKVARS.OBJCOPY, '-O', 'ihex', MKVARS.TARGET, TARGET_HEX]
        },
        'TARGET_BIN': {
            'LOGKEY':   'BIN',
            'FILE':     TARGET_BIN,
            'SCRIPT':   [MKVARS.OBJCOPY, '-O', 'binary', MKVARS.TARGET, TARGET_BIN]
        },
        'TARGET_SIZE': {
            'LOGKEY':   'SIZE',
            'FILE':     TARGET_SIZE,
            'SCRIPT':   [MKVARS.SIZE, '-Ax', MKVARS.TARGET, '>', TARGET_SIZE]
        },
        'RESUME':   {
            'LOGKEY':   '>>',
            'FILE':     'RESUME',
            'SCRIPT':   ['@pybuildanalyzer', TARGET_MAP]
        }
    }

    return TARGETS


def getCompilerSet():
    return tool.confARMeabiGCC()


LIBRARIES = []

def getCompilerOpts():

    PROJECT_DEF = {
    }

    return {
        'MACROS': PROJECT_DEF,
        'MACHINE-OPTS': [
        ],
        'OPTIMIZE-OPTS': [
        ],
        'OPTIONS': [
        ],
        'DEBUGGING-OPTS': [
            '-g3'
        ],
        'PREPROCESSOR-OPTS': [
            '-MP',
            '-MMD'
        ],
        'WARNINGS-OPTS': [
        ],
        'CONTROL-C-OPTS': [
            '-std=gnu11'
        ],
        'GENERAL-OPTS': [
        ],
        'LIBRARIES': LIBRARIES
    }


def getLinkerOpts():
    return {
        'LINKER-SCRIPT': [
        ],
        'MACHINE-OPTS': [
        ],
        'GENERAL-OPTS': [
        ],
        'LINKER-OPTS': [
        ],
        'LIBRARIES': LIBRARIES
    }
