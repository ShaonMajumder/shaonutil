# Utility Functions for developers
    Author: Shaon Majumder
    Stable Version: 0.0.0.46.1

## Utilities
- stats
- network
- image
- string
- file

## Installation
	pip install shaonutil

## Function Usages

### None
Function show_info(functionNode,ModuleName,classobj)
Function generateModuleFunctionUsageString(ModuleName)
Function generateDirFunctionUsageString()
Function get_members(module)
Function get_file_description_file(module)
Function createNewReadme()
Function generateFunctionUsagesString(realcurrentpath)
Function init(args)
Function main()
### File
Function package_exists(package_name) -> Description: check if a python pcakage exists.
Function pip_install(package_name)
Function get_all_functions(object) -> Description: shaonutil.file.get_all_functions(object/file/class)
Function ConfigSectionMap(Config,section)
Function read_configuration_ini(filename)
Function read_safecase_configuration_ini(filename)
Function write_configuration_ini(configs_par,filename,f_mode)
Function read_json(filename) -> Description: Read JSON file and return dictionary
Function write_json(obj,filename) -> Description: Write JSON file
Function read_file(filename) -> Description: Read File and return lines as list
Function write_file(filename,strs,mode) -> Description: Write File from string
Function read_pickle(filename)
Function write_pickle(filename,obj_)
Function open_file_with_default_app(filepath)
Function get_last_file_of_dir(filename)
Function remove_duplicateLines_from_file(filename)
Class CaseConfigParser
    Function optionxform(optionstr)
### None
### Image
Function svg2img(infile,outfile)
Function svg2pdf(infile,outfile)
Function change_image_size_ratio(img_name,out_name,percent)
Function draw_text(img,text,fnt_name,fnt_size)
Function merge_horizontally(images,filename)
Function merge_vertically(images,filename)
Function give_screenshot_caption(img_name,text,fnt_path)
### BarCode
Function calculate_checksum(data) -> Description: Calculates the checksum for EAN13-Code / EAN8-Code return type: Integer
Function verify_data(data) -> Description: Verify the EAN encoded data
Function actual_data(decodedObjects) -> Description: Returns data without checksum digit for EAN type
Function encode(type_,file_,data,rt) -> Description: Encode the data as barcode or qrcode
Function decode(infile,log) -> Description: Decode barcode or qrcode
Function displayBarcode(im,decodedObjects) -> Description: Mark and show the detected barcode
Function make_barcode_matrix(type_,unique_ids,row_number,column_number,filename) -> Description: Make barcode matrix image
Function read_live_barcode(detection_threshold) -> Description: Live read the barcode and returns data
### Mysql Database
Function create_configuration(option) -> Description: Creating Configuration
Class MySQL -> Description: A class for all mysql actions
    Function __init__(config,log)
    Function reopen_connection() -> Description: reopen
    Function close_connection()
    Function config()
    Function config(new_value)
    Function filter_config()
    Function make_cursor()
    Function is_mysql_user_exist(mysql_username)
    Function listMySQLUsers() -> Description: list all mysql users
    Function createMySQLUser(host,userName,password,querynum,updatenum,connection_num)
    Function grantMySQLUserAllPrivileges(host,userName,querynum,updatenum,connection_num)
    Function is_db_exist(dbname)
    Function create_db(dbname)
    Function is_table_exist(tbname)
    Function create_table(tbname,column_info)
    Function get_columns(tbname)
    Function get_columns_names(tbname)
    Function get_unique_id_from_field(key_length,field_name)
    Function insert_data(value_tupple)
### Network
Function url_encoding_to_utf_8(url) -> Description: url_encoding_to_utf_8(url)
Function check_valid_url(url)
Class Email
    Function __init__()
    Function authentication()
    Function authentication(new_value)
    Function send_email(receiver_address,subject,mail_content,attachment_file_link,log)
### OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).

### Process
Function is_process_exist(process_name)
Function kill_duplicate_process(process_name,log) -> Description: Kill a process if there is more than one instance is running.
Function killProcess_ByAll(PROCNAME)
Function killProcess_ByPid(pid)
Function list_processes(sort,save_file,log)
Function start_mysql_server(mysql_bin_folder,mysql_config_file) -> Description: Start mysql server
Function remove_aria_log(mysql_data_dir) -> Description: Removing aria_log.### files to in mysql data dir to restart mysql
Function get_mysql_datadir(mysql_bin_folder,user,pass_) -> Description: Get mysql data directory
Function computer_idle_mode()
Function obj_details_dump(obj) -> Description: check dump
### Statistics
Function counter(li,number)
Function occurance_dic(li)
Function mean(li) -> Description: Avearage or mean of elements - shaonutil.stats.mean(list of numbers)
Function median(li) -> Description: Median of elements - shaonutil.stats.median(list of numbers)
Function mode(li) -> Description: Mode of elements - shaonutil.stats.mode(list of numbers)
### String
Function nicely_print(dictionary,print) -> Description: Prints the nicely formatted dictionary - shaonutil.strings.nicely_print(object)
Function change_dic_key(dic,old_key,new_key) -> Description: Change dictionary key with new key
Function randomString(stringLength) -> Description: Generate a random string of fixed length 
Function generateSecureRandomString(stringLength) -> Description: Generate a secure random string of letters, digits and special characters 
Function generateCryptographicallySecureRandomString(stringLength,filters) -> Description: Generate a random string in a UUID fromat which is crytographically secure and random
### Windows
Function is_winapp_admin()
Function get_UAC_permission(func)


Function Usages End

## Versioning

 *major.minor[.maintenance[.build]]* (example: *1.4.3.5249*) 

adoption: major.minor.patch.maintenance.status.trials_for_success

The last position 

- 0 for alpha (status)
- 1 for beta (status)
- 2 for release candidate
- 3 for (final) release

For instance: 

- 1.2.0.1 instead of 1.2-a1
- 1.2.1.2 instead of 1.2-b2 (beta with some bug fixes)
- 1.2.2.3 instead of 1.2-rc3 (release candidate)
- 1.2.3.0 instead of 1.2-r (commercial distribution)
- 1.2.3.5 instead of 1.2-r5 (commercial distribution with many bug fixes)