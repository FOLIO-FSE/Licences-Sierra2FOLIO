import json
import uuid
import os
import os.path
import datetime
from datetime import datetime
import requests
import pandas as pd
import time
import datetime
import folioAcqfunctions as faf
import ast

class licenses():
    def __init__(self,id):
        self.id=id
        # licenses.licencePrint(self, ermName, vendor[0], vendor[1],ermDescription, ERMlicType, ERMlicstatus, ErmstartDate, ermendDate,docs)

    def licencePrint(self, ermName, vendor,ermDescription, ERMlicType, ERMlicstatus, ErmstartDate, ermendDate,docs,
                     aliases,ermopenEnded,cp,path):
        try:
            Ordarchivo=open("licenses.json", 'a')
            license = {
                #"id": "1ece2ebf-7999-4720-8399-d3c04022647c",
                #"dateCreated": "2021-18-29T15:33:02Z",
                "links": [],
                "description": ermDescription,
                "customProperties": cp,
                "contacts": [],                
                "tags": [],
                #"lastUpdated": "2021-04-26T00:00:00Z",
                "docs":docs,
                "name": ermName,
                "status": ERMlicstatus,
                "supplementaryDocs": [],
                "startDate": ErmstartDate,
                "endDate": ermendDate,
                "_links": {"linkedResources": {"href": "/licenses/licenseLinks?filter=owner.id%"}},
                "openEnded": ermopenEnded,
                "amendments": [],
                "orgs": vendor,
                "type": ERMlicType,
                "alternateNames": aliases
                }
            license=str(license)
            json_ord = ast.literal_eval(json.dumps(license))
            #json_ord = json.dumps(order,indent=2)
            #json_ord = json.dumps(license)
                                      
            #print('Datos en formato JSON', json_ord)
            Ordarchivo.write(json_ord+"\n")
    
        except ValueError as error:
            print("invalid json: %s" % error)
#######

def date_stamp(ilsdate):
    dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(ilsdate) - 2)
    hour, minute, second = floatHourToTime(ilsdate % 1)
    dt = str(dt.replace(hour=hour, minute=minute,second=second))+".000+0000" #Approbal by
    dia=dt[8:10]
    mes=dt[5:7]
    ano=dt[0:4]
    dt=ano+"-"+mes+"-"+dia
    return dt

def notes(spreadsheet,org):
    print_notes(title,linkId,content)

######################### LAFAYETTE
def searchNestedDictByVal(dicToInspect, Dickey, DicVal):
    try:
        #def getKeysByValues(dictOfElements, Dickey):
        listOfKeys = list()
        listOfItems = dicToInspect.items()
        print(listOfItems)
        for item  in listOfItems:
            if item[1] in Dickey:
                listOfKeys.append(item[0])
                print(listOfKeys)
        #keyslist=dicToInspect.get(Dickey)
        #print(keyslist)
        #if keyslist:
            
        
        #dicttemp={}
        #for key, value in dicToInspect.items():
        #    print("Terms:", key)
        #for k, v in value.items():
        #    print(k + ":", value[k])
        #    dicttemp=value[k]
        #    keyslist=dicttemp.get(DicVal)
            #keyslist=dict.get(byVal)
        #if isinstance(byVal, dicToInspect):
        #    for key, value in byVal.items():
        #        searchNestedDictByVal(value, val_to_find, indexpath + f"['{key}']")
        return None
    except ValueError:
        print("error Search Nested dict")

#tof = False
#for value in listDict.values():
#  if ('e' in value):
#    tof = True
#    break
#print(tof)

def searchKeysByVal(dicToInspect, byVal):
    try:
        dic={}
        keysList = ""
        keyslist=dicToInspect.get(byVal)
        dic["label"]=keyslist.capitalize()
        keyslist=keyslist.replace(" ","_")
        keyslist=keyslist.lower()
        dic["value"]=keyslist
        #print(dic)
        return dic
    except ValueError:
        print("Error license Status")
        
def license_docs(dfRow,*argv):
    try:
        docsR=[]
        licDoc={}
        for arg in argv:
            if len(dfRow[arg])>0:
                if faf.urlValidator(dfRow[arg]):
                    licDoc["url"]= dfRow[arg]
                else:
                    licDoc["note"]= "Please enter a valid URL (including http or https)"
                    licDoc["url"]= "http://"+dfRow[arg]
                licDoc["name"]= "URL"
            docsR.append(licDoc)
            licDoc={}
        return docsR
    except ValueError:
        print("Error license Docs")

def license_organizations(dfRow,*argv,customer):
        try:    
                dic = {}
                orgs=[]
                licenseOrg={}
                for arg in argv:
                        #print("argumentos de *argv:", row[arg])
                        if len(dfRow[arg])>0:
                                #print(dfRow[arg])
                                toSearch=str(dfRow[arg])
                                toSearch=toSearch.replace("&"," ")
                                provider=faf.get_OrgId(toSearch,okapi_url="https://okapi-lafayette.folio.ebsco.com",okapi_token="",okapi_tenant="fs00001054")
                                if provider:
                                        licenseOrg["orgsUuid"]=provider[0]
                                        licenseOrg["name"]=provider[1]
                                #"orgs": [{"id": "", "org": {"id": "", "orgsUuid": "19fdabf3-b73a-4da1-bb5b-25e4aa737ab7", "name": "Proquest Info Learning Co"}, "role": {"id": "", "value": "licensor", "label": "Licensor"}}
                                else:
                                        #Define undefined provider
                                        licenseOrg["orgsUuid"]="1e94d6db-e89d-43fe-afe5-09a2f5a24866"
                                        licenseOrg["name"]="undefined"
                                dic["id"]=""
                                dic["org"]=licenseOrg
                                dic["note"]="Org name not found "+str(dfRow[arg])
                                if arg==1:                                                
                                        dic["role"]= {"value": "licensee", "label": "Licensee"}
                                elif arg==2:
                                        dic["role"]= {"value": "licensor", "label": "Licensor"}
                                if provider: dic["note"]=""
                                licenseOrg={}
                                orgs.append(dic)
                                dic={}
                #print(orgs)
                return orgs
        except ValueError:
                print("Error license Organizations")
                
def searchDataframe(pathOrg,idSearch):
        try:
           if pathOrg[-4:] == ".csv":
              organization = pd.read_csv(pathOrg)
           else:
                organization = pd.read_excel(pathOrg)
                        
           organization = organization.sort_values(by="RECORD #(LICENSE)", ascending=False)
           #print("Total rows: {0}".format(len(organization)))
           #print('\n'*5)
           #Cleaning licenses section for vendorsframe
           #Replacing NaN content by blank
           organization = organization.apply(lambda x: x.fillna(""))
           
           #is there duplicated content in the orgCode?
           #print("Duplicate vendors= ",organization.duplicated(subset = 'RECORD #(LICENSE)').sum())
           organization_filter = organization[organization['RECORD #(LICENSE)']== idSearch]
           #print("organizations founds: ",len(organization_filter))
           for c, rowc in organization_filter.iterrows():
                return(organization_filter.loc[c])
                                
        except ValueError:
                print("error license organizations")

def json_validator(data):
    try:
        json_data = ast.literal_eval(json.dumps(data))
        #print(json_data)
        #json.loads(json_data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False
                
def get_note(dfNote,value1):
    try:
        head1=list(dfNote.keys())
        #print(dfNote[1])        
        notesR=""
        path_org: str=r"C:\Users\asoto\Documents\EBSCO\Migrations\folio\Lafayette"
        filename="License_export2_variable_fields.xlsx"
        rowdata=searchDataframe(f"{path_dir}/{filename}",str(dfNote[1]).strip())
        if value1=="ILL":
            if rowdata[18]:
                notesR=str(rowdata[18]).strip()
        elif value1=="DISCLOSURE":
            if rowdata[19]:
                notesR=str(rowdata[19]).strip()
        elif value1=="DISABILTY":
            if rowdata[23]:
                notesR=str(rowdata[23]).strip()
        elif value1=="WARRANTY":
            if rowdata[22]:
                notesR=str(rowdata[22]).strip()
        elif value1=="ARCHIVES":
            if rowdata[21]:
                 notesR=str(rowdata[21]).strip()
        elif value1=="PERPTL ACS":
            if rowdata[20]:
                notesR=str(rowdata[20]).strip()
        elif value1=="INDEMNIF":
            if rowdata[24]:
                notesR=str(rowdata[24]).strip()
        elif value1=="LAW VENUE":
            if rowdata[25]:
                notesR=str(rowdata[25]).strip()
        return notesR
    except ValueError:
        print("Error")
                
def cpterm_TextInteger(dfRow,*argv):
    try:
        cp=[]        
        head=list(dfRow.keys())
        coR={}
        cpvalues={}
        notetemp=""
        #dictempa=dfRow
        for arg in argv:
                #print(arg)
                termCp=f"{head[arg]}"
                if dfRow[arg]:
                    cpvalues["note"]=""
                    cpvalues["internal"]= True
                    notetemp=get_note(dfRow,termCp)
                    if notetemp:
                        cpvalues["note"]=notetemp
                    cpvalues["value"]=dfRow[arg]                   
                    #cpvalues["id"]=""
                    cp.append(cpvalues)
                    cpvalues={}
                    termCp=termCp.replace(" ","")
                    coR[termCp]=cp
                    cp=[]
                    #print(coR)
        return coR        
    except ValueError:
        print("Error")
                
                
#def cpterm_Integer(dfRow,*argv):
#    try:
#        cp=[]
#        head=list(dfRow.keys())
#        coR={}
#        cpvalues={}
#        #dictempa=dfRow
#        for arg in argv:
#                #print(arg)
#                termCp=f"{head[arg]}"
#                if dfRow[arg]:                    
#                    cpvalues["value"]=int(dfRow[arg])
#                    cpvalues["note"]=""
#                    notetemp=get_note(dfRow)
#                    if notetemp:
#                        cpvalues["note"]=notetemp
#                    #cpvalues["id"]=""
#                    cp.append(cpvalues)
#                    cpvalues={}                    termCp=termCp.replace(" ","")
# if                coR[termCp]=cp
#                    cp=[]
#                   #print(coR)
#       return coR        
#   except ValueError:
#       print("Error")
        
def cpterm_PickupList(dfRow,*argv, **kwargs):
    try:
        dicTermtemp=kwargs
        #print(dicTermtemp)
        cp=[]
        head=list(dfRow.keys())
        coR={}
        cpvalues={}
        notetemp=""
        #dictempa=dfRow
        for arg in argv:
                #print(arg)
                termCp=f"{head[arg]}"
                if dfRow[arg]:                    
                    #print(dfRow[arg])
                    #print(dicTerms['CONFIDENTL']['c'])
                    #print(dicTermtemp['dictiorarylicTerms'][termCp])
                    cpvalues["note"]=""
                    cpvalues["internal"]= True
                    notetemp=get_note(dfRow,termCp)
                    if notetemp:
                        cpvalues["note"]=notetemp
                    #cpvalues["id"]=""
                    inspectDic=dicTermtemp['dictiorarylicTerms'][termCp]
                    cpvalues["value"]=searchKeysByVal(inspectDic,dfRow[arg])
                    cp.append(cpvalues)
                    cpvalues={}
                    termCp=termCp.replace("LCODE1","ILL")
                    termCp=termCp.replace("LCODE2","E-RESERVES")
                    termCp=termCp.replace("LCODE3","LICENSE CODE 3")
                    termCp=termCp.replace("LCODE3","TEXTDATA")
                    termCp=termCp.replace("TEXT/DATA","TEXTDATA")
                    termCp=termCp.replace(" ","")
                    coR[termCp]=cp
                    cp=[]
                    #print(coR)
        #json_validator(str(coR))            
        return coR        
    except ValueError:
        print("Error")
        


def readSpreadsheet(file_path,org):
        try:
            ## LICENCES TERMS AND CONDITIONS
                dicTerms= {
                "CONFIDENTL":{"c":"All Confident", "n": "None Confident", "o": "Other (see disclosure note)", "p":"Price Only", "u":"Unknown"},
                "TEXT/DATA": {"n":"No", "y":"Yes", "u": "Unknown", "c":"Check license"},
                "WARRANTY": {"n":"No", "y":"Yes", "u": "Unknown", "c":"Check license"},
                "USER CONF": {"n":"No", "y": "Yes", "u": "Unknown", "c": "Check license"},
                "TYPE": {"x":"Clickthru", "c": "Consortium", "l": "Limited site", "y":"Shrinkwrap", "s":"Site license", "u":"unknown"},
                "SUPPRESS": {"-":"Display normal", "n": "No display"},
                "STATUS": {"v":"Active", "e": "Expired", "p": "Pending", "u": "Unknown"},
                "PERPTL ACS": {"n":"No", "y":"Yes", "u": "Unknown", "o":"Other (See Note)"},
                "LCODE3": {"y":"Yes mining", "n": "No mining", "o": "Other (See Note)"},
                "LCODE2": {"n":"No", "y": "Yes", "u": "Unknown", "o": "Other (See Note)"},
                "LCODE1": {"f" : "Any format", "n": "No ILL allowed", "o": "Other (See Note)", "a": "Print/Ariel", "p": "Print only", "u": "unknown"},
                "LAW VENUE": {"o":"other", "p": "PA", "s": "Silent", "u": "Unknown"},
                "INDEMNIF": {"w":"By institution", "p": "By provider", "c": "Check license", "m": "Mutual", "n": "See note", "u": "Unknown"},
                "DISABILTY": {"n":"No", "y":"Yes", "u": "Unknown", "c":"Check license"},
                "AUTO RENEW": {"n":"No", "y": "Yes", "u":"Unknown"},
                "ARCHIVES": {"n":"No", "y":"Yes", "u": "Unknown", "o": "Other (See Note)"}
                
                }
                #print(dicTerms)
                #print(dicTerms['CONFIDENTL']['c'])
                #print(dicTerms[1]['WARRANTY'])
                #print(dicTerms[1]['TYPE'])
                license=faf.readFileToDataFrame(file_path)
                #list={}
                contact_Id=""
                interface_Id=""
                org_erpCode=""
                nextorg=""
                #excel_filename = r"{}".format(file_path)
                #if excel_filename[-4:] == ".csv":
                #        license = pd.read_csv(excel_filename)
                #else:
                #        license = pd.read_excel(excel_filename)
                        
                license = license.sort_values(by="RECORD #(LICENSE)", ascending=False)
                print("Total rows: {0}".format(len(license)))
                #print('\n'*5)
                #Cleaning licenses section for vendorsframe
                #Replacing NaN content by blank
                #license = license.apply(lambda x: x.fillna(""))
                #license = license.replace("-","", regex=True)
                #is there duplicated content in the orgCode?
                print("Duplicate vendors= ",license.duplicated(subset = 'RECORD #(LICENSE)').sum())
                #Need to delete duplicated rows
                #df.drop_duplicates(keep = 'first', inplace = True))
                ##loop through each row in range()
                nextorg=""
                cont=0
                for i, row in license.iterrows():
                        cont=cont+1
                        tic = time.perf_counter()
                        lic_links=[]
                        #Add license Name
                        lic_name=""
                        addname=True
                        if addname:
                                lic_name=str(row[0]).strip()
                        ##PRINT SEQUENCE
                        print(lic_name+" "+str(cont)+" / "+str(len(license)))
                        #License Alternative Name
                        lic_alternateNames=[]
                        addlicalte=False
                        if addlicalte:
                               lic_alternateNames=""
                               lic_alternateNames=license_alternateNames()
                                
                        #add license Status (to include dicctionary lic_statDictionary={"v":["id","Active"],"e":["id","Expired"],"p":["id","Pending"],"u":["id","Unkown"]})
                        #lic_statDictionary={"v":["2c91808b76863753017688df315a0045","active"],"e":["2c91808b76863753017688df31870047","expired"],"p":["2c91809078f005b401790b083df20001","pending"],"u":["2c91809078f005b401790b09cd5c0002","unknown"]}
                        lic_dicStatus={"v":"active","e":"expired","p":"pending","u":"unknown"}
                        lic_status={}
                        addlicstatus=True
                        if addlicstatus:
                                licStatus=row[4].strip()
                                if licStatus:
                                        lic_status=searchKeysByVal(lic_dicStatus,licStatus)
                                else:
                                        lic_status={"value": "unknown","label":"Unknow"}
                                        
                        #Add license Type
                        #blank -, x Clickthru, c Consortium, l Limited site, y Shrinkwrap, s Site license, u unknown
                        #lic_typeDiccionary={"x":["id","value"]}
                        #lic_dicType={"l":"Limited side","x":"Clickthru","c":"Consortium","y":"Shrinkwrap","s":"Site license","u":"Unknown"}
                        lic_dicType={"x":"Clickthru", "c": "Consortium", "l": "Limited site", "y":"Shrinkwrap", "s":"Site license", "u":"unknown"}
                        lic_type=""
                        addlictype=True
                        if addlictype:
                                if row[5]:
                                        licType=row[5].strip()
                                        lic_type=searchKeysByVal(lic_dicType,licType)
                                else:
                                        lic_type={"value": "site_license","label": "Site License"}
                            
                        
                        #StartDate license
                        lic_startDate=""
                        addlicstarDate=True
                        if addlicstarDate:
                                if row[21]:
                                        lic_startDate=str(row[21]).strip()
                                        lic_startDate=lic_startDate[:10]

                                
                        #EndDate License Format lic_startDate= "2019-07-01"
                        lic_endDate=""
                        addlicEnddate=True
                        if addlicEnddate:
                                if row[22]:
                                        lic_endDate=str(row[22]).strip()
                                        lic_endDate=lic_endDate[:10]
                                
                        #License OpenEnddate
                        lic_openEnded=False
                        if lic_endDate=="":
                                lic_openEnded=True
                                   
                        ##Description license
                        lic_description=""
                        addlicDesc=False
                        if addlicDesc:
                                lic_description=""
                                
                        #Add contacts
                        lic_contacts=[]
                        addliccont=False
                        if addliccont:
                                lic_contacts=""
                                lic_contacts=license_contacts()
                        #addtags
                        lic_tags=[]
                        addtag=False
                        if addtag:
                                lic_tags=""
                                lic_tags=license_tags()

                        ###################
                        ##LINK EXTERNAL DOCUMENT
                        ################
                        path_org: str=r"C:\Users\asoto\Documents\EBSCO\Migrations\folio\Lafayette"
                        filename="License_export2_variable_fields.xlsx"
                        rowdata=searchDataframe(f"{path_dir}/{filename}",str(row[1]).strip())
                        #Organizations Licenses
                        lic_org=[]
                        addlicorg=True
                        if addlicorg:
                                lic_org=""
                                if len(rowdata)>0:
                                        #print(rowdata[1])
                                        lic_org=license_organizations(rowdata,1,2,customer="lafayette") 
                                        
                        #CustomProperties
                        ###########################
                        #Defined Dictionary
                        #dict_term={"confidential":{"c"}}
                        ###########################
                        lic_customProperties={}
                        addcustomp= True
                        addlicTermIntegers=True
                        addlicTermText=True
                        if addcustomp:
                                #lic_customPropertiestext=""
                                #heads=license.
                                termPickupList=cpterm_PickupList(license.loc[i],2,3,6,7,8,9,10,11,12,13,14,15,dictiorarylicTerms=dicTerms)
                                if len(termPickupList)>0:
                                    lic_customProperties.update(termPickupList)
                                    #json_validator(str(lic_customProperties))
                                #to include integer license terms
                                if addlicTermIntegers:
                                    termInteger=cpterm_TextInteger(license.loc[i],17,18)
                                    if len(termInteger)>0:
                                        #print(lic_customPropertiesInteger)
                                        lic_customProperties.update(termInteger)
                                        #print(lic_customProperties)
                                       # json_validator(str(lic_customProperties))
                                if addlicTermText:
                                    termText=cpterm_TextInteger(rowdata,4,7,8,9,10,11,12,14,26)
                                    if len(termText)>0:
                                        lic_customProperties.update(termText)
                                json_validator(str(lic_customProperties))
                                #    pass
                                #else:
                                #    lic_customProperties={}
                                    
                                #termPickupList=cpterm_PickupList(rowdata,26,dictiorarylicTerms=dicTerms)
                                #if len(termPickupList)>0:
                                    #lic_customProperties.update(termPickupList)
                                      
                        #License External links to Documents 
                        #Define TRUE/ FALSE if the License will have link to external links, https, http.                       
                        ## Add docs
                        lic_docs=[]
                        adddocs= True
                        if adddocs:
                                if len(rowdata)>0:
                                    lic_docs=""
                                    lic_docs=license_docs(rowdata,5)
                                
                        #Sumplementary Docs
                        lic_supplementaryDocs=[]
                        addlicsupp= False
                        if addlicsupp:
                                lic_supplementaryDocs=license_supplementaryDocs()      
                                 
                        ##Amendments
                        lic_amendments=[]
                        addamendments= False
                        if addamendments:
                                lic_amendments=""
                                lic_amendments=license_amendments()        
                        ##add link      
                        addlink=False
                        if addlink:
                                lic_links=license_links()


                        #License Links
                        lic_links={}
                        addliclink=False
                        if addliclink:
                                lic_links=""
                                lic_links=license_links()
                        
                        id=str(uuid.uuid4())
                        file_path="lafayette"
                        org=licenses(id)
                        #(self, ermName, vendor,ermDescription, ERMlicType, ERMlicstatus, ErmstartDate, ermendDate,docs,
                        # aliases,ermopenEnded,cp,path):
                        org.licencePrint(lic_name, lic_org, lic_description, lic_type, lic_status, lic_startDate,lic_endDate,lic_docs,
                                         lic_alternateNames, lic_openEnded, lic_customProperties,file_path)
                        print("################# END Record Number: "+str(cont)+"\n")
        except ValueError:
            print("Main Error: "+str(ValueError))
            
           

######
def Readnotes(file_path):
    license=faf.readFileToDataFrame(file_path)
    for i, row in license.iterrows():
        lic_id=str(row[1]).strip()
        licId=faf.get_licId(toSearch,okapi_url="https://okapi-lafayette.folio.ebsco.com",okapi_token=,okapi_tenant="fs00001054")
        
######
def org_aliases(dfRow,*argv):
    alia={}
    aliaR=[]
    for arg in argv:
        #print("argumentos de *argv:", row[arg])
        if len(dfRow[arg])>0:
            alia['value']=dfRow[arg]
            alia['description']=""
            aliaR.append(alia)
            alia={}
    
    return aliaR


if __name__ == "__main__":


    customerName="lafayette"
    path_dir: str=r"C:\Users\asoto\Documents\EBSCO\Migrations\folio\Lafayette"
    
    filename="License_export1_fixed_fields.xlsx"
    path_file: str = path_dir + "/" + filename  
    typeFile=1 #1 spreadsheet, 2 CSV
    #readOrganizations(f"{path_dir}/{filename}","ORGANIZATIONS" ,customerName,typeFile)
    readSpreadsheet(f"{path_dir}\{filename}",customerName)