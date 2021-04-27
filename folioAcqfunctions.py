import datetime
from datetime import datetime
import json
import uuid
import os
import os.path
import requests
import io
import math
import csv
import time
import random
import logging
import pandas as pd
import validator 

######################
#PURCHASE ORDERS
######################

class purchaseOrder():
    def __init__(self,poNumber,vendor,orderType,orderAcqbill,Order_status):
        self.poNumber=poNumber
        self.vendor=vendor
        self.orderType=orderType
        self.workflowStatus=Order_status
        self.orderAcqbill=orderAcqbill
        
    #polines Online
    def polinesOnline(self,polineAcqmethod,polinecost,polinedetailsInfo,
                      polineEresource,poLineDescription,polinePaymentstatus,polineReceiptstatus,
                      polineDescription,polineIspackage,polineTitle,polineVendordetail):
        poline={}
        poline={
            #"id": polineId,
            "checkinItems": False,
            "acquisitionMethod": polineAcqmethod,
            #"alerts": [],
            #"claims": [],
            "collection": False,
            #"contributors": contributors,
            "cost": polinecost, #{"listUnitPriceElectronic": price,"currency": currency,"discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": price},
            "details": polinedetailsInfo,
            "eresource":polineEresource,# {"activated": False,"createInventory": "None","trial": False, "accessProvider": vendor},
            #"fundDistribution": [],
            "isPackage": False,
            #"locations": [],
            "orderFormat": "Electronic Resource",
            "poLineDescription": poLineDescription,
            "paymentStatus": polinePaymentstatus,
            #"physical": {"createInventory": "None","materialSupplier": vendor,"volumes": []},
            #"poLineNumber": poLineNumber,
            "receiptStatus": polineReceiptstatus,
            #"reportingCodes": [],
            "rush": False,
            "source": "User",
            #"tags": {"tagList": taglist2},
            "description": polineDescription,
            "selector": "",
            "isPackage": polineIspackage, #True/False
            #"packagePoLineId": packagePoLineId,
            "titleOrPackage": polineTitle,
            "vendorDetail": polineVendordetail,
        }
        print(poline)
        return poline
    
    #polines OTHERS
    def polinesOnlineOthers(self,polineId,polineAcqmethod,polinecost,polinedetailsInfo,polineEresource,
                            poLineDescription,polinePaymentstatus,polinephysical,polineReceiptstatus,polineDescription,
                            polineIspackage,polineTitle,polineVendordetail):
        poline={}
        poline={"id": polineId,
                "checkinItems": False,
                "acquisitionMethod": polineAcqmethod,
                #"alerts": [],
                #"claims": [],
                "collection": False,
                #"contributors": contributors,
                "cost" : polinecost,# {"listUnitPrice" : price,"listUnitPriceElectronic" : price,"currency" : currency,"discountType" : "percentage","quantityPhysical" : 1,"quantityElectronic" : 1,"poLineEstimatedPrice" : price},
                #"cost": {"listUnitPriceElectronic": price,"currency": currency,"discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": price},
                "details": polinedetailsInfo,
                "eresource": polineEresource,#{"activated": False,"createInventory": "None","trial": trial, "accessProvider": vendor},
                #"fundDistribution": [],
                "isPackage": False,
                "locations": [],
                "orderFormat": "P/E Mix",
                "poLineDescription": poLineDescription,
                "paymentStatus": polinePaymentstatus,
                "physical": polinephysical,#{"createInventory": "None","materialSupplier": vendor,"volumes": []},
                #"poLineNumber": poLineNumber,
                "receiptStatus": polineReceiptstatus,
                #"reportingCodes": [],
                "rush": False,
                "source": "User",
                #"tags": {"tagList": taglist2},
                "description": polineDescription,
                "selector": "",
                "isPackage": polineIspackage,
                #"packagePoLineId": packagePoLineId,
                "titleOrPackage": polineTitle,
                "vendorDetail": polineVendordetail,
                }
        return poline
    
    #polines Online + Print
    def polinesOnlinePrint(self,polineId,polineAcqmethod,polinecost,
                           polinedetailsInfo,polineEresource,poLineDescription,polinePaymentstatus,polinephysical,
                           polineReceiptstatus,polineDescription,polineIspackage,polineTitle,polineVendordetail):
        poline={}
        poline={ "id": polineId,
            "checkinItems": False,
            "acquisitionMethod": polineAcqmethod,
            #"alerts": [],
            #"claims": [],
            "collection": False,
            #"contributors": contributors,
            "cost":polinecost,# {"listUnitPrice": 0.0,"listUnitPriceElectronic": price,"currency": currency,"discountType": "percentage","quantityPhysical": 1,"quantityElectronic": 1,"poLineEstimatedPrice": price},
            "details": polinedetailsInfo,
            "eresource": polineEresource,#{"activated": False,"createInventory": "None","trial": trial, "accessProvider": vendor},
            ##"fundDistribution": [],
            "isPackage": polineIspackage,
            "locations": [],
            "orderFormat": "P/E Mix",
            "paymentStatus": polinePaymentstatus,
            "poLineDescription": poLineDescription,
            "physical": polinephysical,# {"createInventory": "None","materialSupplier": vendor,"volumes": []},
            #"poLineNumber": poLineNumber,
            "receiptStatus": polineReceiptstatus,
            #"packagePoLineId": packagePoLineId,
            #"reportingCodes": [],
            "rush": False,
            "source": "User",
            #"tags": {"tagList": taglist2},
            "titleOrPackage": polineTitle,
            "vendorDetail": polineVendordetail,
            }
        return poline
    
    #polines Print
    def polinesPrint(self,polineId, polineAcqmethod, polinecost,
                           polinedetailsInfo, polineEresource, poLineDescription, polinePaymentstatus, polinephysical,
                           polineReceiptstatus, polineDescription, polineIspackage, polineTitle, polineVendordetail):
        poline={}
        poline={"id": polineId,
            "checkinItems": False,
            "acquisitionMethod": polineAcqmethod,
            #"alerts": [],
            #"claims": [],
            "collection": False,
            #"contributors": contributors,
            "cost" : polinecost,# {"listUnitPrice" : price,"currency" : currency,"discountType" : "percentage","quantityPhysical" : 1,"poLineEstimatedPrice" : price},
            "details": polinedetailsInfo,
            "eresource": polineEresource,#{"activated": False,"createInventory": "None","trial": trial, "accessProvider": vendor},
            #"fundDistribution": [],
            "isPackage": polineIspackage,
            "locations": [],
            "orderFormat": "Physical Resource",
            "poLineDescription": poLineDescription,
            "paymentStatus": polinePaymentstatus,
            "physical": polinephysical,#{"createInventory": "None","materialSupplier": vendor,"volumes": []},
            #"poLineNumber": poLineNumber,
            "receiptStatus": polineReceiptstatus,
            #"reportingCodes": [],
            "rush": False,
            "source": "User",
            #"tags": {"tagList": taglist2},
            "description": polineDescription,
            "selector": "",
            #"packagePoLineId": packagePoLineId,
            "titleOrPackage": polineTitle,
            "vendorDetail": polineVendordetail,
            }
        return poline

    def polinesOther(self,polineId, polinedetailsInfo, polineEresource, poLineDescription, polinePaymentstatus, polinephysical,
                           polineReceiptstatus, polineinternalnote, polineIspackage, polineTitle, polineVendordetail):
        poline={}
        poline={
            "id": polineId,
            "checkinItems": False,
            "acquisitionMethod": polineId,
            #"alerts": [],
            #"claims": [],
            "collection": False,
            #"contributors": contributors,
            "cost" : polineId,#{"listUnitPrice" : price,"currency" : currency,"discountType" : "percentage","quantityPhysical" : 1,"poLineEstimatedPrice" : price},
            "details": polinedetailsInfo,
            "eresource": polineEresource,#{"activated": False,"createInventory": "None","trial": trial, "accessProvider": vendor},
            #"fundDistribution": [],
            "locations": [],
            "orderFormat": "Other",
            "poLineDescription": poLineDescription,
            "paymentStatus": polinePaymentstatus,
            "physical": polinephysical,#{"createInventory": "None","materialSupplier": vendor,"volumes": []},
            #"poLineNumber": poLineNumber,
            "receiptStatus": polineReceiptstatus,
            #"reportingCodes": [],
            "rush": False,
            "source": "User",
            #"tags": {"tagList": taglist2},
            "description": polineinternalnote,
            "selector": "",
            "isPackage": polineIspackage,
            #"packagePoLineId": packagePoLineId,
            "titleOrPackage": polineTitle,
            "vendorDetail": polineVendordetail,
            }
        return poline    
     
    #MASTER ORDER 
    def masterpurchaseOrders(self,orderPrefix,orderSuffix,ordermanualPo,ordernotes,orderOngoing,
                             orderApproved,orderClosereason,Ordertags,compositePoLines,fileName):
        try:
            orderFile=open(fileName+"_orders.json", 'a')
            order= {
                    #"id":polId,
                    "poNumberPrefix": orderPrefix,
                    "poNumber": self.poNumber,
                    "poNumberSuffix": orderSuffix,
                    "vendor": self.vendor,
                    "orderType": self.orderType,
                    "billTo": self.orderAcqbill,
                    "shipTo": self.orderAcqbill,
                    "manualPo": ordermanualPo,
                    "notes": ordernotes,
                    "reEncumber": False,
                    "ongoing": orderOngoing, #{"interval": interval, "manualRenewal": manualPo, "isSubscription": True,"renewalDate": renewalDate, "reviewPeriod": 90, "notes": notesOngoing},
                    #"totalEstimatedPrice": amount,
                    #"totalItems": totalUnits,
                    "approved": orderApproved,
                    "workflowStatus": self.workflowStatus,
                    "closeReason": orderClosereason, # {"reason": closereason,"note": reasonNote},
                    "tags":Ordertags,
                    "compositePoLines": compositePoLines,
                    #"acqUnitIds":acqunits,
                    }
            
            #json_ord = json.dumps(notes,indent=2)
            json_order = json.dumps(order)
            print('Datos en formato JSON', json_order)
            orderFile.write(json_order+"\n")
            notestatus=True
            return None
        
        except ValueError:
            print("Module folioAcqfunctions Master Orders: "+str(ValueError))

        
################################################
### NOTES
################################################

class notes():
    def __init__(self):
        self.idNotes= str(uuid.uuid4())
    #(uuidOrg,typeId,customerName,15,16,17)
    def print_notes(self,dfRow,typeId,linkId,fileName,*argv):
        notestatus=False
        for arg in argv:
            titleN="Additional notes"
            if dfRow[arg]!="":
                noteFile=open(fileName+"_notes.json", 'a')
                notes ={
                    #"id": self.idNotes,
                    "typeId": typeId,
                    "type": "Organization note",
                    "domain": "organizations",
                    "title": titleN,
                    "content": "<p>"+dfRow[arg]+"</p>",
                    "links":[{"id": linkId,"type": "organization"}]
                    }
                #json_ord = json.dumps(notes,indent=2)
                json_notes = json.dumps(notes)
                #print('Datos en formato JSON', json_notes)
                noteFile.write(json_notes+"\n")
                notestatus=True
        return notestatus
        
################################################
### CONTACTS
################################################
class contactsClass():
    
    def __init__(self,contactID,contactfirstName, contactlastName, contactcategories,contactlanguage):
        self.contactid=contactID
        self.contactfirstName= contactfirstName
        self.contactlastName= contactlastName
        self.language= contactlanguage
        self.contactinactive= False
        self.categories=contactcategories

    def printcontactsClass(self,contactprefix,cont_phone,cont_email, cont_address,cont_urls,cont_categories,contactnotes,fileName):
        contactFile=open(fileName+"_contacts.json", 'a')
        contacto={
                "prefix": contactprefix,
                "id": self.contactid,
                "firstName": self.contactfirstName,
                "lastName": self.contactlastName,
                "language": self.language,
                "notes": contactnotes,
                "phoneNumbers": cont_phone,
                "emails": cont_email,
                "addresses": cont_address,
                "urls": cont_urls,
                "categories": cont_categories,
                "inactive": self.contactinactive,
           }
        json_contact = json.dumps(contacto)
        #print('Datos en formato JSON', json_contact)
        contactFile.write(json_contact+"\n")
        
 
    
#end
################################################
### INTERFACES
################################################
class interfaces():

    def __init__(self,interUuid, intername, interuri, type):
        self.interid=interUuid
        self.intername = intername
        self.interuri = interuri
        self.deliveryMethod= "Online"
        self.interavailable=True
        self.intertype=type
        
    def printinterfaces(self, fileName,notes,statisticsNotes):
        intFile=open(fileName+"_interfaces.json", 'a')
        dato={
            "id": self.interid,
            "name": self.intername,
            "uri": self.interuri,
            "notes":notes,
            "available":self.interavailable,
            "deliveryMethod": self.deliveryMethod,
            "statisticsFormat": "HTML",
            "locallyStored": "",
            "onlineLocation": "",
            "statisticsNotes": statisticsNotes,
            "type": self.intertype
           }
        json_interfaces = json.dumps(dato)
        #print('Datos en formato JSON', json_str)
        intFile.write(json_interfaces+"\n")

### CREDENTIALS
    def printcredentials(self, idInter, login, passW, fileName):
        creFile=open(fileName+"_credentials.json", 'a')
        cred ={
            #"id": str(uuid.uuid4()),
            "username": login, 
            "password": passW,
            "interfaceId": idInter
             }
        json_cred = json.dumps(cred)
        #print('Credentials: ', json_cred)
        creFile.write(json_cred+"\n")
        
    def urltype(self,value):
        urlname=[]
        if value=="1":
            urlname.append("Admin")
            urlname.append("Admin")
        elif value=="2":
            urlname.append("FTP")
            urlname.append("Admin")
        elif value=="3":
            urlname.append("Other")
            urlname.append("Other")
        elif value=="4":
            urlname.append("Statistics")
            urlname.append("End user")
        elif value=="Support":
            urlname.append("Support")
            urlname.append("End user")
        else:
            urlname.append("Other")
            urlname.append("Other")
        return urlname


################################################
### ORGANIZATIONS
################################################
class Organizations():
    def __init__(self,idorg,name,orgcode,vendorisactive,orglanguage):
        self.id=idorg
        self.name=name
        self.code=orgcode
        self.language=orglanguage
        self.exportToAccounting= True
        self.status="Active"
        self.isVendor= True
        self.accounts=[]
            
    def printorganizations(self,org_desc,org_aliases,org_addresses,org_phoneNum,org_emails,org_urls,org_vendorCurrencies,org_contacts, org_interfaces,org_erpCode,fileName):
        orgFile=open(fileName+"_organizations.json", 'a')
        organization= {
                    "id": self.id,
                    "name": self.name,
                    "code": self.code,
                    "erpCode": org_erpCode,
                    "description": org_desc,
                    "exportToAccounting" : self.exportToAccounting,
                    "status": self.status,
                    "language": self.language,
                    "aliases": org_aliases,
                    "addresses": org_addresses,
                    "phoneNumbers": org_phoneNum,
                    "emails": org_emails,
                    "urls": org_urls,
                    "contacts": org_contacts,
                    #"agreements": org_agreements,
                    "vendorCurrencies": org_vendorCurrencies,
                    "claimingInterval": 30,
                    "discountPercent": 0,
                    "expectedInvoiceInterval": 0,
                    "renewalActivationInterval": 0,
                    "interfaces": org_interfaces,
                    "accounts": self.accounts,
                    "isVendor": self.isVendor,
                    "paymentMethod": "EFT",
                    "accessProvider": True,
                    "governmental": False,
                    "licensor": False,
                    "liableForVat": False,
                    "materialSupplier": True,
                    "expectedActivationInterval": 0,
                    "subscriptionInterval": 0,
                    "changelogs": [],
            }
        json_organization = json.dumps(organization)
        #print('Datos en formato JSON', json_organization)
        orgFile.write(json_organization+"\n")    

#end
###############################################
####PURCHASE ORDERS FUNCTIONS
#########################################

def delete_specialcharacters(value):
    try:
        valuefix=""
        Newmpol=""
        keepit=False
        sp_chars = [';', ':', '!', "*","<","/","_","-","(",")","|"," ","@","¿","?","=","#","!"] 
        valuefix = filter(lambda i: i not in sp_chars, value)
        if len(value)>18: 
            valuefix=""
            keepit=True
            for i in range(2):
                Newmpol=str(random.randint(100, 1000))
                with open('oldNew_ordersID.txt', 'a') as clean:
                    clean.write(str(value)+"/"+str(Newmpol)+"\n")
                valuefix=Newmpol            
        return valuefix, keepit
        #if value.find(" ")!=-1: valuefix=value.replace(" ","")
        #if value.find("#")!=-1: valuefix=value.replace("#","")
        #if value.find(">")!=-1: valuefix=value.replace(">","")
        #if value.find("<")!=-1: valuefix=value.replace("<","")
        #if value.find("/")!=-1: valuefix=value.replace("/","")
        #if value.find(":")!=-1: valuefix=value.replace(":","")
        ##if value.find("-")!=-1: valuefix=value.replace("-","")
        ######if value.find("_")!=-1: valuefix=value.replace("_","")
        #if value.find("(")!=-1: valuefix=value.replace("(","")
        #if value.find(")")!=-1: valuefix=value.replace(")","")
        #if value.find("&")!=-1: valuefix=value.replace("&","")
        #if value.find(".")!=-1: valuefix=value.replace(".","")
        #if value.find("'")!=-1: valuefix=value.replace("'","")
        #if value.find(",")!=-1: valuefix=value.replace(",","")
        #if value.find("|")!=-1: valuefix=value.replace("|","")
        #if value.find("!")!=-1: valuefix=value.replace("!","")
        #if value.find("=")!=-1: valuefix=value.replace("=","")
        #if value.find("@")!=-1: valuefix=value.replace("@","")
        #if value.find("?")!=-1: valuefix=value.replace("?","")
        #if value.find("¿")!=-1: valuefix=value.replace("¿","")
        #if value.find("*")!=-1: valuefix=value.replace("*","")
    except ValueError:
        print("Concat Error")
        
def searchKeysByVal(dict, byVal):
    keysList = ""
    keyslist=dict.get(byVal)
    return keyslist

def get_OrgId(searchValue,okapi_url,okapi_token,okapi_tenant):
    try:
        dic={}
        path1=""        
        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
        pathPattern1="/organizations/organizations" #?limit=9999&query=code="
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="organizations"
        query=f"query=code=="
        #/organizations-storage/organizations?query=code==UMPROQ
        paging_q = f"?{query}"+'"'+f"{searchValue}"+'"'
        #paging_q = f"?{query}"+search_string
        path1 = pathPattern1+paging_q
        #data=json.dumps(payload)
        url1 = okapi_url + path1
        req = requests.get(url1, headers=okapi_headers)
        idorg=[]
        #Search by name
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                rec=json_str[element]
                #print(rec)
                l=rec[0]
                if 'id' in l:
                    idorg.append(l['id'])
                    idorg.append(l['name'])
                    return idorg
            #Search by code
            elif (total_recs==0):
                query=f"query=name=="
                paging_q = f"?{query}"+'"'+f"{searchValue}"+'"'
                #paging_q = f"?{query}"+orgname
                path1 = pathPattern1+paging_q
                #data=json.dumps(payload)
                url1 = okapi_url + path1
                req = requests.get(url1, headers=okapi_headers)
                json_str = json.loads(req.text)
                total_recs = int(json_str["totalRecords"])
                if (total_recs!=0):
                    rec=json_str[element]
                    #print(rec)
                    l=rec[0]
                    if 'id' in l:
                        idorg.append(l['id'])
                        idorg.append(l['name'])
                        return idorg
    except requests.exceptions.HTTPError as err:
        print("error Organization GET")

def get_title(searchValue,okapi_url,okapi_token,okapi_tenant):
        dic={}
        #pathPattern="/instance-storage/instances" #?limit=9999&query=code="
        #https://okapi-ua.folio.ebsco.com/instance-storage/instances?query=hrid=="264227"
        pathPattern="/instance-storage/instances" #?limit=9999&query=code="
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="instances"
        #https://okapi-trinitycollegelibrarycambridge.folio.ebsco.com/instance-storage/instances?query=(identifiers any ".b10290242")
        query=f"?query=(identifiers="
        #query=f"query=hrid=="
        #/finance/funds?query=name==UMPROQ
        search='"'+searchValue+'")'
        #.b10290242
        #paging_q = f"?{query}"+search
        paging_q = f"{query} "+search
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idhrid=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                rec=json_str[element]
                #print(rec)
                l=rec[0]
                if 'id' in l:
                    idhrid.append(l['id'])
                    idhrid.append(l['title'])            
        return idhrid
    
def order_cost(additionalCost,currency,discount,discountType,exchangeRate,listUnitPrice,
               listUnitPriceElectronic,quantityPhysical,quantityElectronic,poLineEstimatedPrice):
    #{"listUnitPriceElectronic": price,"currency": currency,"discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": price},
    try:
        coste={}        
        coste["additionalCost"]= additionalCost
        coste["currency"]= currency
        coste["discount"]= ""
        coste["discountType"]= discountType #"percentage"
        coste["exchangeRate"]= exchangeRate
        coste["listUnitPrice"]= listUnitPrice
        coste["listUnitPriceElectronic"]= listUnitPriceElectronic
        coste["quantityPhysical"]= quantityPhysical
        coste["quantityElectronic"]: quantityElectronic
        coste["poLineEstimatedPrice"]= poLineEstimatedPrice
        return coste
    except ValueError:
        print("coste Error")
        
def order_closeReason(reasonvalue, reasonnote):
    try:
        reason={}    
        reason["reason"]=""
        reason["note"]= ""
        return reason
    except ValueError:
        print("Concat Error")
        
def order_costbyElectronic(orderprice,ordercurrency,orderdiscountype,orderquantity, orderpoestimateprice):
    try:#{"listUnitPriceElectronic": price,"currency": currency,"discountType": "percentage","quantityElectronic": 1,"poLineEstimatedPrice": price},
        cost={}
        cost["listUnitPriceElectronic"]=orderprice
        cost["currency"]=ordercurrency
        cost["discountType"]=orderdiscountype
        cost["quantityElectronic"]=orderquantity
        cost["poLineEstimatedPrice"]=orderpoestimateprice
        return cost
    except ValueError:
        print("Concat Error")  
        
         
def order_eresource(eresourceActivated, ecreateInventory,etrial, eaccessprovider):
    try:
    # {"activated": False,"createInventory": "None","trial": False, "accessProvider": vendor},
        eresource={} 
        eresource["activated"]=eresourceActivated
        eresource["createInventory"]=ecreateInventory
        eresource["trial"]=etrial
        eresource["accessProvider"]=eaccessprovider #Vendor ID
        return eresource
    except ValueError:
        print("Concat Error")    
def order_notes(value):
    try:
        orderNote=[]
        orderNote.append(value)
        return orderNote
    except ValueError:
        print("Concat Error")

def order_ongoing(interval, issuscription, manualRenewal, revieperiod, renewaldate):
    try:
        ordOn={}
        if issuscription:
            ordOn["interval"]=interval
            ordOn["isSubscription"]=issuscription
            ordOn["manualRenewal"]=manualRenewal
            ordOn["reviewPeriod"]=revieperiod
            ordOn["renewalDate"]=renewaldate
        else:
            ordOn["isSubscription"]=False
        return ordOn
    except ValueError:
        print("Concat Error")    
def order_tags(value):
    try:
        tags={}
        tagsvalue=[]
        tagsvalue.append(value)
        tagList["tagList"]=tagsvalue
        return tags
    except ValueError:
        print("Concat Error")    
def order_acqUnitId(value):
    adqUni=[]
    adqUni.append(value)
    return value
    
#############################
#GENERAL FUNCTIONS
#############################
def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r*60, 1)
    return (
        int(h),
        int(m),
        int(r*60),
    )
    
################################################
### ORGANIZATIONS FUNCTIONS
################################################
def org_aliases(dfRow,*argv):
    try:
        alia={}
        aliaR=[]
        for arg in argv:
        #print("argumentos de *argv:", row[arg])
            if len(dfRow[arg])>0:
                alia['value']=dfRow[arg]
                alia['description']=""
                aliaR.append(alia)
                alia={}
    except ValueError:
        print("Module folioAcqfunctions organizations aliases Error: "+str(ValueError))
    return aliaR

def org_languages(value):
    try:
        value=value.upper()
        if value=="ENGLISH":
            valueR="eng"
        elif value=="SPANISH":
            valueR="spa"
        elif value=="NULL":
            valueR="eng"
        elif value is None:
            valueR="eng"
        elif value=="":
            valueR=""
        else:
            valueR="eng"
        return valueR
    
    except ValueError:
        print("org_addresses Error: "+str(ValueError))
        
def concatfields(dfRow,*argv):
    try:
        concatfield=""
        for arg in argv:
            if dfRow[arg]:
                concatfield=concatfield+"$"+dfRow[arg]
        if len(concatfield)>0:
            return concatfield
        else:
            return None
    except ValueError:
        print("Concat Error")
        
def org_addresses(dfRow,concat, *argv):
    try:
        if concat:
            addr={}
            addrR=[]
            dir2=""
            dir=""
            cadena=""
            for arg in argv:
                cadena=dfRow[arg]
                if cadena!="$ $ $ $":
                    print(cadena)
                    if len(cadena)>0:
                        x=cadena.count("$")                
                        if (x>0):
                            chunked=cadena.split("$")
                            if (x==1):
                                addr['addressLine1']=chunked[0]
                                addr['addressLine2']=""
                                cadena=chunked[1]
                                if (cadena.find(",")!=-1):
                                    y=cadena.find(",")
                                    addr['city']=cadena[:y]
                                    addr['country']=""
                                    cadena=cadena[y+2:]
                                    if (cadena.find(" ")!=-1):
                                        y=cadena.find(" ")
                                        addr['stateRegion']=cadena[:y]
                                        addr['zipCode']=cadena[y+1:]
                                        addr['categories']=org_categorie("nn")
                                        addr['language']=""
                                        addr["isPrimary"]=True    
                            elif (x==2):
                                addr['addressLine1']=chunked[0]
                                addr['addressLine2']=chunked[1]
                                cadena=chunked[2]
                                if (cadena.find(",")!=-1):
                                    y=cadena.find(",")
                                    addr['city']=cadena[:y]
                                    addr['country']=""
                                    cadena=cadena[y+2:]
                                    if (cadena.find(" ")!=-1):
                                        y=cadena.find(" ")
                                        addr['stateRegion']=cadena[:y]
                                        addr['zipCode']=cadena[y+1:]                     
                                        addr['categories']=org_categorie("nn")
                                        addr['language']=""
                                        addr["isPrimary"]=True    
                            elif (x==3):
                                pass
                            elif (x==4):
                                addr['addressLine1']=dfRow[10]
                                addr['addressLine2']=dfRow[11]
                                addr['city']=dfRow[12]
                                addr['stateRegion']=dfRow[13]
                                addr['zipCode']=dfRow[14]
                                addr['country']=""
                                addr['categories']=org_categorie("nn")
                                addr['language']=""
                                addr["isPrimary"]=True
                                addrR.append(addr)

                            elif (x==5):
                                pass
                    else:
                        addr['addressLine1']=dfRow[arg]
                        addr['addressLine2']=""
                        addr['city']=""
                        addr['stateRegion']=""
                        addr['zipCode']=""
                        addr['country']=""
                        addr['categories']=org_categorie("nn")
                        addr['language']=""
                        addr["isPrimary"]=True
                    addrR.append(addr)
                    cadena=""
                    addr={}
                return addrR
        
            return addrR
    except ValueError:
            print("org_addresses Error: "+str(ValueError))
        
    
def org_phoneNumbers(dfRow,*argv):
    pho={}
    phoR=[]
    for arg in argv:
        #print("argumentos de *argv:", row[arg])
        if len(dfRow[arg])>0:
            pho["phoneNumber"]=dfRow[arg]
            pho["categories"]=org_categorie("")
            pho["language"]="en-us"
            pho["type"]=dfRow[arg+1],
            pho["isPrimary"]= True
            phoR.append(pho)
            pho={}
    return phoR


def org_emails(dfRow,*argv):
    emai={}
    emaiR=[]
    for arg in argv:
        #print("argumentos de *argv:", row[arg])
        if len(dfRow[arg])>0:
            emai['value']=dfRow[arg] 
            emai['description']="" 
            emai['categories']=org_categorie("nn")
            emai['language']="en-us" 
            emai['isPrimary']=True
            emaiR.append(emai)
            emai={}
    return emaiR

def org_urls(dfRow,*argv):
    urls={}
    urlsR=[]
    for arg in argv:
        #print("argumentos de *argv:", row[arg])
        if len(dfRow[arg])>0:
            if (dfRow[arg].find("http://")!=-1): 
                urls['value']=dfRow[arg]
            else:
                urls['value']="http://"+dfRow[arg]
            urls['description']=""
            urls['language']=""
            urls['categories']=org_categorie("nn")
            urls['notes']=""
            urlsR.append(urls)
            urls={}
    return urlsR

def org_contacts(dfRow, *argv):
    contactsId=[]
    person={}
    for arg in argv:
        #print("argumentos de *argv:", row[arg])
        if len(dfRow[arg])>0:
            if dfRow[arg]:
                contactprefix= dfRow[arg]
                contactName_temp=str(dfRow[arg])+" "+str(dfRow[arg])
                ContactName=SplitString(contactName_temp)
                FN=str(ContactName[0])
                LN=str(ContactName[1])
            else:
                FN="NaN"
                LN="NaN"
                #Title go to notes and categorical
                #contactTitle="NULL"
                #if namesheet.cell_value(c,4)!="NULL":
                #    contactTitle=str(namesheet.cell_value(c,4))
                #address
            contactLang="en-us"
            contactnotes=""
            addcontnote=True
            if addcontnote:
                if dfRow[arg]:
                    contactnotes=contact_notes(dfRow[arg])

            addcono=True
            if addcono:
                if dfRow[arg]:
                    contactnotes= dfRow[arg]
            #Contacts phone
            contactphoneN=[]
            addpho=True
            if addpho:
                contactphoneN=""
                contactphoneN=org_phoneNumbers(dfRow[arg],23,31,35,39,)
            #Contact emails
            contactemail=[]
            addmails=True
            if addmails:
                contactemail=""
                contactemail=org_emails(dfRow[arg],15,23)

            #Contact Address
            contactaddresses=[]
            addadd=False
            if addadd:
                contactaddresses=""
                contactaddresses=org_addresses(dfRow[arg],47)

            #INACTIVE / ACTIVE
            contactinactive= False
            #Contact URL
            contacturls=[]
            addurl=False
            if addurl:
                contacturls="" 
                contacturls=org_urls(dfRow[arg],43)
                
            contcategories=[]
            if dfRow[6]:
                contcategories=org_categorie(dfRow[arg])
            conID=str(uuid.uuid4())
            contactsId.append(conID)
            #(self,contactID,contactfirstName, contactlastName, contactcategories):
            ctc=contactsClass(conID,FN,LN,contcategories,contactLang)
            #def printcontacts(self,cont_phone,cont_email, cont_address,cont_urls,cont_categories,contactnotes,fileName):
            ctc.printcontactsClass(contactprefix,contactphoneN, contactemail, contactaddresses, contacturls,contcategories,contactnotes,customerName)  
    return contactsId


def org_account(dfRow,*argv):
    accou={}
    accouR=[]
    for arg in argv:
        print("argumentos de *argv:", dfRow[arg])
        accouR.append(accou)
        accou={}
    return accouR

def org_acqunit(dfRow,*argv):
    acqunit={}
    acqunitR=[]
    for arg in argv:
        print("argumentos de *argv:", dfRow[arg])
        acqunit.append(acqunit)
        acquint={}
    return acqunit

def org_agreements(dfRow,*argv):
    agre={}
    for arg in argv:            
        agre["name"]= "History Follower Incentive"
        agre["discount"]= 10
        agre["referenceUrl"]= "http://my_sample_agreement.com"
        agre["notes"]= "note"
    return agre


def contact_notes(dfRow,*argv):
    nt=""
    for arg in argv:
        if (dfRow.find(' - ') !=-1):
            result=dfRow.find(' - ')
            nt=dfRow[result+3:]
        elif (dfRow.find(' -- ') !=-1):
            result=dfRow.find(' -- ')
            nt=dfRow[result+3:]
        elif (dfRow.find('; ') !=-1):
            result=dfRow.find('; ')
            nt=dfRow[result+2:]
        elif (dfRow.find(' | ') !=-1):
            result=dfRow.find(' | ')
            nt=dfRow[result+3:]
        elif (dfRow.find(' / ') !=-1):
            result=dfRow.find(' / ')
            nt=dfRow[result+3:]
        elif (dfRow.find(', ') !=-1):
            result=dfRow.find(', ')
            nt=dfRow[result+2:]
        else:
            nt=dfRow[arg]
    return nt

def org_categorie(valueA):
    catego=[]
    
    if valueA=="company URL":
        catego.append("d963c6fa-7aa8-4b65-8f64-5f119ef17cd1")
    elif valueA=="Office":
        catego.append("6a60106e-6ffb-4e02-a872-f6941f76245e")
    elif valueA=="Fax":
        catego.append("d78d4e2e-11f9-4397-971e-300cb3dd8522")
    elif valueA=="nn":
        catego=[] #GENERAL
    else:
        value=cat(valueA)
        if len(value)>0:
            catego.append(value)
    return catego
#end

def get_licId(orgname):
        dic={}
        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
        #https://okapi-macewan.folio.ebsco.com/licenses/licenses?stats=true&term=Teatro Español del Siglo de Oro&match=name
        pathPattern="/licenses/licenses" #?limit=9999&query=code="
        okapi_url="https://okapi-macewan.folio.ebsco.com"
        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJfaWQiOiI4MjEzODdhZS1hNzkxLTQ5NTgtYTg3ZS1jYTFmMDE2NzA2YmUiLCJpYXQiOjE2MTA5MzAwMjEsInRlbmFudCI6ImZzMDAwMDEwMzcifQ.ygLWuFDNUT8No5TF6FD9NNRpNk4Z_iSRVmPmxaH_UsE"
        okapi_tenant="fs00001037"
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="organizations"
        query=f"?stats=true&term="
        #/organizations-storage/organizations?query=code==UMPROQ
        paging_q = f"{query}"+orgname+"&match=name"
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idorg=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                #print('Datos en formato JSON',json.dumps(json_str))
                rec=json_str["results"]
                #print(json_str)
                l=rec[0]
                if 'id' in l:
                    idorg.append(l['id'])
                    #idorg.append(l['name'])
        if len(idorg)==0:
            return "00000-000000-000000-00000"
        else:
            return idorg
        
def urlValidator(value):
    try:
        valid=False
        #valid=validator.url(str(value))
        if (value.find("http")!= -1):
            #print("Url is valid only for folio ")
            valid=True
        return valid
    except ValueError:
        print("error")
        
def is_empty(data_structure):
    if data_structure:
            #print("No está vacía")
            return False
    else:
            #print("Está vacía")
            return True

def interfacetype(categ):
    catego=[]
    if (categ.find('Admin') != -1): catego.append("Admin")
    if (categ.find('Statistics') != -1): catego.append("Admin")
    if (categ.find('End user') != -1): catego.append("End user")
    if (categ.find('Other') != -1): catego.append("Other")
    if (categ.find('Report') != -1): catego.append("Report")
    return catego


def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r*60, 1)
    return (
        int(h),
        int(m),
        int(r*60),
    )
    
def cat(categ):
        dic={}
        #https://okapi-liverpool-ac-uk.folio.ebsco.com/organizations-storage/categories?query=value=="Sales"
        pathPattern="/organizations-storage/categories" #?limit=9999&query=code="
        okapi_url="https://okapi-utm.folio.ebsco.com"
        okapi_token="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJfaWQiOiJiNWM4YzFmOS02YzQxLTRhMzgtYjk1ZS03YTk5ZTgxMTM3MjUiLCJpYXQiOjE2MTg4NTI5NzMsInRlbmFudCI6ImZzMDAwMDEwNTMifQ.kKuVc2PdXuEgQioN2jphmFw4AdVmKkngoYMdZrfSJ54"
        okapi_tenant="fs00001053"
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="categories"
        query=f"query=value=="
        #/finance/funds?query=name==UMPROQ
        search='"'+categ+'"'
        #paging_q = f"?{query}"+search
        paging_q = f"?{query}"+search
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idcat=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                rec=json_str[element]
                #print(rec)
                l=rec[0]
                if 'id' in l:
                    idcat.append(l['id'])                   
        return idcat
#END


def exitfile(arch):    
    if os.path.isfile(arch):
        print ("File exist")
        os.remove(arch)
    else:
        print ("File not exist")


def search(fileB,code_search):
    idlicense=""
    foundc=False
    with open(fileB,'r',encoding = 'utf-8') as h:
        for lineh in h:
            if (lineh.find(code_search) != -1):
                #print(lineh)
                foundc=True
                if (foundc):                    
                    idlicense=lineh[8:44]
                    break
    if (foundc):
        return idlicense
    else:
        idlicense="No Vendor"
        return idlicense


def SplitString(string_to_split):
    string_fn=""
    string_ln=""
    if (string_to_split.find('@') !=-1):
            result=string_to_split.find('@')
            largo=len(string_to_split)
            #print("largo:", largo)
            #print("position @:",result)
            string_fn=" "
            string_ln=string_to_split[0:result]
    elif (string_to_split.find(' ') !=-1):
            largo=len(string_to_split)
            result=string_to_split.find(' ')
            #print("Large:", largo)
            #print("position blank:",result)
            string_fn=string_to_split[0:result]
            string_ln=string_to_split[result+1:largo]
            if (string_ln.find(' - ') !=-1):
                result=string_ln.find(' - ')
                #print("Large:", largo)
                #print("position blank:",result)
                string_ln=string_ln[:result]
            elif (string_ln.find(', ') !=-1):
                result=string_ln.find(', ')
                #print("Large:", largo)
                #print("position blank:",result)
                string_ln=string_ln[:result]


    else:
            #print("is not last name, first name")    
            string_fn=" "
            string_ln=string_to_split
    return string_fn, string_ln

###########################
### LICENCES FUNCTIONS
##########################

def get_licId(licToSearch,okapi_url,okapi_token,okapi_tenant):
    try:
        dic={}
        #pathPattern="/organizations-storage/organizations" #?limit=9999&query=code="
        #https://okapi-macewan.folio.ebsco.com/licenses/licenses?stats=true&term=Teatro Español del Siglo de Oro&match=name
        pathPattern="/licenses/licenses" #?limit=9999&query=code="
        okapi_headers = {"x-okapi-token": okapi_token,"x-okapi-tenant": okapi_tenant,"content-type": "application/json"}
        length="1"
        start="1"
        element="organizations"
        query=f"?stats=true&term="
        #/organizations-storage/organizations?query=code==UMPROQ
        paging_q = f"{query}"+licToSearch+"&match=name"
        path = pathPattern+paging_q
        #data=json.dumps(payload)
        url = okapi_url + path
        req = requests.get(url, headers=okapi_headers)
        idorg=[]
        if req.status_code != 201:
            json_str = json.loads(req.text)
            total_recs = int(json_str["totalRecords"])
            if (total_recs!=0):
                #print('Datos en formato JSON',json.dumps(json_str))
                rec=json_str["results"]
                #print(json_str)
                l=rec[0]
                if 'id' in l:
                    idorg.append(l['id'])
                    #idorg.append(l['name'])

    except ValueError as error:
            print("Error: %s" % error)

######END

###################
###NOTES
####################
def print_notes(title,linkId,cont,path):
    try:
        Ordarchivo=open(path+"notes.json", 'a')
        tn="bb2b5a44-c017-46a2-a9d5-89e4920e99f2"
        notes ={
           "typeId": tn,
           "type": "General note",
           "domain": "licenses",
           "title": title,
           "content": "<p>"+cont+"</p>",
           "links": [{"id": linkId[0],"type": "license"}]
           }
        json_ord = json.dumps(notes,indent=2)
        json_notes = json.dumps(notes)
        print('Datos en formato JSON', json_notes)
        Ordarchivo.write(json_notes+"\n")
    except ValueError as error:
            print("Error: %s" % error)
######END NOTES

def readFileToDataFrame(file_path):
    try:
        filename = r"{}".format(file_path)
        if filename[-4:] == ".csv":
                df = pd.read_csv(filename)
        else:
                df = pd.read_excel(filename)
                
        #license = license.sort_values(by="RECORD #(LICENSE)", ascending=False)
        print("Total rows: {0}".format(len(df)))
        #print('\n'*5)
        #Cleaning licenses section for vendorsframe
        #Replacing NaN content by blank
        df = df.apply(lambda x: x.fillna(""))
        df = df.replace("-","", regex=True)
        #is there duplicated content in the orgCode?
        #print("Duplicate vendors= ",df.duplicated(subset = 'RECORD #(LICENSE)').sum())
        return df
    except ValueError as error:
            print("Error: %s" % error)