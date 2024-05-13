prompt = """

user query = {}

You have a  table and its name :fertilizer table and its schema definition is here:
for every user query always gives count with the answer. give answer in a conversational way, also return the sql query for the same
For Application_Status column here is description(Code 99 indicate: objection in application, code 9 indicate: application rejected, code 3 indicate: application submitted, 
code 3 indicate:Approved. for code 0,1,2 indicate pending.
Overdue column has information about the overdue of fertilizer application.
Application_Id: It has unique application id of fertilizer
Parent_Application_Id: It has unique parent applicaiton id
Process_Id: it has unique process id
Payment_Status: its has different coding format and its defenition is here:(Code 99 indicate: objection in application,code 9 indicate: application rejected,code 3 indicate:Approved,code 0,1,2 indicate pending)
Is_Service_Completed:its two value(0 indicate in draft mode and 1 indicate application submitted)
Request_Id_Fk: It is uniques request id of application and is a foreign key linked with multiple table.
Application_Status: having different application status
Amount: Its has informaiton about fees collected for fertilizer license.
RejectionRemarks: It has different rejection remark of actor.




APP_SERVICE_FERTILIZER: For fertilizer license service you have to check only this table and this table have request_id column as foreign key.
Md_Process_Workflow_Stage_Actions_Dtl:for action detail on fertilizer licesne you have to look on this table and has common request_id of license.
Md_Process_Workflow_Stage_Master:For actio title and role_id you have to look only this table,Here you will find next stage_id and next_role_id .
App_Service_Request_Activity_Detail:for application current stage and stage title and stage pending for detail you have to check this table only.
Temp_Dist_Fertilizer: For District_id, District_name, Firm_Name and firm validity details you have to look only for this table.
App_Service_Request_Actors_Detail:For activity_id,Emp_id-foreign key and post_id query you have to look for this table.
App_User_Post_Role_Mapping: For post_id and role_id you have to look for this table only.
App_User_Post_Master:for post_id and post_title you have to search into this table.
 Md_Roles_Master: For role_title and  role_id you have check for this table.


You have a table and its name: md_process_workflow_stage_master table and its schema definition is here:

Action_id: Its a unique action id of an actor.
Processs_Id_Fk: Its an unique process id of an actor for a process
Action_Title: This is an action remark given by an actor
Stage_Id_Fk: This is unique stage id of a process
Role_Id_Fk :Role id is an unique roll id
Next_Stage_Id_Fk: This is new stage id of process and its a foreign key
Next_Role_Id_Fk: this is new role id and foreign key
Action_UI_Flag: Its an action ui flag taken by an actor
Action_UI_FormType_Flag: Its has multiple type of action ui form type
Action_DB_Flag:indicate the process to assign new actor

You have a table and its  name : app_service_sequest_activity_detail table and its schema definition is here:

Activity_Id:This is unique activity id of an actor activity
Request_Id_Fk:This is unique request id and it is a foreign key linked with multiple table
 stage_Id: This is stage is of an application
Action_Id_FK: This is unique action id of an actor
Action_Date: This is action date of a process
action_remarks: It has action remark details
Emp_Id_Fk: It has unique emp_id and it is  a foreign key and also available in multiple table
Post_Id_Fk: It has unique post id and it is a foreign key
Action Remark: It has unique action remark given by an actor

You have a table and its name name : app_service_request_actors_detail table and its schema definition is here:

Action Remark: It has unique action remark given by an actor
Request_Id_Fk: this is unique reqest id and it is a foreign key
Activity_Id: it is a unique activity id
Emp_Id_Fk: its an unique emp id and is a foreign key
Post_Id_Fk: it is a n unique post id and is a foreign key
Assigned_On : this assigned date of any application
Is_Current : it has current status of appliction, and 0: no pendency and 1: application pending
Role_level: it has role level of an actor

You have a table and its name : md_process_workflow_stage_master table and its schema definition is here:
stage_id: this is unique stage id
process_id_fk: it is a unique process id and it is a foreign key
stage_title: it has stage title
stage_pending_for :It has information about pending stae
stage_type: in which stage its pending
is_first_stage: it is stage of application
created_on: application creation date
created_by_emp:from which employee its created
created_by_Post: from which post its created

You have a table and its name : md_Office_master table and its schema definition is here:
office_id :It has a unique office id   
state_id_fk:it has a unique state id and is a foreign key
district_id_fk :it has a unique district id and is a foreign key
Tehsil_id_fk : it has a unique tehsil id and is foreign key
Block_Id_fk: it has a unique block id and is foreign key
Department_id_fk : it has unique department id and is foreign key
Office_Name: It has  office name
Office_Level_Id_Fk: It has unique officer level id and its a foreign key



You have a table and its name : md_roles_master table and its schema definition is here:

Role_id : It has unique role id
Post_Id : Its has unique post id
Office_Id: It has unique office id
Post_Title: It has unique post title
Role_Title: It has unique Role title
Role_Level: It has unique role level
Department_id_fk	: it has unique department id and is foreign key


You have a table and its name : temp_dist_fertilizer table and its schema definition is here:
District_ID: It has uniuqe district id
Name_of_District: It has unique district name
Firm_Name : It has unique firm name
Proprietor_Name : It has Proprietor Name

You have another table name : md_process_workflow_wtage_actions_dtl table and its schema definition is here:
Action id :it is unique action id
process_id_fkit : is a unique process id and it is a foreign key
action_title :it is a unique action title
action_type : it is a uniue action type
state_id_fk : its uniue state id and is foriegn key
role_id_fk : it is a unique role_id and is a foriegn key
next_stage_id_fk : its next stage id of an application and it is a foreign key
next_role_id_fk : it is a next role id and is a foreign key
mandatory_doc_flag:  It has mandatory doc flag
action_ui_flag: it has unique action flag
action_ui_form_type_flag   :  type of action ui form type flag
action_db_flag: action db flag and has information about application assigned to different actor
created_on	: in which date created on
created_by_emp	:from which employee its crated
created_by_Post	: from which post its created








fertilizer table:
Application_Status: Code 99 (objection in application), Code 9 (application rejected), Code 3 (application submitted), Code 3 (Approved), Code 0,1,2 (pending)
Overdue: Overdue of fertilizer application

Md_Process_Workflow_Stage_Master table:

Action_id: Unique action id of an actor
Processs_Id_Fk: Unique process id of an actor for a process
Action_Title: Action remark given by an actor
Stage_Id_Fk: Unique stage id of a process
Role_Id_Fk: Unique role id
Next_Stage_Id_Fk: New stage id of process (foreign key)
Next_Role_Id_Fk: New role id (foreign key)
Action_UI_Flag: Action UI flag taken by an actor
Action_UI_FormType_Flag: Multiple types of action UI form type
Action_DB_Flag: Indicates the process to assign a new actor

App_Service_Request_Activity_Detail table:

Activity_Id: Unique activity id of an actor activity
Request_Id_Fk: Unique request id (foreign key)
Stage_Id: Stage id of an application
Action_Id_FK: Unique action id of an actor
Action_Date: Action date of a process
Action_Remarks: Action remark details
Emp_Id_Fk: Unique emp_id (foreign key)
Post_Id_Fk: Unique post id (foreign key)
Action Remark: Unique action remark given by an actor

App_Service_Request_Actors_Detail table:
Action Remark: Unique action remark given by an actor
Request_Id_Fk: Unique request id (foreign key)
Activity_Id: Unique activity id
Emp_Id_Fk: Unique emp id (foreign key)
Post_Id_Fk: Unique post id (foreign key)
Assigned_On: Assigned date of an application
Is_Current: Current status of the application
Role_level: Role level of an actor

Md_Process_Workflow_Stage_Master table:

Stage_id: Unique stage id
Process_id_fk: Unique process id (foreign key)
Stage_title: Stage title
Stage_pending_for: Pending stage information
Stage_type: Stage type
Is_first_stage: Stage of application
Created_on: Application creation date
Created_by_emp: Employee who created the application
Created_by_Post: Post who created the application

MD_Office_Master table:
Office_id: Unique office id
State_id_fk: Unique state id (foreign key)
District_id_fk: Unique district id (foreign key)
Tehsil_id_fk: Unique tehsil id (foreign key)
Block_Id_fk: Unique block id (foreign key)
Department_id_fk: Unique department id (foreign key)
Office_Name: Office name

Md_Roles_Master table:

Role_id: Unique role id
Department_id_fk: Unique department id (foreign key)
Role_title: Unique role title

Temp_dist_fertilizer table:

District_ID: Unique district id
Name_of_District: Unique district name
Firm_Name: Unique firm name
Proprietor_Name: Proprietor Name
Md_Process_Workflow_Stage_Actions_Dtl table:
Action id: Unique action id
Process_id_fk: Unique process id (foreign key)
Action_title: Unique action title
Action_type: Unique action type
State_id_fk: Unique state id (foreign key)
Role_id_fk: Unique role_id (foreign key)
Next_stage_id_fk: Next stage id of an application (foreign key)
Next_role_id_fk: Next role id (foreign key)
Mandatory_doc_flag: Mandatory doc flag
Action_ui_flag: Unique action flag
Action_ui_form_type_flag: Type of action UI form type flag
Action_db_flag: Action DB flag (information about application assigned to different actor)
Created_on: Date created
Created_by_emp: Employee who created
Created_by_Post: Post who created



"""
