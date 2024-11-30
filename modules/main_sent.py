def get_row1():
    row1="#"
    #orig_sent_copy=run_generate_usr.orig_sent_copy
    '''for p_list in parser_output_list:
        row1=row1+" "+p_list[1]
    row1=row1.replace("|","।")'''
    file_temp=open("txt_files/bh-2","r",encoding="UTF-8")
    sent_temp=file_temp.readline()
    #print("sent_temp",sent_temp)
    file_temp.close()
    row1=row1+""+sent_temp
    row1=row1.strip()
    #print("row1:",row1)
    return row1

if __name__=="__main__":
    row1 = get_row1()  # Call the get_row1() function to get the first row
    print(row1)  # Print the first row
