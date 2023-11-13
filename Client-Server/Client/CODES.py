class OPCODE:
    OPSUCCESS = '222'
    OPFAILURE = '111'
    ALREADYEXISTS = '101'
    INVALIDOPTION = '103'

def opcode_check(opcode,checker):
    match opcode:
        case OPCODE.OPSUCCESS:    
            print("SIGN UP SUCCESSFUL")
            checker = True
        case OPCODE.INVALIDOPTION:
            print("INVALID USERNAME/PASSWORD")
            checker= False
        case OPCODE.ALREADYEXISTS:
            print("USERNAME ALREADY EXISTS")
            checker= False
        case _:
            print("NOT RECOGNIZED")
            checker= False