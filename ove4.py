#!/usr/bin/env python)

## Test for og hente snmp data

import snmp_helper

def main():

   if True:
      IP = '50.76.53.27'
      a_user = 'pysnmp'
      auth_key = 'galileo1'
      encrypt_key = 'galileo1'
      snmp_user = (a_user, auth_key, encrypt_key)
      pynet_rtr1 = (IP, 7961)
      pynet_rtr2 = (IP, 8061)

   snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.1.5.0')
   output = snmp_helper.snmp_extract(snmp_data)
   print output

if __name__ == "__main__":
    main()
