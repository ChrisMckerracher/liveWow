from pyflink.common.watermark_strategy import TimestampAssigner


class LogLineTimestampSupplier(TimestampAssigner):

    def extract_timestamp(self, value, record_timestamp):
        #1/3 14:45:02.903  SPELL_AURA_APPLIED,Player-76-0B98C34D,"Anonymous-Server",0x518,0x0,Player-76-0B98C34D,"Vissarra-Sargeras",0x518,0x0,154796,"Touch of Elune - Day",0x1,BUFF
        return value.split(" ")[1].strip(" ")
